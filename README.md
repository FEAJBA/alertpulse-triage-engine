# AlertPulse - SOC Alert Triage Engine

A Python-based Security Operations Center (SOC) Alert Triage Engine that helps analysts cut through alert fatigue by deduplicating, scoring, and prioritizing security alerts.

## The Problem: Alert Fatigue

Modern SOC teams receive thousands of alerts every day from SIEM, EDR, Firewall, and IDS systems.
- 90%+ of alerts are duplicates or low-value noise
- Analysts waste hours manually grouping the same attack
- Real critical attacks get buried under noise
- Mean Time To Respond (MTTR) increases

AlertPulse solves this by automatically grouping, scoring, and ranking alerts so analysts investigate the most dangerous threats first.

## Features

- **Deduplication:** Groups 100 raw alerts into unique incidents by `src_ip + rule`
- **Noise Reduction:** Removes 97% duplicate noise
- **Risk Scoring:** Assigns severity score based on attack type
    - Port Scan = 95 (CRITICAL)
    - Brute Force = 95 (CRITICAL)
    - Malware Beacon = 75 (HIGH)
- **Prioritization:** Sorts alerts from highest to lowest risk
- **Clear Output:** Analyst-friendly triage summary

## How It Works

1. **Ingest:** Loads raw alerts from SIEM
2. **Group:** Uses `defaultdict` to group by `(src_ip, rule)`
3. **Score:** Maps each rule to a risk score and severity
4. **Rank:** Sorts grouped alerts by score descending
5. **Report:** Prints top priority alerts for investigation

## Example Output

[+] Loaded 100 raw alerts from SIEM
[+] After Deduplication: 3 unique alerts
[+] Reduction: 97% noise removed

TOP PRIORITY ALERTS:
CRITICAL | Score: 95 | Port Scan | 192.168.1.10 | Count: 80
CRITICAL | Score: 95 | Brute Force | 10.0.0.5 | Count: 12
HIGH     | Score: 75 | Malware Beacon | 172.16.0.20 | Count: 8

[+] Triage Complete. Analyst should investigate CRITICAL first.

## Project Structure

AlertPulse/
├── src/
│   └── main.py          # Main triage engine
├── README.md

## How To Run

1. Go to https://www.programiz.com/python-programming/online-compiler/
2. Copy code from `src/main.py`
3. Paste and click **Run**

Or locally:
```bash
python src/main.py
