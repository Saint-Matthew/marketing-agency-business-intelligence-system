import pandas as pd
import random

# ----------------------------
# CLIENT DATASET
# ----------------------------

companies = [
    "Zinox Media",
    "Flutter Campaigns",
    "Lagos Fashion House",
    "Naija Travels",
    "TechNova Africa",
    "Food Arena NG",
    "Glow Beauty",
    "Prime Realtors",
    "AfroBeats Hub",
    "Luxury Wears NG"
]

industries = [
    "Fashion",
    "Fintech",
    "Travel",
    "Real Estate",
    "Hospitality",
    "Beauty",
    "Technology",
    "Entertainment",
    "Food"
]

campaign_types = [
    "Social Media",
    "Influencer Marketing",
    "SEO",
    "Google Ads",
    "Brand Awareness",
    "Product Launch"
]

client_rows = []

for i in range(100):

    client_rows.append({
        "client_name": random.choice(companies),
        "industry": random.choice(industries),
        "campaign_type": random.choice(campaign_types),
        "monthly_budget_naira": random.randint(500000, 10000000),
        "status": random.choice(["Active", "Paused", "Completed"])
    })

clients_df = pd.DataFrame(client_rows)

clients_df.to_csv(
    "datasets/clients.csv",
    index=False
)

# ----------------------------
# CAMPAIGNS DATASET
# ----------------------------

platforms = [
    "Instagram",
    "TikTok",
    "Facebook",
    "Twitter/X",
    "Google Ads"
]

campaign_rows = []

for i in range(200):

    impressions = random.randint(10000, 500000)
    clicks = random.randint(1000, 50000)

    campaign_rows.append({
        "platform": random.choice(platforms),
        "impressions": impressions,
        "clicks": clicks,
        "conversions": random.randint(50, 5000),
        "engagement_rate": round(random.uniform(1.5, 15.0), 2),
        "roi_percentage": round(random.uniform(10, 300), 2)
    })

campaigns_df = pd.DataFrame(campaign_rows)

campaigns_df.to_csv(
    "datasets/campaigns.csv",
    index=False
)

# ----------------------------
# REVENUE DATASET
# ----------------------------

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

revenue_rows = []

for month in months:

    revenue = random.randint(5000000, 50000000)
    expenses = random.randint(1000000, 20000000)

    revenue_rows.append({
        "month": month,
        "revenue_naira": revenue,
        "expenses_naira": expenses,
        "profit_naira": revenue - expenses
    })

revenue_df = pd.DataFrame(revenue_rows)

revenue_df.to_csv(
    "datasets/revenue.csv",
    index=False
)

# ----------------------------
# EMPLOYEE DATASET
# ----------------------------

roles = [
    "Graphic Designer",
    "Video Editor",
    "Content Strategist",
    "Social Media Manager",
    "Marketing Analyst",
    "Account Manager"
]

employee_rows = []

for i in range(50):

    employee_rows.append({
        "employee_id": i + 1,
        "role": random.choice(roles),
        "tasks_completed": random.randint(10, 200),
        "productivity_score": round(random.uniform(50, 100), 2),
        "assigned_campaigns": random.randint(1, 20)
    })

employees_df = pd.DataFrame(employee_rows)

employees_df.to_csv(
    "datasets/employees.csv",
    index=False
)

print("Marketing agency datasets generated successfully.")

