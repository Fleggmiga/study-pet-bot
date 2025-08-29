#Study Pet Bot- Portfolio Repo (Spec + Code Skeleton)
A Telegram bot concept that gamifies learning with a virtual pet.
This repository includes a clear product spec, mechanics, data model, and a Python AIogram skeleton with unit‑tested core logic.

>Intentional: The bot skeleton compiles and shows the command structure, but persistence/auth/etc. are simplified. Focus is on design and engineering structure.

##MVP Features
- `/pet`- pet card: Name, Level, XP→next, Mood, Satiety, Health, weekly goal/progress, sticker preview; inline actions.
- `/study <minutes>`- adds study time;limits (5-120 per entry, ≤720/day); daily mood/health boosts.
- `/ach`- analytics (Today/Week/Month- simplified stub here).
- Weekly goal with level-up; health decay after ≥3 days inactivity; satiety over days.
- Social stubs: `/invite`, `/accept`, `/friends`, `/leaderboard` (in‑memory for demo).

##Core Mechanics (short)
- XP: 1 xp per minute.
- Level: `1 + xp // 300` (plus +1 on weekly-goal completion).
- Daily ≥ 60m → Mood good, Health +10%(cap 100).
- Inactivity ≥ 3 days → on next interaction −5%/day (lazy apply).
- Satiety: −10/day baseline, +5 per full 30‑minute session (cap 100).

Full details in docs/.
##Roadmap
- Spec + logic + tests (this repo)
- SQLite persistence + screenshots
- Friends/leaderboard persistence + simple CI

