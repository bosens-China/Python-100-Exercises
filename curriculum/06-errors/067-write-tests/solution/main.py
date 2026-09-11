def check_shipping(shipping):
    assert shipping(0) == 800
    assert shipping(9899) == 800
    assert shipping(9900) == 0
    assert shipping(12000) == 0
