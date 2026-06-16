# -*- coding: utf-8 -*-
import marshal
import hashlib
import math
import sys
import os
from datetime import datetime

# 日志目录统一，修复之前导入报错
TEST_LOG_DIR = "test_log"
os.makedirs(TEST_LOG_DIR, exist_ok=True)

def get_python_ver():
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

def calc_md5(data):
    dump_bin = marshal.dumps(data)
    return hashlib.md5(dump_bin).hexdigest()

def safe_equal(origin, restore):
    # NaN专用判断逻辑
    if isinstance(origin, float) and math.isnan(origin):
        return isinstance(restore, float) and math.isnan(restore)
    return origin == restore

def run():
    log_path = f"{TEST_LOG_DIR}/float_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_file = open(log_path, "w", encoding="utf-8")
    py_ver = get_python_ver()

    # 包含Inf、-Inf、普通浮点、NaN四条用例
    float_cases = [
        ("Inf Value", float("inf")),
        ("-Inf Value", float("-inf")),
        ("Normal Float", 3.1415926),
        ("NaN Value", float("nan"))
    ]

    log_file.write(f"===== Float Test | Python {py_ver} =====\n")
    print("\n----- Float Test -----")

    for case_name, data in float_cases:
        hash_records = []
        stable_flag = True

        for _ in range(10):
            md5_val = calc_md5(data)
            hash_records.append(md5_val)

            bin_buf = marshal.dumps(data)
            restore_obj = marshal.loads(bin_buf)
            if not safe_equal(data, restore_obj):
                stable_flag = False

        unique_hash = set(hash_records)
        output_line = f"【{case_name}】Current Version: Python {py_ver}\nHash values: {unique_hash}\nStable: {stable_flag}\n"
        print(output_line)
        log_file.write(output_line + "\n")

    log_file.close()
    print(f"Float test log saved: {log_path}")