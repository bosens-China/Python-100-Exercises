# 051 · 读取练习文件

## 学习目标

用 with 管理文本文件。

## 前置知识

先完成第 050 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`with open(path, "r", encoding="utf-8") as file:` 打开文本，`file.read()` 读取全部内容；离开 with 会自动关闭。路径属于练习工作区。

## 任务与约定

完成 `read_text(path)`，path 为已经存在的 UTF-8 文本文件路径，返回全部内容，保留换行和首尾空白。测试会提供文件，无需上传或准备。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

文件内容为 `你好\nPython\n` 时，返回同样的文本。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

指定 UTF-8 编码。

</details>

<details>
<summary>提示 2：实现方向</summary>

不要 strip 文件内容。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
