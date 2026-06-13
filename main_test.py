# -*- coding: utf-8 -*-
"""
marshal 模块稳定性测试套件
运行环境：Windows
"""
import os
import sys

# 修复模块导入路径
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

import time

# 日志目录
TEST_LOG_DIR = "test_log"
os.makedirs(TEST_LOG_DIR, exist_ok=True)


def main():
    print("=" * 60)
    print("Python marshal Black-box Stability Test Suite Start")
    print("=" * 60)


    from core_tests import test_basic, test_float, test_container
    from boundary_tests import test_empty, test_large_data, test_recursive
    from fuzz_test import test_fuzzing
    from cross_env import cross_version_compare

    # 执行所有测试
    test_basic.run()
    test_float.run()
    test_container.run()
    test_empty.run()
    test_large_data.run()
    test_recursive.run()
    test_fuzzing.run()
    cross_version_compare.run()

    print("\n" + "=" * 60)
    print(f"All tests completed. Log dir: {TEST_LOG_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Total running time: {end - start:.2f} seconds")