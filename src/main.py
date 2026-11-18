import json
from collections import defaultdict

print("="*55)
print("AlertPulse - SOC Alert Triage Engine")
print("="*55)

alerts = (
    [{"src_ip": "192.168.1.10", "rule": "Port Scan"}] * 80 +
    [{"src_ip": "10.0.0.5", "rule": "Brute Force"}] * 12 +
    [{"src_ip": "172.16.0.20", "rule": "Malware Beacon"}] * 8
)

print(f"\n[+] Loaded {len(alerts)} raw alerts from SIEM")

grouped = defaultdict(list)
for a in alerts:
    key = (a["src_ip"], a["rule"])
    grouped[key].append(a)

results = []
for (ip, rule), items in grouped.items():
    count = len(items)
    if count >= 10:
        severity, score = "CRITICAL", 95
    elif count >= 5:
        severity, score = "HIGH", 75
    else:
        severity, score = "MEDIUM", 45
    results.append((score, severity, rule, ip, count))

results.sort(reverse=True)

reduction = 100 - int(len(results) / len(alerts) * 100)
print(f"[+] After Deduplication: {len(results)} unique alerts")
print(f"[+] Reduction: {reduction}% noise removed\n")
print("TOP PRIORITY ALERTS:")
print("-"*55)
for score, severity, rule, ip, count in results:
    print(f"{severity:9} | Score: {score} | {rule:20} | {ip} | Count: {count}")

print("\n[+] Triage Complete. Analyst should investigate CRITICAL first.")
