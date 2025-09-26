from src.logic import level_for_xp, xp_to_next, validate_session, apply_daily_boost, apply_decay, update_satiety

def test_level_progression():
    assert level_for_xp(0) == 1
    assert level_for_xp(299) == 1
    assert level_for_xp(300) == 2
    assert level_for_xp(615) == 3

def test_xp_to_next():
    assert xp_to_next(0) == 300
    assert xp_to_next(299) == 1
    assert xp_to_next(300) == 300

def test_validate_session():
    ok, _ = validate_session(5, 0); assert ok
    ok, _ = validate_session(4, 0); assert not ok
    ok, _ = validate_session(121, 0); assert not ok
    ok, _ = validate_session(60, 700); assert not ok

def test_daily_boost_and_decay():
    mood, h = apply_daily_boost(5, 80);  assert mood == "bad" and h == 80
    mood, h = apply_daily_boost(20, 80); assert mood == "neutral" and h == 80
    mood, h = apply_daily_boost(60, 95); assert mood == "good" and h == 100
    assert apply_decay(0, 90) == 90
    assert apply_decay(2, 90) == 90
    assert apply_decay(3, 90) == 75

def test_satiety():
    assert update_satiety(70, 0) == 60
    assert update_satiety(98, 2) == 100
