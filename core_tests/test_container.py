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
    unique_hash = set(hash_list)
    import sys
    ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"【{desc}】Current Version: Python {ver}")
    print(f"Hash values: {unique_hash}")
    status = "✅ 稳定" if is_stable else "❌ 不稳定"
    print(f"{status}\n")
    return is_stable


def run():
    print("\n----- 常规容器测试 -----")
    check_stability([1, 2, 3], "普通列表")
    check_stability((10, 20, 30), "元组")
    check_stability({"name": "test", "age": 18}, "字典")
    check_stability([1, "text", 3.14, True], "混合类型容器")

    a = [1, 2]
    b = {"data": a}
    a.append(b)
    check_stability(a, "双向循环嵌套容器")
    
    recur_list = [1, 2, 3]
    recur_list.append(recur_list)
    check_stability(recur_list, "递归自引用列表")