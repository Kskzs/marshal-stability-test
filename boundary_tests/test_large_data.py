# -*- coding: utf-8 -*-
import marshal
import hashlib

TEST_ROUND = 5


def check_stability(obj, desc: str) -> bool:
    hash_list = []
    for _ in range(TEST_ROUND):
        byte_stream = marshal.dumps(obj)
        hash_list.append(hashlib.md5(byte_stream).hexdigest())
    is_stable = len(set(hash_list)) == 1
    status = "✅ 稳定" if is_stable else "❌ 不稳定"
    print(f"【{desc}】{status}")
    return is_stable


def run():
    print("\n----- 超大容量集合测试 -----")
    big_list_1w = [i for i in range(10000)]
    big_list_10w = [i for i in range(100000)]
    check_stability(big_list_1w, "10000元素列表")
    check_stability(big_list_10w, "100000元素列表")