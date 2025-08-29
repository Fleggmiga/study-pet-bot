#Portfolio skeleton for AIogram bot (no persistence; in-memory demo)
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .logic import level_for_xp, xp_to_next, validate_session, apply_daily_boost

TOKEN = os.getenv("TELEGRAM_TOKEN", "PUT_YOUR_TOKEN_HERE")
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

STATE = {}    # user_id -> state dict
FRIENDS = {}  # user_id -> set(friend_ids)
INVITES = {}  # code -> inviter_id

def get_user(uid: int):
    return STATE.setdefault(uid, {
        "name": None,
        "xp": 0,
        "health": 80,
        "satiety": 70,
        "mood": "neutral",
        "today": 0,
        "weekly": 0,
        "goal": 300  # minutes
    })

def friend_set(uid: int):
    return FRIENDS.setdefault(uid, set())

def kb_pet():
    kb = InlineKeyboardBuilder()
    kb.button(text="Pet me", callback_data="pet_me")
    kb.button(text="+30m", callback_data="plus_30")
    kb.button(text="Set goal", callback_data="set_goal")
    kb.button(text="Achievements", callback_data="ach")
    kb.adjust(2,2)
    return kb.as_markup()

@dp.message(Command("start"))
async def start(m: types.Message):
    u = get_user(m.from_user.id)
    welcome = ("Hello! So you finally decided to take control and start your personal growth? \n"
               "This little fluff ball is now part of your family- take care of it! \n\n"
               "Send me your pet's name.")
    await m.answer(welcome)

@dp.message(lambda msg: msg.text and not msg.text.startswith("/"))
async def set_name(m: types.Message):
    u = get_user(m.from_user.id)
    if u["name"] is None and len(m.text) <= 20:
        u["name"] = m.text.strip()
        await m.answer(f"Great! Your pet’s name is <b>{u['name']}</b>.",
                       reply_markup=kb_pet())

@dp.message(Command("pet"))
async def pet(m: types.Message):
    u = get_user(m.from_user.id)
    level = level_for_xp(u["xp"])
    card = (f" <b>{u['name'] or 'Unnamed'}</b>\n"
            f" Level: <b>{level}</b> (to next: {xp_to_next(u['xp'])} XP)\n"
            f"• Health: <b>{u['health']}%</b> · Satiety: <b>{u['satiety']}%</b>\n"
            f" Mood: <b>{u['mood']}</b>\n"
            f" Weekly goal: <b>{u['goal']//60}h</b> — Progress: <b>{u['weekly']//60}h {u['weekly']%60}m</b>")
    await m.answer(card, reply_markup=kb_pet())

@dp.message(Command("study"))
async def study(m: types.Message):
    u = get_user(m.from_user.id)
    try:
        minutes = int((m.text or "").split(maxsplit=1)[1])
    except:
        return await m.answer("Usage: <code>/study 30</code>")
    ok, msg = validate_session(minutes, u["today"])
    if not ok:
        return await m.answer(f"{msg}")
    u["today"] += minutes
    u["weekly"] += minutes
    u["xp"] += minutes
    u["mood"], u["health"] = apply_daily_boost(u["today"], u["health"])
    await m.answer(
        f"Added <b>{minutes}m</b>. XP: <b>{u['xp']}</b> · Level: <b>{level_for_xp(u['xp'])}</b> "
        f"(to next: {xp_to_next(u['xp'])} XP). Mood: <b>{u['mood']}</b>"
    )

@dp.message(Command("ach"))
async def ach(m: types.Message):
    u = get_user(m.from_user.id)
    await m.answer(f"Today: {u['today']}m\nThis week: {u['weekly']}m / {u['goal']}m\n(Portfolio stub)")

#Social stubs
@dp.message(Command("invite"))
async def invite(m: types.Message):
    code = f"ref_{abs(hash(m.from_user.id)) % 1000000}"
    INVITES[code] = m.from_user.id
    await m.answer(f"Share this code to add friends:\n<code>{code}</code>\nUse /accept <code> to connect.")

@dp.message(Command("accept"))
async def accept(m: types.Message):
    parts = (m.text or "").split(maxsplit=1)
    if len(parts) < 2: return await m.answer("Usage: /accept ref_XXXXX")
    code = parts[1].strip()
    inviter = INVITES.get(code)
    if not inviter: return await m.answer("Invalid or expired code.")
    if inviter == m.from_user.id: return await m.answer("That's your own code.")
    friend_set(inviter).add(m.from_user.id); friend_set(m.from_user.id).add(inviter)
    await m.answer("Friendship established!")

@dp.message(Command("friends")) 
async def friends(m: types.Message):
    ids = sorted(friend_set(m.from_user.id))
    if not ids: return await m.answer("No friends yet. Use /invite.")
    lines = []
    for fid in ids:
        u = get_user(fid)
        pct = int(100 * u["weekly"] / max(1, u["goal"]))
        lines.append(f"• <b>{fid}</b> — {u['weekly']}m ({pct}%) · L{level_for_xp(u['xp'])}")
    await m.answer("Friends (weekly):\n" + "\n".join(lines))

@dp.message(Command("leaderboard"))
async def leaderboard(m: types.Message):
    ids = [m.from_user.id] + list(friend_set(m.from_user.id))
    rows = [(uid, get_user(uid)["weekly"]) for uid in ids]
    rows.sort(key=lambda t: t[1], reverse=True)
    text = "\n".join([f"{i+1}. <b>{uid}</b> — {w}m" for i,(uid,w) in enumerate(rows[:5])])
    await m.answer("Leaderboard (friends):\n" + (text or "—"))

# Optional local run
if __name__ == "__main__":
    import asyncio
    async def main():
        print("Study Pet bot stub running (portfolio mode).")
        await dp.start_polling(bot)
    asyncio.run(main())
