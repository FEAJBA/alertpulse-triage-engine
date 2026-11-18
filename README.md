# AlertPulse - SOC Alert Engine

>SOC analyst drown in 10,000+ alerts a day. AlertPulse cuts the noise.

## Problem 
90% of SOC alerts are duplicates / false positives. Analyst get and miss the real attacks.

## Solution 
AlertPulse groups alerts by IP + Rule, scores them, and outputs only the priority alerts.

## Lab test result
- Input: 100 raw alerts
- Output: 3unique alerts
- Noise Reductuion: 97%

## How to Run

```python
python src/main.py
```
## Tech 
python, JSON, Collections
