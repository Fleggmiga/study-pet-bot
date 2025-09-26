from dataclasses import dataclass
from typing import Tuple

SESSION_MIN = 5
SESSION_MAX = 120
DAILY_CAP = 720

@dataclass
class DayStats:
    minutes_today: int = 0
    full_30m_sessions: int = 0  #for satiety bonus calc

def level_for_xp(xp: int) -> int:
    return 1 + max(0, xp) // 300

def xp_to_next(xp: int) -> int:
    nxt = ((max(0, xp) // 300) + 1) * 300
    return max(0, nxt - max(0, xp))

def clamp(v: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, v))

def validate_session(add_minutes: int, minutes_today: int) -> Tuple[bool, str]:
    if add_minutes < SESSION_MIN:
        return False, f"Minimum is {SESSION_MIN} minutes."
    if add_minutes > SESSION_MAX:
        return False, f"Maximum per entry is {SESSION_MAX} minutes."
    if minutes_today + add_minutes > DAILY_CAP:
        return False, f"Daily cap {DAILY_CAP} minutes reached."
    return True, "OK"

def apply_daily_boost(today_minutes: int, health: int) -> Tuple[str, int]:
    if today_minutes >= 60:
        return "good", clamp(health + 10, 0, 100)
    if today_minutes >= 10:
        return "neutral", health
    return "bad", health

def apply_decay(days_without_study: int, health: int) -> int:
    if days_without_study >= 3:
        return clamp(health - 5 * days_without_study, 0, 100)
    return health

def update_satiety(satiety: int, full_30m_sessions: int) -> int:
    #daily baseline -10; +5 per full 30m session
    return clamp(satiety - 10 + 5 * max(0, full_30m_sessions), 0, 100)
