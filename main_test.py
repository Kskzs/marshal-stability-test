# -*- coding: utf-8 -*-
"""
marshal 模块稳定性与正确性测试套件 - 主入口文件
遵循 PEP 8 编码规范
功能：统一调用所有分类测试模块，批量执行全部用例
"""
import os
import time

# 全局配置：日志文件夹
TEST_LOG_DIR = "test_log"
# 自动创建日志目录（不存在则新建）
os.makedirs(TEST_LOG_DIR, exist_ok=True)


def main():
    """主函数：按顺序执行所有测试模块"""
    print("=" * 60)
    print("Python marshal 模块稳定性测试套件 开始运行")
    print("=" * 60)

    # 导入各类测试模块
    from core_tests import test_basic, test_float, test_container
    from boundary_tests import test_empty, test_large_data, test_recursive
    from fuzz_test import test_fuzzing
    from cross_env import cross_os_compare, cross_version_compare

    # 依次执行测试用例
    test_basic.run()
    test_float.run()
    test_container.run()
    test_empty.run()
    test_large_data.run()
    test_recursive.run()
    test_fuzzing.run()
    cross_os_compare.run()
    cross_version_compare.run()

    # 测试结束提示
    print("\n" + "=" * 60)
    print(f"所有测试执行完成，日志目录：{TEST_LOG_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    # 统计整体运行耗时
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"\n本次测试总耗时：{end_time - start_time:.2f} 秒")