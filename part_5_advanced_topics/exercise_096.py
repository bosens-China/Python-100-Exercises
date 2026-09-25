"""
题目 096: 使用标准库分析函数性能

要求:
实现 `profile_call(function, *args, **kwargs)`。
使用 `cProfile` 执行函数一次，返回 `(函数返回值, 性能报告字符串)`。
报告应包含函数调用统计，方便排查慢函数。

提示:
`cProfile.Profile().runcall(...)` 可以取得返回值；
`pstats.Stats` 配合 `io.StringIO` 可以生成报告字符串。
"""


def profile_call(function, *args, **kwargs):
    # 在这里写下你的代码
    pass
