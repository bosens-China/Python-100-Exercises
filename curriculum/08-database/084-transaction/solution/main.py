def transfer(db, source, target, amount):
    if amount <= 0 or source == target:
        raise ValueError("转账参数无效")
    source_row = db.execute(
        "SELECT balance FROM accounts WHERE id = ?", (source,)
    ).fetchone()
    target_row = db.execute(
        "SELECT balance FROM accounts WHERE id = ?", (target,)
    ).fetchone()
    if source_row is None or target_row is None:
        raise KeyError("账户不存在")
    if source_row[0] < amount:
        raise ValueError("余额不足")
    with db:
        db.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, source)
        )
        db.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, target)
        )
