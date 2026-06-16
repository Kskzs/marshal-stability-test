# -*- coding: utf-8 -*-
import marshal
import hashlib
import sys

TEST_ROUND = 10  # 每个对象重复测试次数


def get_md5_hash(data: bytes) -> str:
    """计算字节流MD5哈希值"""
    return hashlib.md5(data).hexdigest()


def check_stability(obj, desc: str) -> bool:
    """检测单个对象序列化稳定性，返回是否稳定"""
    hash_list = []
    for _ in range(TEST_ROUND):
        byte_stream = marshal.dumps(obj)
        current_hash = get_md5_hash(byte_stream)
        hash_list.append(current_hash)

    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    unique_hash = set(hash_list)
    is_stable = len(unique_hash) == 1
    status = "✅ 稳定" if is_stable else "❌ 不稳定"
    print(f"【{desc}】Current Version: Python {py_ver}")
    print(f"Hash values: {unique_hash}")
    print(f"{status}\n")
    return is_stable


def run():
    print("\n----- 基础数据类型测试 -----")
    # 常规基础用例
    check_stability(12345, "普通整数")
    check_stability(2 ** 64, "超大整数")
    check_stability("hello world", "普通字符串")
    check_stability(True, "布尔值 True")
    check_stability(False, "布尔值 False")
    check_stability(None, "空对象 None")

    # 编译代码对象，marshal可序列化，3.7与3.11哈希一定不同
    code_obj = compile("a = 100 + 200", "<demo>", "exec")
    check_stability(code_obj, "编译Code代码对象")