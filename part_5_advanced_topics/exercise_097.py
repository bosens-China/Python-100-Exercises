"""
题目 097: 为不稳定操作添加重试

要求:
实现 `retry_call(function, attempts=3)`，调用不需要参数的 `function`。
如果调用抛出异常，就重试，最多调用 `attempts` 次；成功时立即返回结果。
所有尝试都失败时，重新抛出最后一次异常。
`attempts` 小于 1 时抛出 `ValueError`。

提示:
先验证参数，再使用循环。不要吞掉最后一次异常。
"""


def retry_call(function, attempts=3):
    # 在这里写下你的代码
    pass
