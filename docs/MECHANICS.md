#Mechanics (Rules & Formulas)

## XP & Level
- XP = sum of minutes from /study
- Level= 1 + floor(XP / 300)
- Weekly goal completion → +1 additional level and +1 free pass (later)

##Session Constraints
- 5 ≤ minutes ≤ 120 per /study
- Daily cap: 600 minutes
- Soft rate limit: ≤ 6 entries / 10 minutes
- If entry ≥ 90 minutes, ask for a short note (“What did you study?”)

## Mood
- Today minutes: ≥60 → good; 10–59 → neutral; <10 → bad
- “Pet me” increases one step up to good (cooldown hours)

## Health
- +10% when mood == good today (cap 100)
- Decay: if no study for ≥3 days, apply −5% per day on next interaction (lazy)
- 0 ≤ Health ≤ 100

## Satiety
- Baseline −10 per day
- +5 per full 30-minute session
- 0 ≤ Satiety ≤ 100

## Weekly Progress
- Weekly goal in minutes (e.g., 300 = 5h). Track ISO week aggregates.
