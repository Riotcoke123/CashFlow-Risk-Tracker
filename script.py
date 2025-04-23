import json
import random
import matplotlib.pyplot as plt

REGISTER_START_CASH = 80
NUM_REGISTERS = 3
EARLY_DEPOSIT_THRESHOLD = 210
EARLY_DEPOSIT_RISK_FLAG = 150
ROBBERY_RISK_THRESHOLD = 250

BASE_SALES = {
    'Monday': 300,
    'Tuesday': 300,
    'Wednesday': 300,
    'Thursday': 360,
    'Friday': 500,
    'Saturday': 750,
    'Sunday': 400,
}

DAYS = list(BASE_SALES.keys())

def generate_fluctuated_sales(base_sales):
    return {day: round(sales * random.uniform(0.85, 1.15)) for day, sales in base_sales.items()}

def simulate_cash_flow_with_json_log(weeks=1, json_file="cash_flow_with_risk_log.json"):
    full_log = {
        "simulation_weeks": weeks,
        "weekly_logs": [],
        "totals": {
            "total_deposited": 0,
            "total_early": 0,
            "robbery_days": []
        }
    }

    for week_num in range(1, weeks + 1):
        register_cash = [REGISTER_START_CASH] * NUM_REGISTERS
        weekly_sales = generate_fluctuated_sales(BASE_SALES)
        week_log = {"week": week_num, "days": {}}
        week_total = 0
        week_early = 0

        for day in DAYS:
            day_log = {
                "sales": weekly_sales[day],
                "early_deposit": 0,
                "night_deposit": 0,
                "risk_flag": False,
                "robbery_risk": False
            }

            total_sales = weekly_sales[day]
            daily_early_deposit = 0
            daily_night_deposit = 0
            per_register_sales = total_sales / NUM_REGISTERS

            for i in range(NUM_REGISTERS):
                register_cash[i] += per_register_sales
                if register_cash[i] > EARLY_DEPOSIT_THRESHOLD:
                    excess = register_cash[i] - EARLY_DEPOSIT_THRESHOLD
                    daily_early_deposit += excess
                    register_cash[i] = EARLY_DEPOSIT_THRESHOLD

            if daily_early_deposit > EARLY_DEPOSIT_RISK_FLAG:
                day_log["risk_flag"] = True
            if daily_early_deposit > ROBBERY_RISK_THRESHOLD:
                day_log["robbery_risk"] = True
                full_log["totals"]["robbery_days"].append({"week": week_num, "day": day})

            for i in range(NUM_REGISTERS):
                excess = register_cash[i] - REGISTER_START_CASH
                daily_night_deposit += excess
                register_cash[i] = REGISTER_START_CASH

            day_log["early_deposit"] = round(daily_early_deposit, 2)
            day_log["night_deposit"] = round(daily_night_deposit, 2)
            week_log["days"][day] = day_log

            week_total += daily_early_deposit + daily_night_deposit
            week_early += daily_early_deposit

        week_log["week_total_deposited"] = round(week_total, 2)
        week_log["week_total_early"] = round(week_early, 2)
        full_log["weekly_logs"].append(week_log)
        full_log["totals"]["total_deposited"] += week_total
        full_log["totals"]["total_early"] += week_early

    full_log["totals"]["total_deposited"] = round(full_log["totals"]["total_deposited"], 2)
    full_log["totals"]["total_early"] = round(full_log["totals"]["total_early"], 2)

    with open(json_file, "w") as f:
        json.dump(full_log, f, indent=2)

    return full_log

def plot_robbery_trends(json_file="cash_flow_with_risk_log.json"):
    with open(json_file, "r") as f:
        data = json.load(f)

    robbery_days = data["totals"]["robbery_days"]
    weekly_robbery_count = {week: 0 for week in range(1, data["simulation_weeks"] + 1)}

    for robbery in robbery_days:
        week = robbery["week"]
        weekly_robbery_count[week] += 1

    weeks = list(weekly_robbery_count.keys())
    robbery_counts = list(weekly_robbery_count.values())

    plt.figure(figsize=(10, 6))
    plt.bar(weeks, robbery_counts, color="#f44336", alpha=0.7)
    plt.xlabel('Week Number')
    plt.ylabel('Robbery Risk Days Count')
    plt.title('Robbery Risk Days Per Week')
    plt.xticks(weeks)
    plt.tight_layout()
    plt.show()

def plot_early_deposit_trends(json_file="cash_flow_with_risk_log.json"):
    with open(json_file, "r") as f:
        data = json.load(f)

    weekly_early_deposits = {week: 0 for week in range(1, data["simulation_weeks"] + 1)}

    for week_num in range(1, data["simulation_weeks"] + 1):
        weekly_total_early = 0
        for day in DAYS:
            for week in data["weekly_logs"]:
                if week["week"] == week_num:
                    weekly_total_early += week["days"][day]["early_deposit"]
        weekly_early_deposits[week_num] = weekly_total_early

    weeks = list(weekly_early_deposits.keys())
    early_deposit_values = list(weekly_early_deposits.values())

    plt.figure(figsize=(10, 6))
    plt.plot(weeks, early_deposit_values, marker='o', color="#4caf50", linestyle='-', linewidth=2)
    plt.xlabel('Week Number')
    plt.ylabel('Total Early Deposits ($)')
    plt.title('Total Early Deposits Per Week')
    plt.xticks(weeks)
    plt.tight_layout()
    plt.show()

simulate_cash_flow_with_json_log(weeks=10)
plot_robbery_trends()
plot_early_deposit_trends()
