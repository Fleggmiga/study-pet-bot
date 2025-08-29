#Data Model (simplified for portfolio)
```json
{
  "user_id": 123456,
  "pet": {
    "name": "Mochi",
    "level": 3,
    "xp": 740,
    "health": 85,
    "satiety": 70,
    "mood": "neutral",
    "sticker_pack": "CuteCats",
    "sticker_file_id": "AAEAA...xyz"
  },
  "goals": {
    "weekly_minutes": 420,
    "week_progress": 310
  },
  "free_passes": 1,
  "timestamps": {
    "last_study_at": "2025-08-27T20:10:00Z",
    "last_decay_date": "2025-08-28"
  }
}
```
- `study_sessions`: array of objects `{minutes, note?, created_at}`
- `friendships`: array of `{user_id, status}` with `status: pending|accepted|blocked`
