# Python marshal Stability Test
软件工程课程作业：Python marshal 模块稳定性与正确性测试套件

## 项目介绍
本项目基于黑盒+白盒测试技术，验证 `marshal` 序列化输出的确定性，覆盖：
- 基础数据类型、浮点数(NaN/Inf)
- 空容器、超大集合、递归循环结构
- 模糊测试、跨操作系统、跨Python版本测试

## 运行环境
- Python 3.7.4 3.10.8 3.11.9
- 依赖：pytest, coverage

## 安装依赖
```bash
pip install pytest coverage
