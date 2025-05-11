from fair_rent_calc import adjust_rent

def test_adjust_rent():
    assert adjust_rent(1500, 48000, 0.08) < 1500
