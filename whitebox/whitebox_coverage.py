# -*- coding: utf-8 -*-
import coverage
from marshal_wrapper import dumps, loads, full_cycle

# 只统计当前目录下的业务代码
cov = coverage.Coverage(source=["."])
cov.start()

# 全部测试用例
full_cycle(123)
full_cycle(-999)
full_cycle("hello marshal")
full_cycle(b"binary data")
full_cycle([1, "2", 3.0])
full_cycle({"name": "test", "num": 666})
full_cycle((10, 20, 30))
full_cycle(None)
full_cycle(True)
full_cycle(False)

data = dumps(12345)
res = loads(data)
data = dumps(12345)
res = loads(data)
print("All test cases executed successfully")

cov.stop()
cov.save()

print("\n===== 代码覆盖率文本报告 =====")
cov.report()
cov.html_report(directory="html_report")
print("\nHTML覆盖率报告生成完成，打开 html_report/index.html 查看")