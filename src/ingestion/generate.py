import subprocess
import sys

scripts = [
    "src/ingestion/customers_generate.py",
    "src/ingestion/merchants_generate.py",
    "src/ingestion/accounts_generate.py",
    "src/ingestion/cards_generate.py",
    "src/ingestion/devices_generate.py",
    "src/ingestion/transactions_generate.py",
    "src/ingestion/transaction_legs_generate.py",
    "src/ingestion/login_history_generate.py",
    "src/ingestion/alert_rules_generate.py",
    "src/ingestion/fraud_analysis_generate.py",
    "src/ingestion/fraud_alerts_generate.py",
    "src/ingestion/audit_logs_generate.py"
]

for script in scripts:
    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR in {script}:\n{result.stderr}")
        sys.exit(1)
    print(f"Done: {script}")

