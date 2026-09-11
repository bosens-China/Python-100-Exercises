def validate_age(age):
    if type(age) is not int or not 0 <= age <= 120:
        raise ValueError("年龄必须是 0 到 120 的整数")
    return age
