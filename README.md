# MLOps SQL Project 🚀

## Overview

This repository provides a structured MLOps project that integrates **SQL, Python, Tableau, and MLOps automation**. The project includes structured SQL queries, Tableau dashboards for data visualization, and Python scripts for automation and data generation.

## Project Structure 📂

mlops_sql_project/ ├── env/ # Environment Configuration ├── Excel/ │ ├── transactions_overview.xlsx │ ├── sales_summary.xlsx
│ ├── customer_behavior.xlsx # Excel-based Analysis ├── Tableau/ # Tableau Dashboards & Reports │ ├── sales_dashboard.twb │ ├── transaction_analysis.twb │ ├── customer_insights.twb │ ├── python/ # Data Generation & Automation │ ├── generate_customers.py # Generates random customer data │ ├── generate_orders.py # Generates random orders │ ├── generate_products.py # Generates product catalog │ ├── generate_transactions.py # Simulates transaction history │ ├── transactions_overview.py
│ ├── sales_summary.py
│ ├── customer_behavior.py
├── sql/ # Structured SQL Queries │ ├── ddl/ # Schema definition (Create, Constraints) │ │ ├── 01_create_database.sql │ │ ├── 02_create_tables.sql │ │ ├── 03_constraints.sql │ │ │ ├── dml/ # Data Manipulation (Insert, Update, Delete) │ │ ├── 00_truncate_tables.sql │ │ │ ├── dql/ # Queries & Analysis │ │ ├── a_checks/ # Data Validation & Structure │ │ │ ├── 01_check_constraints.sql │ │ │ ├── 02_check_all_foreign_keys.sql │ │ │ ├── 03_check_table_dependencies.sql │ │ │ ├── 04_check_indexes_primary_keys.sql │ │ │ ├── 05_check_privileges.sql │ │ │ │ │ ├── b_aggregations/ # Aggregation & Statistical Analysis │ │ │ ├── 06_table_counts.sql │ │ │ ├── 07_check_total_records.sql │ │ │ ├── 08_counts_the_number_of_products.sql │ │ │ ├── 09_min_max_and_average_price.sql │ │ │ ├── 10_stock_statistics.sql │ │ │ │ │ ├── c_transactions/ # Orders & Transactions │ │ │ ├── 11_top_expensive_orders.sql │ │ │ ├── 12_orders_by_month.sql │ │ │ ├── 13_random_orders_check.sql │ │ │ ├── 14_customers_orders_join.sql │ │ │ ├── 15_transaction_amount_summary.sql │ │ │ ├── 16_transactions_by_payment.sql │ │ │ ├── 17_daily_transaction_volume.sql │ │ │ ├── 18_top_10_biggest_transactions.sql │ │ │ ├── 19_top_10_biggest_customers.sql │ │ │ │ │ ├── d_joins/ # Multi-table Joins & Relationships │ │ │ ├── 20_join_customers_orders_products.sql # Customers x Orders x Products │ │ │ ├── 21_join_orders_transactions.sql # Orders x Transactions │ │ │ ├── 22_top_10_customers_by_spent.sql → Retrieves the top 10 customers based on total transaction amount. │ │ │ ├── 23_avg_order_value.sql → Calculates the average order value per customer. │ │ │ ├── 24_returning_customers.sql → Identifies returning customers (more than 1 order). │ │ │ ├── 25_bonus.sql → Executes a special bonus query for additional insights. │ │ │ ├── 26_cleaned_bonus.sql → Refines 25_bonus.sql by replacing NULL values with meaningful defaults. │ ├── environment.yaml # Conda environment setup ├── README.md # Project Documentation

markdown
Copy
Edit

---

## 🚀 Features

- **Structured SQL Queries**: Includes `DDL`, `DML`, and `DQL` for **data creation, manipulation, and querying**.
- **MLOps & Automation**: Uses Python scripts for **data generation** and **processing**.
- **Tableau Dashboards**: Interactive dashboards for **transaction analysis** and **customer insights**.
- **CI/CD Integration** (Planned): Future implementation of **GitHub Actions** for automation.

---

## 🛠 Tech Stack

- **SQL (PostgreSQL)** – Database & Queries  
- **Python** – Automation & Data Processing  
- **Tableau** – Dashboards & Reports  
- **MLOps Tools** (Planned) – **MLflow, Weights & Biases (W&B)**  
- **GitHub Actions** – CI/CD (Planned)  

---

## 🔥 Getting Started

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/evgeniimatveev/mlops_sql_project.git
cd mlops_sql_project
2️⃣ Set Up Environment (Optional)
sh
Copy
Edit
conda env create -f environment.yaml
conda activate mlops_env
3️⃣ Run SQL Queries
Queries are stored in /sql/dql/. Execute them using PostgreSQL:

sql
Copy
Edit
-- Example: Retrieve Top 10 Customers by Spending
SELECT * FROM top_10_customers_by_spent;
4️⃣ Open Tableau Dashboards
Navigate to the Tableau/ folder.
Open .twb files in Tableau Desktop.
🔄 Future Plans
✔️ Complete SQL Queries & Analysis
✔️ Add Tableau Dashboards
✔️ Automate Data Generation (Python)
🛠 Implement MLflow for Experiment Tracking
🛠 Set up CI/CD (GitHub Actions) for Deployment

📌 Contributing
Feel free to fork the repo, create a pull request, or suggest improvements. 🚀

📜 License
This project is open-source and licensed under MIT License.

🔥 Developed by evgeniimatveev

🚀 MLOps + SQL + Tableau = Power 🚀
