# Financial Intelligence & Fraud Analytics Platform (FIFAP)
A full end-to-end banking analytics platform that detects fraud, scores  risk, and turns raw transaction data into decisions, built from scratch  using Python, PostgreSQL, and Power BI.


## What Is This?

FIFAP is a portfolio project that simulates how a real bank detects fraud
and monitors financial activity.

It covers everything from generating realistic banking data, storing it in
a properly designed database, running fraud detection rules, scoring customer
risk, and presenting the results in a dashboard, the same workflow used by
real fraud and analytics teams in financial institutions.

No real customer data is used. All data is synthetically generated using
Python to closely mirror real banking behavior.


## The Problem It Solves

Banks process thousands of transactions every minute. No human team can
manually review all of them for fraud. The only way to catch suspicious
activity at scale is through automated pattern detection and intelligent
risk scoring.

FIFAP simulates exactly that a system that watches every transaction,
compares it against known fraud patterns, assigns a risk score, and raises
an alert when something looks wrong.


## What I Built

  - **A realistic banking database** with 12 interconnected tables designed
    to mirror how real banks store customer and transaction data.

  - **A synthetic dataset generator** using Python and Faker that produces
    50,000 realistic transactions with genuine spending patterns, timestamps,
    and customer behavior not random noise.

  - **A rule-based fraud detection engine** with 8 fraud rules that score
    every transaction and classify it as Low, Medium, High, or Critical risk.

  - **SQL analytics** covering transaction KPIs, customer segmentation,
    merchant performance, and fraud trend reporting.

  - **A Power BI dashboard** that gives fraud analysts and business managers
    a clear view of what is happening across the platform.


## Tech Stack

    - Python
    - PostgreSQL
    - SQLAlchemy
    - Psycopg2 
    - Pandas 
    - NumPy 
    - Faker 
    - Jupyter Notebook 
    - Power BI 
    - Git & GitHub


## Database Design

| Table | What It Stores                                            |
|-------|-----------------------------------------------------------|
| customers | Customer profiles and assigned risk tier                  |
| accounts | Bank accounts linked to each customer                     |
| cards | Debit and credit cards linked to accounts                 |
| devices | Devices customers use, flagged if unrecognized            |
| merchants | Businesses receiving payments, tagged by risk level       |
| transactions | Every financial event (the core of the entire system )    |
| transaction_legs | Both sides of every transfer (debit and credit)           |
| fraud_analysis | Fraud score and risk level assigned to each transaction   |
| fraud_alerts | Alerts raised when a transaction crosses a risk threshold |
| alert_rules | The 8 configurable rules that power the fraud engine      |
| login_history | Customer login events used for security pattern analysis  |
| audit_logs | A full record of every change made in the system          |


## The Dataset

Built with Python, Faker, and NumPy.

| Table | Records |
|-------|---------|
| Customers | 500 |
| Accounts | 750 |
| Cards | 580 |
| Devices | 900 |
| Merchants | 100 |
| Transactions | 50,000 |
| Transaction legs | 100,000 |
| Fraud analysis records | 50,000 |
| Fraud alerts | 1,000 |
| Login history | 8,000 |
| Audit logs | 2,000 |

**How the data looks realistic:**
  - Most transactions are small amounts with occasional large ones,
  the same pattern seen in real spending data.
  - Timestamps are weighted toward business hours with realistic
    weekend and late-night patterns.
  - Customers return to the same merchants regularly, just like
    real people do.
  - Every customer has their own normal spending range, making
    unusual activity easy to detect.

**Fraud injection rate:** around 2% of all transactions contain
deliberately planted fraud patterns for the detection engine to find.


## Fraud Detection Engine

Every transaction is scored against 8 rules. Rules can stack —
one transaction can trigger multiple rules and accumulate a high score.

| Rule | What Triggers It                                                | Score |
|------|-----------------------------------------------------------------|-------|
| Rapid transaction burst | More than 5 transactions in 60 minutes                          | +40 |
| Abnormally high amount | Purchase is more than 3 times what the customer normally spends | +35 |
| Rapid consecutive transfers | More than 3 transfers in 10 minutes                             | +30 |
| Unrecognized device | Customer pays using a device they have never used before5       | +30 |
| Multiple failed logins | More than 3 failed logins in 30 minutes                         | +25 |
| Unusual transaction location | More than 500km from last known location                        | +25 |
| Middle-of-the-night transaction | Transaction happens between 12AM and 5AM with no history of night spending        | +20 |
| High-risk merchant | Merchant is in a high-risk category                             | +20 |

**What the score means:**

| Score | Risk Level | What Happens |
|-------|------------|--------------|
| 0–20 | Low | No action taken |
| 21–49 | Medium | Transaction flagged for review |
| 50–79 | High | Fraud alert generated |
| 80+ | Critical | Transaction blocked + immediate alert |

## What I Plan To Add Next

- Machine learning fraud detection.
- Real-time transaction monitoring with a streaming pipeline.
- A REST API that serves fraud scores to external systems.
- Automated alert notifications by email or SMS.
- Deeper dashboard views for customer-level fraud investigation.

---

## Author

**Clarise C. Tan**
Aspiring Data Analyst

- A 2nd Year College Computer Science Student
---

*This project demonstrates end-to-end data skills across database design,
data engineering, fraud analytics, SQL development, and business
intelligence reporting.*
