#Study Pet Bot- Product Spec

##Problem
Studying is hard to sustain. Timers feel like chores. Gamification with a pet makes progress tangible and fun.

## Solution
Telegram bot where your virtual pet grows with study time. Clear weekly goals, mood/health feedback, and light social comparison.

## Commands
- `/pet`- pet card (name, level, xp→next, mood, satiety, health, weekly goal/progress). Inline: Pet me / +30m /Set goal //Achievements.
- `/study <minutes>`- adds minutes; constraints: 5–120 per entry, ≤720/day; soft rate limit.
- `/ach`- analytics (Today /This week /This month).
- `/help`- brief manual + rules.
- (Optional later) `/pass`, `/invite`, `/friends`, `/compare @user`, `/leaderboard`.

##Copy (English)
Start: “Hello! So you finally decided to take control and start your personal growth? I’ve got a small gift and a reason to keep you moving. This little fluff ball is now part of your family- take care of it!”
After naming: “Great! Your pet’s name is {name}. Set a weekly study goal to earn level-ups and free passes.”

##Non-functional
- Friendly tone, short messages, minimal emojis.
- Privacy: friends see only aggregates (weekly minutes, %, streak, level).
