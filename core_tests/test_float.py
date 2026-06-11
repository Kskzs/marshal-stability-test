# -*- coding: utf-8 -*-
import marshal
import hashlib

TEST_ROUND = 10


def get_md5_hash(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


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
    print("\n----- 浮点数及特殊值测试 -----")
    check_stability(3.1415926, "普通浮点数")
    check_stability(float("nan"), "浮点 NaN")
    check_stability(float("inf"), "正无穷 Inf")
    check_stability(float("-inf"), "负无穷 -Inf")