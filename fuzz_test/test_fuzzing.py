# -*- coding: utf-8 -*-
import marshal
import hashlib
import random
import string

FUZZ_COUNT = 50
TEST_ROUND = 3


def generate_fuzz_data():
    rand_str = ''.join(random.sample(string.ascii_letters, random.randint(1, 30)))
    rand_num = random.randint(-10000, 10000)
    rand_float = random.random()
    return [rand_str, rand_num, rand_float, [rand_str]]


def check_fuzz_stability(obj, idx: int) -> bool:
    hash_result = []
    for _ in range(TEST_ROUND):
        stream = marshal.dumps(obj)
        hash_result.append(hashlib.md5(stream).hexdigest())
    stable = len(set(hash_result)) == 1
    status = "STABLE" if stable else "UNSTABLE"
    print(f"Fuzz Sample {idx} : {status}")
    return stable


def run():
    print("\n----- Fuzzing Test -----")
    unstable_cnt = 0
    for i in range(1, FUZZ_COUNT + 1):
        fuzz_obj = generate_fuzz_data()
        if not check_fuzz_stability(fuzz_obj, i):
            unstable_cnt += 1
    print(f"Total samples: {FUZZ_COUNT}, Unstable samples: {unstable_cnt}")