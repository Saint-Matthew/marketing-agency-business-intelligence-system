# Marketing Agency Business Intelligence System

An advanced business intelligence and analytics dashboard designed for Nigerian marketing agencies.

This platform combines data analytics, machine learning, predictive analytics, interactive visualizations, and campaign intelligence to help agencies monitor performance, analyze revenue trends, evaluate employee productivity, and predict campaign ROI.

The project also demonstrates containerized application deployment using Docker alongside cloud based Streamlit deployment workflows.

---

# Live Demo

Streamlit App:  
https://your-streamlit-link.streamlit.app/

---

# Dashboard Preview

## Executive Dashboard

![Dashboard](screenshots/dashboard.png)

## Campaign Analytics

![Analytics](screenshots/analytics.png)

---

# Project Overview

Marketing agencies manage multiple campaigns, clients, platforms, and teams simultaneously. Monitoring campaign performance manually becomes increasingly difficult as operations scale.

This project simulates a real-world business intelligence platform capable of:

- Monitoring campaign performance
- Tracking revenue growth
- Evaluating employee productivity
- Analyzing client industries
- Comparing advertising platforms
- Predicting campaign ROI using machine learning
- Delivering interactive executive business insights
- Supporting containerized deployment environments

The system was designed specifically around the operational structure of modern Nigerian marketing agencies.

---

# Separated Concerns and System Architecture

The project follows separated concerns architecture to improve scalability, maintainability, modularity, and enterprise software organization.

The system is divided into multiple independent layers, where each layer is responsible for a specific operational concern.

---

# Frontend Layer

Responsible for dashboard rendering, visualization, user interaction, and business intelligence presentation.

## Technologies
- Streamlit
- Plotly

## Responsibilities
- Interactive dashboards
- KPI visualization
- Dynamic filtering
- Business intelligence rendering
- Executive reporting interfaces
- User interaction workflows

## Frontend Components

```text
app.py
```

---

# Backend Layer

Responsible for business logic, workflow orchestration, enterprise processing, and analytics computation.

## Technologies
- Python
- Pandas
- NumPy
- SQLite

## Responsibilities
- Campaign analytics computation
- Data preprocessing
- Revenue analysis
- Productivity calculations
- Workflow management
- Database interaction
- Data transformation pipelines

## Backend Components

```text
main.py
database.py
generate_dataset.py
```

---

# Machine Learning Layer

Responsible for predictive analytics, campaign intelligence, and ROI prediction systems.

## Technologies
- Scikit-learn
- Linear Regression

## Capabilities
- Campaign ROI prediction
- Predictive business analytics
- Trend analysis
- Performance forecasting

## Machine Learning Techniques
- Linear Regression
- Label Encoding
- Train/Test Split Validation
- R² Accuracy Evaluation

---

# Data Layer

Responsible for enterprise dataset management and structured business records.

## Datasets
- Campaign performance
- Client analytics
- Employee productivity
- Revenue intelligence

## Dataset Structure

```text
datasets/
├── campaigns.csv
├── clients.csv
├── employees.csv
└── revenue.csv
```

---

# Infrastructure and Deployment Layer

Responsible for deployment workflows, repository management, cloud accessibility, and containerized infrastructure.

## Technologies
- Docker
- Git
- GitHub
- Streamlit Cloud

## Responsibilities
- Containerized deployment
- Cloud deployment
- Version control management
- Repository workflows
- Portable runtime environments
- Infrastructure scalability

---

# Key Features

## Executive Dashboard
- KPI summary metrics
- Revenue monitoring
- Productivity tracking
- Campaign performance overview
- Growth indicators

## Campaign Analytics
- ROI analysis by platform
- Engagement performance visualization
- Platform ranking tables
- Campaign performance comparisons

## Revenue Intelligence
- Monthly revenue growth analysis
- Profit trend visualization
- Business growth monitoring

## Team Performance Analytics
- Employee productivity analysis
- Task completion tracking
- Team performance visualization

## Machine Learning Prediction Engine
Predict expected campaign ROI using:
- Campaign budget
- Impressions
- Clicks
- Engagement rate
- Advertising platform

## Interactive Business Intelligence
- Dynamic filtering
- Interactive visualizations
- Executive reporting dashboards
- Business analytics rendering

## Downloadable Reports
- Export campaign analytics reports as CSV files

---

# Machine Learning Model

The project uses:

- Linear Regression
- Label Encoding
- Train/Test Split Validation
- R² Accuracy Evaluation

The model predicts campaign ROI using historical campaign performance data.

---

# Tech Stack

- Python
- Streamlit
- SQLite
- Pandas
- Plotly
- Scikit-learn
- NumPy
- Docker
- Git
- GitHub
- Streamlit Cloud

---

# Project Structure

```text
marketing-agency-business-intelligence-system/
│
├── assets/
│
├── datasets/
│   ├── campaigns.csv
│   ├── clients.csv
│   ├── employees.csv
│   └── revenue.csv
│
├── screenshots/
│   ├── dashboard.png
│   └── analytics.png
│
├── agency_data.db
├── app.py
├── database.py
├── generate_dataset.py
├── main.py
├── Dockerfile
├── .dockerignore
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Run Project Locally

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Start the Dashboard

```bash
streamlit run app.py
```

---

# Run with Docker

## 1. Build Docker Image

```bash
docker build -t marketing-dashboard .
```

## 2. Run Docker Container

```bash
docker run -p 8501:8501 marketing-dashboard
```

## 3. Open in Browser

```text
http://localhost:8501
```

---

# Dashboard Modules

## Overview
- Industry distribution analysis
- Top client budget insights
- Client ranking tables

## Campaign Analytics
- Platform ROI comparisons
- Engagement analytics
- Campaign performance ranking

## Revenue Intelligence
- Revenue growth tracking
- Profit analysis
- Business trend insights

## Team Performance
- Productivity analytics
- Team efficiency visualization
- Employee workload analysis

---

# AI Business Insights

The system automatically identifies:
- Highest performing advertising platforms
- Highest budget client industries
- Campaign performance trends
- ROI prediction insights

---

# Sample Use Cases

This platform can be adapted for:
- Marketing agencies
- Digital media firms
- Advertising consultancies
- Social media agencies
- Growth marketing startups
- Business intelligence demonstrations

---

# Future Improvements

Planned future upgrades include:

- Real-time API integrations
- Client authentication system
- Automated PDF reports
- AI recommendation engine
- Forecasting dashboards
- Real-time campaign monitoring
- PostgreSQL integration
- Cloud deployment optimization
- Kubernetes deployment workflows
- Enterprise infrastructure scaling

---

# Project Goal

The objective of this project is to demonstrate:
- Business intelligence engineering
- Interactive analytics systems
- Machine learning applications
- Predictive analytics
- Dashboard engineering
- Data visualization
- Enterprise deployment workflows
- Containerized infrastructure engineering

---

# Author

Matthew Obayemi

Computer Science Student  
University of the People

---

# License

This project demonstrates the practical application of machine learning, predictive analytics, business intelligence engineering, interactive dashboard systems, and containerized deployment workflows in solving real-world marketing agency reporting and analytics challenges.

