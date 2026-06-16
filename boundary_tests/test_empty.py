# -*- coding: utf-8 -*-
import marshal
import hashlib

TEST_ROUND = 10


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
    print("\n----- 空容器边界测试 -----")
    check_stability([], "空列表")
    check_stability({}, "空字典")
    check_stability("", "空字符串")
    check_stability((), "空元组")