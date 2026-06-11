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
    status = "? 稳定" if is_stable else "? 不稳定"
    print(f"【{desc}】{status}")
    return is_stable


def run():
    print("\n----- 递归/循环结构测试 -----")
    # 自引用列表
    cycle_list = []
    cycle_list.append(cycle_list)
    check_stability(cycle_list, "自引用循环列表")

    # 多层嵌套递归
    a = []
    b = [a]
    a.append(b)
    check_stability(a, "双层嵌套递归结构")