import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

from main import (
    predict_roi,
    accuracy
)

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Marketing Agency Business Intelligence System",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    div.block-container {
        padding-top: 1.5rem;
    }

    [data-testid="stSidebar"] {
        width: 260px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# DATABASE CONNECTION
# -----------------------------------

connection = sqlite3.connect(
    "agency_data.db"
)

clients_df = pd.read_sql(
    "SELECT * FROM clients",
    connection
)

campaigns_df = pd.read_sql(
    "SELECT * FROM campaigns",
    connection
)

revenue_df = pd.read_sql(
    "SELECT * FROM revenue",
    connection
)

employees_df = pd.read_sql(
    "SELECT * FROM employees",
    connection
)

# -----------------------------------
# SIDEBAR FILTERS
# -----------------------------------

st.sidebar.title("Dashboard Filters")

selected_industry = st.sidebar.multiselect(
    "Select Industry",
    clients_df["industry"].unique()
)

selected_platform = st.sidebar.multiselect(
    "Select Platform",
    campaigns_df["platform"].unique()
)

selected_role = st.sidebar.multiselect(
    "Select Employee Role",
    employees_df["role"].unique()
)

# -----------------------------------
# DEFAULT FILTERS
# -----------------------------------

if not selected_industry:
    selected_industry = (
        clients_df["industry"].unique()
    )

if not selected_platform:
    selected_platform = (
        campaigns_df["platform"].unique()
    )

if not selected_role:
    selected_role = (
        employees_df["role"].unique()
    )

# -----------------------------------
# FILTER DATA
# -----------------------------------

filtered_clients = clients_df[
    clients_df["industry"].isin(
        selected_industry
    )
]

filtered_campaigns = campaigns_df[
    campaigns_df["platform"].isin(
        selected_platform
    )
]

filtered_employees = employees_df[
    employees_df["role"].isin(
        selected_role
    )
]

# -----------------------------------
# HEADER
# -----------------------------------

st.title(
    "Marketing Agency Business Intelligence System"
)

st.write(
    """
    Advanced business intelligence and analytics
    dashboard for Nigerian marketing agencies.
    """
)

# -----------------------------------
# EXECUTIVE SUMMARY
# -----------------------------------

st.subheader("Executive Summary")

top_platform = (
    filtered_campaigns.groupby("platform")[
        "roi_percentage"
    ].mean().idxmax()
)

top_industry = (
    filtered_clients.groupby("industry")[
        "monthly_budget_naira"
    ].mean().idxmax()
)

st.info(
    f"""
    Highest Performing Platform: {top_platform}

    Highest Budget Industry: {top_industry}

    Machine Learning ROI Accuracy:
    {accuracy * 100:.1f}%
    """
)

# -----------------------------------
# KPI METRICS
# -----------------------------------

total_clients = len(filtered_clients)

total_campaigns = len(filtered_campaigns)

total_revenue = revenue_df[
    "revenue_naira"
].sum()

avg_productivity = (
    filtered_employees[
        "productivity_score"
    ].mean()
)

monthly_growth = (
    revenue_df[
        "revenue_naira"
    ].pct_change().mean() * 100
)

col1, col2, col3, col4, col5 = (
    st.columns(5)
)

col1.metric(
    "Clients",
    total_clients,
    delta="+8%"
)

col2.metric(
    "Campaigns",
    total_campaigns,
    delta="+14%"
)

col3.metric(
    "Revenue",
    f"₦{total_revenue:,.0f}",
    delta="+18%"
)

col4.metric(
    "Productivity",
    f"{avg_productivity:.1f}%",
    delta="+5%"
)

col5.metric(
    "Growth",
    f"{monthly_growth:.1f}%",
    delta="+3%"
)

st.divider()

# -----------------------------------
# TABS
# -----------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "Overview",
    "Campaign Analytics",
    "Revenue Intelligence",
    "Team Performance"
])

# -----------------------------------
# OVERVIEW TAB
# -----------------------------------

with tab1:

    col1, col2 = st.columns(2)

    with col1:

        industry_chart = px.pie(
            filtered_clients,
            names="industry",
            title="Client Industry Distribution"
        )

        industry_chart.update_layout(
            height=450
        )

        st.plotly_chart(
            industry_chart,
            use_container_width=True
        )

    with col2:

        top_clients = (
            filtered_clients.sort_values(
                by="monthly_budget_naira",
                ascending=False
            ).head(10)
        )

        budget_chart = px.bar(
            top_clients,
            x="client_name",
            y="monthly_budget_naira",
            color="industry",
            title="Top Client Budgets"
        )

        budget_chart.update_layout(
            height=450
        )

        st.plotly_chart(
            budget_chart,
            use_container_width=True
        )

    st.subheader(
        "Top Performing Clients"
    )

    st.dataframe(
        top_clients[
            [
                "client_name",
                "industry",
                "monthly_budget_naira"
            ]
        ],
        use_container_width=True
    )

# -----------------------------------
# CAMPAIGN ANALYTICS TAB
# -----------------------------------

with tab2:

    col1, col2 = st.columns(2)

    with col1:

        roi_chart = px.bar(
            filtered_campaigns,
            x="platform",
            y="roi_percentage",
            color="platform",
            title="ROI by Platform"
        )

        roi_chart.update_layout(
            height=450
        )

        st.plotly_chart(
            roi_chart,
            use_container_width=True
        )

    with col2:

        engagement_chart = px.scatter(
            filtered_campaigns,
            x="impressions",
            y="clicks",
            size="engagement_rate",
            color="platform",
            title="Campaign Engagement"
        )

        engagement_chart.update_layout(
            height=450
        )

        st.plotly_chart(
            engagement_chart,
            use_container_width=True
        )

    st.subheader(
        "Platform Performance Ranking"
    )

    platform_summary = (
        filtered_campaigns.groupby(
            "platform"
        )["roi_percentage"]
        .mean()
        .reset_index()
        .sort_values(
            by="roi_percentage",
            ascending=False
        )
    )

    st.dataframe(
        platform_summary,
        use_container_width=True
    )

# -----------------------------------
# REVENUE TAB
# -----------------------------------

with tab3:

    revenue_chart = px.line(
        revenue_df,
        x="month",
        y="revenue_naira",
        markers=True,
        title="Monthly Revenue Growth"
    )

    revenue_chart.update_layout(
        height=500
    )

    st.plotly_chart(
        revenue_chart,
        use_container_width=True
    )

    profit_chart = px.bar(
        revenue_df,
        x="month",
        y="profit_naira",
        color="profit_naira",
        title="Monthly Profit Analysis"
    )

    profit_chart.update_layout(
        height=500
    )

    st.plotly_chart(
        profit_chart,
        use_container_width=True
    )

# -----------------------------------
# TEAM PERFORMANCE TAB
# -----------------------------------

with tab4:

    productivity_chart = px.bar(
        filtered_employees,
        x="role",
        y="productivity_score",
        color="role",
        title="Employee Productivity"
    )

    productivity_chart.update_layout(
        height=500
    )

    st.plotly_chart(
        productivity_chart,
        use_container_width=True
    )

    performance_chart = px.scatter(
        filtered_employees,
        x="tasks_completed",
        y="assigned_campaigns",
        size="productivity_score",
        color="role",
        title="Team Performance Analysis"
    )

    performance_chart.update_layout(
        height=500
    )

    st.plotly_chart(
        performance_chart,
        use_container_width=True
    )

# -----------------------------------
# MACHINE LEARNING ENGINE
# -----------------------------------

st.divider()

st.header(
    "AI Campaign Prediction Engine"
)

st.write(
    """
    Predict expected campaign ROI
    using machine learning.
    """
)

col1, col2 = st.columns(2)

with col1:

    budget = st.number_input(
        "Campaign Budget (₦)",
        min_value=100000,
        value=5000000
    )

    impressions = st.number_input(
        "Expected Impressions",
        min_value=1000,
        value=500000
    )

    clicks = st.number_input(
        "Expected Clicks",
        min_value=100,
        value=25000
    )

with col2:

    engagement_rate = st.slider(
        "Engagement Rate (%)",
        1,
        100,
        25
    )

    platform = st.selectbox(
        "Platform",
        campaigns_df["platform"].unique()
    )

st.metric(
    "Model Accuracy",
    f"{accuracy * 100:.1f}%"
)

if st.button(
    "Predict Campaign ROI"
):

    prediction = predict_roi(
        budget,
        impressions,
        clicks,
        engagement_rate,
        platform
    )

    st.success(
        f"Predicted ROI: {prediction:.2f}%"
    )

    if prediction >= 50:

        st.info(
            """
            This campaign is projected
            to perform strongly.
            """
        )

    elif prediction >= 30:

        st.warning(
            """
            This campaign has moderate
            growth potential.
            """
        )

    else:

        st.error(
            """
            Predicted ROI is relatively low.
            """
        )

    st.success(
        """
        AI Insight:

        Campaigns with stronger
        engagement rates and higher
        click-through activity tend
        to generate better ROI.
        """
    )

# -----------------------------------
# DOWNLOAD REPORT
# -----------------------------------

st.divider()

st.subheader(
    "Download Analytics Reports"
)

csv = (
    filtered_campaigns.to_csv(
        index=False
    ).encode("utf-8")
)

st.download_button(
    label="Download Campaign Report",
    data=csv,
    file_name="campaign_report.csv",
    mime="text/csv"
)

# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.caption(
    """
    Built with Streamlit, SQLite,
    Plotly, Pandas, and Scikit-learn
    """
)

