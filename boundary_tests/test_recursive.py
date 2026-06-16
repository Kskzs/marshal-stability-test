# -*- coding: utf-8 -*-
import marshal
import hashlib

TEST_ROUND = 10


def check_stability(obj, desc: str) -> bool:
    hash_result = []
    for _ in range(TEST_ROUND):
        stream = marshal.dumps(obj)
        hash_result.append(hashlib.md5(stream).hexdigest())
    stable = len(set(hash_result)) == 1
    status = "STABLE" if stable else "UNSTABLE"
    print(f"{desc} : {status}")
    return stable


def run():
    print("\n----- Recursive & Cyclic Structure Test -----")
    cycle_list = []
    cycle_list.append(cycle_list)
    check_stability(cycle_list, "Self-referencing List")

    a = []
    b = [a]
    a.append(b)
    check_stability(a, "Nested Recursive Structure")