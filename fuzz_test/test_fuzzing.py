# -*- coding: utf-8 -*-
import marshal
import hashlib
import random
import string

FUZZ_COUNT = 50
TEST_ROUND = 3


def generate_fuzz_data():
    """生成随机混合测试数据"""
    random_str = ''.join(random.sample(string.ascii_letters, random.randint(1, 30)))
    random_num = random.randint(-10000, 10000)
    random_float = random.random()
    return [random_str, random_num, random_float, [random_str]]


def check_fuzz_stability(obj, idx: int) -> bool:
    hash_list = []
    for _ in range(TEST_ROUND):
        byte_stream = marshal.dumps(obj)
        hash_list.append(hashlib.md5(byte_stream).hexdigest())
    is_stable = len(set(hash_list)) == 1
    status = "? 稳定" if is_stable else "? 不稳定"
    print(f"【模糊样本{idx}】{status}")
    return is_stable


def run():
    print("\n----- 模糊测试（随机数据） -----")
    unstable_cnt = 0
    for i in range(1, FUZZ_COUNT + 1):
        fuzz_obj = generate_fuzz_data()
        if not check_fuzz_stability(fuzz_obj, i):
            unstable_cnt += 1
    print(f"模糊测试总计：{FUZZ_COUNT} 组，不稳定样本：{unstable_cnt} 组")