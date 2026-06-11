# -*- coding: utf-8 -*-
import marshal
import hashlib

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

    is_stable = len(set(hash_list)) == 1
    status = "✅ 稳定" if is_stable else "❌ 不稳定"
    print(f"【{desc}】{status} | 哈希集合：{set(hash_list)}")
    return is_stable


def run():
    print("\n----- 基础数据类型测试 -----")
    # 测试用例
    check_stability(12345, "普通整数")
    check_stability(2 ** 64, "超大整数")
    check_stability("hello world", "普通字符串")
    check_stability(True, "布尔值 True")
    check_stability(False, "布尔值 False")
    check_stability(None, "空对象 None")