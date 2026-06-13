# -*- coding: utf-8 -*-
import marshal
import hashlib
import sys

TEST_ROUND = 5


def get_python_version() -> str:
    """Get current running Python version"""
    return f"Python {sys.version.split()[0]}"


def check_cross_version(obj, desc: str):
    """Check serialization result for single object"""
    print(f"【{desc}】Current Version: {get_python_version()}")
    hash_result = []
    for _ in range(TEST_ROUND):
        stream = marshal.dumps(obj)
        hash_result.append(hashlib.md5(stream).hexdigest())
    print(f"Hash values: {set(hash_result)}")


def run():
    print("\n----- Cross Python Version Test -----")
    # Test common objects
    test_dict = {"num": 999, "str": "version_test"}
    test_inf = float("inf")

    check_cross_version(test_dict, "Dict Object")
    check_cross_version(test_inf, "Inf Value")

    print("Tip: Run this script with different Python versions to compare results")