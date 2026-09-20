# Retail Sales Analytics Dashboard

An end-to-end **Data Science / Data Analytics portfolio project** built using a Superstore-style retail transaction dataset. The project covers data cleaning, exploratory data analysis (EDA), SQL analysis, statistical analysis, and an interactive Streamlit dashboard.

> **Current status:** The analytical workflow and dashboard foundation are built. Machine-learning forecasting and deployment are planned as the next phases.

## 1. Project Overview

Retail businesses generate large amounts of transaction data. This project transforms raw transaction records into business insights through a complete analytics workflow.

### Questions addressed

- How are sales changing over time?
- Which months and quarters generate the most sales?
- Which regions contribute the most sales?
- Which product categories and sub-categories perform best?
- Which customer segment contributes the most sales?
- Which products generate the highest sales?
- Which shipping modes are most frequently used?
- What is the average shipping duration?
- Are observed differences between regions or customer segments statistically significant?

The final application presents these insights through an interactive Streamlit dashboard.

---

## 2. Objectives

### Primary objectives

1. Clean and prepare the raw retail transaction dataset.
2. Perform exploratory data analysis.
3. Identify sales trends and seasonal patterns.
4. Analyze regional, category, sub-category, product, and customer-segment performance.
5. Build a SQLite database for SQL analysis.
6. Perform statistical hypothesis testing.
7. Build an interactive Streamlit dashboard.
8. Prepare the project for a future sales-forecasting ML component.

### Future objective

Extend the project with machine-learning-based sales forecasting and integrate predictions into the dashboard.

---

# 3. Dataset

The project uses a Superstore-style retail transaction dataset.

### Dataset profile

| Property | Value |
|---|---:|
| Rows | 9,800 |
| Columns | 18 |
| Duplicate rows | 0 |
| Missing values | 11 |
| Unique customers | 793 |
| Unique orders | 4,922 |
| Unique products | 1,861 |
| Categories | 3 |
| Sub-categories | 17 |
| Regions | 4 |
| Ship modes | 4 |
| Time period | 2015–2018 |

### Columns

| Column | Description |
|---|---|
| `Row ID` | Row identifier |
| `Order ID` | Order identifier |
| `Order Date` | Date the order was placed |
| `Ship Date` | Date the order was shipped |
| `Ship Mode` | Shipping method |
| `Customer ID` | Customer identifier |
| `Customer Name` | Customer name |
| `Segment` | Customer segment |
| `Country` | Country |
| `City` | City |
| `State` | State |
| `Postal Code` | Postal code |
| `Region` | Sales region |
| `Product ID` | Product identifier |
| `Category` | Product category |
| `Sub-Category` | Product sub-category |
| `Product Name` | Product name |
| `Sales` | Sales amount |

### Dataset limitation

The dataset does **not** contain `Profit`, `Quantity`, or `Discount`.

Therefore, the project does not invent unsupported metrics such as profit margin, profit by region, discount impact, or revenue per unit. The analysis focuses on the variables actually present in the dataset.

---

# 4. Project Architecture

```text
retail-sales-dashboard/
│
├── app/
│   └── dashboard.py
│
├── data/
│   ├── raw/
│   │   └── train.csv
│   ├── processed/
│   │   └── retail_cleaned.csv
│   └── retail_sales.db
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_statistical_analysis.ipynb
│
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
│
├── src/
│   └── data_pipeline.py
│
├── reports/
│   └── figures/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## End-to-end workflow

```text
Raw CSV
   ↓
Data Cleaning & Feature Engineering
   ↓
Clean Dataset
   ↓
Exploratory Data Analysis
   ↓
SQLite Database
   ↓
SQL Business Analysis
   ↓
Statistical Analysis
   ↓
Streamlit Dashboard
   ↓
Future: ML Sales Forecasting
   ↓
Future: Deployment
```

---

# 5. Data Cleaning

Notebook:

```text
notebooks/01_data_cleaning.ipynb
```

## 5.1 Initial inspection

The raw dataset was inspected using:

```python
df.shape
df.head()
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
```

The dataset contains 9,800 rows and 18 columns.

There are no duplicate rows.

---

## 5.2 Date conversion

The raw date columns were converted from strings into datetime objects:

```python
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    dayfirst=True
)
```

This makes time-based analysis possible.

---

## 5.3 Time-based feature engineering

The following features were created:

```python
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month_Name"] = df["Order Date"].dt.month_name()
df["Quarter"] = df["Order Date"].dt.quarter
df["Year_Month"] = df["Order Date"].dt.to_period("M")
```

Additional features:

```python
df["Day"] = df["Order Date"].dt.day
df["Day_of_Week"] = df["Order Date"].dt.day_name()
```

These support yearly, monthly, quarterly, and seasonal analysis.

---

## 5.4 Shipping duration

Shipping duration was calculated as:

```python
df["Shipping_Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days
```

This enables analysis of shipping performance.

---

## 5.5 Text cleaning

Categorical/text fields were stripped of leading and trailing whitespace:

```python
for col in text_columns:
    df[col] = df[col].str.strip()
```

This prevents values such as `"Technology"` and `" Technology "` from being treated as different categories.

---

## 5.6 Postal-code handling

Postal codes were converted to a nullable integer type:

```python
df["Postal Code"] = df["Postal Code"].astype("Int64")
```

There are 11 missing postal-code values. These rows are retained because the missing postal code does not invalidate the transaction.

---

## 5.7 Cleaned dataset

The cleaned dataset is saved to:

```text
data/processed/retail_cleaned.csv
```

---

# 6. Exploratory Data Analysis

Notebook:

```text
notebooks/02_eda.ipynb
```

The EDA phase examines the main business dimensions of the dataset.

## 6.1 KPIs

Calculated metrics include:

```python
total_sales = df["Sales"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_products = df["Product ID"].nunique()
average_order_value = total_sales / total_orders
```

Approximate dataset-level values:

| KPI | Value |
|---|---:|
| Total Sales | $2.26M |
| Total Orders | 4,922 |
| Customers | 793 |
| Products | 1,861 |
| Average Order Value | ~$459 |

---

## 6.2 Yearly sales

Approximate totals:

| Year | Sales |
|---|---:|
| 2015 | $479,856 |
| 2016 | $459,436 |
| 2017 | $600,193 |
| 2018 | $722,052 |

The data shows a small decline from 2015 to 2016 followed by strong growth in 2017 and 2018.

---

## 6.3 Monthly sales

Approximate totals:

| Month | Sales |
|---|---:|
| January | $94K |
| February | $59K |
| March | $198K |
| April | $136K |
| May | $154K |
| June | $146K |
| July | $146K |
| August | $157K |
| September | $300K |
| October | $199K |
| November | $350K |
| December | $321K |

November has the highest total monthly sales, while February has the lowest.

Monthly sales are also compared year by year to investigate whether seasonal patterns repeat.

---

## 6.4 Quarterly sales

Approximate totals:

| Quarter | Sales |
|---|---:|
| Q1 | $351K |
| Q2 | $436K |
| Q3 | $603K |
| Q4 | $871K |

Q4 is the strongest quarter.

---

## 6.5 Regional sales

Approximate totals:

| Region | Sales |
|---|---:|
| West | $710,220 |
| East | $669,519 |
| Central | $492,647 |
| South | $389,151 |

Regional performance is visualized and later tested statistically.

---

## 6.6 Category sales

Approximate totals:

| Category | Sales |
|---|---:|
| Technology | $827,456 |
| Furniture | $728,659 |
| Office Supplies | $705,422 |

Technology has the highest total sales among the three categories.

---

## 6.7 Sub-category sales

The dataset contains 17 sub-categories.

Leading sub-categories include:

| Rank | Sub-category | Approx. Sales |
|---:|---|---:|
| 1 | Phones | $327,782 |
| 2 | Chairs | $322,823 |
| 3 | Storage | $219,343 |
| 4 | Tables | $202,811 |
| 5 | Binders | $200,029 |

---

## 6.8 Top products

Products are aggregated by total sales and sorted in descending order.

The highest-selling product identified so far is:

```text
Canon imageCLASS 2200 Advanced Copier
```

with approximately $61,600 in sales.

The dashboard displays the top 10 products.

---

## 6.9 Customer segments

Approximate sales:

| Segment | Sales |
|---|---:|
| Consumer | $1.148M |
| Corporate | $688K |
| Home Office | $425K |

Consumer is the largest segment by sales.

---

## 6.10 Shipping analysis

Shipping is analyzed using:

- Order count
- Total sales
- Average shipping duration

Approximate order counts:

| Ship Mode | Orders | Avg. Shipping Days |
|---|---:|---:|
| Standard Class | 2,945 | 5.01 |
| Second Class | 944 | 3.25 |
| First Class | 772 | 2.18 |
| Same Day | 261 | ~0 |

Standard Class is the most commonly used shipping mode.

---

# 7. SQLite Database

Database:

```text
data/retail_sales.db
```

SQLite is used to demonstrate relational database and SQL skills without requiring a separate database server.

The main table is:

```text
sales
```

## Schema

The table contains the original fields plus engineered fields:

```text
row_id
order_id
order_date
ship_date
ship_mode
customer_id
customer_name
segment
country
city
state
postal_code
region
product_id
category
sub_category
product_name
sales
year
month
month_name
quarter
year_month
shipping_days
```

---

# 8. SQL Business Analysis

File:

```text
sql/analysis_queries.sql
```

The SQL analysis covers:

1. Total sales
2. Total orders
3. Total customers
4. Total products
5. Average order value
6. Sales by year
7. Sales by month
8. Sales by quarter
9. Sales by region
10. Sales by category
11. Sales by sub-category
12. Top 10 products
13. Customer segment analysis
14. Shipping mode analysis
15. Region and category analysis
16. Monthly sales by year
17. Year-over-year growth
18. SQL views

### Example

```sql
SELECT
    region,
    SUM(sales) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;
```

### Year-over-year growth

The project uses SQL CTEs and the `LAG()` window function:

```sql
WITH yearly_sales AS (
    SELECT
        year,
        SUM(sales) AS total_sales
    FROM sales
    GROUP BY year
),
sales_with_previous AS (
    SELECT
        year,
        total_sales,
        LAG(total_sales) OVER (
            ORDER BY year
        ) AS previous_year_sales
    FROM yearly_sales
)
SELECT
    year,
    total_sales,
    previous_year_sales,
    (total_sales - previous_year_sales)
        * 100.0 / previous_year_sales AS growth_percentage
FROM sales_with_previous
ORDER BY year;
```

This demonstrates aggregation, CTEs, window functions, and growth calculations.

---

# 9. Statistical Analysis

Notebook:

```text
notebooks/03_statistical_analysis.ipynb
```

The statistical stage determines whether observed differences between groups have sufficient evidence to be considered statistically significant.

## Research Question 1

**Is there a statistically significant difference in sales across regions?**

### Null hypothesis

```text
H₀: Mean sales are equal across all regions.
```

### Alternative hypothesis

```text
H₁: At least one region has a different mean sales value.
```

Significance level:

```text
α = 0.05
```

---

## 9.1 One-way ANOVA

```python
from scipy.stats import f_oneway

f_stat, p_value = f_oneway(
    east,
    west,
    central,
    south
)
```

Interpretation:

```text
p < 0.05
    → Reject H₀

p >= 0.05
    → Fail to reject H₀
```

---

## 9.2 Variance check

Levene's test is used to examine equality of variances:

```python
levene_stat, levene_p = stats.levene(
    east,
    west,
    central,
    south
)
```

---

## 9.3 Non-parametric robustness check

Because transaction sales are right-skewed, Kruskal-Wallis is also used:

```python
h_stat, kruskal_p = kruskal(
    east,
    west,
    central,
    south
)
```

---

## 9.4 Post-hoc analysis

When an overall test indicates significant differences, Tukey HSD can identify which pairs differ:

```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey = pairwise_tukeyhsd(
    endog=df["Sales"],
    groups=df["Region"],
    alpha=0.05
)

print(tukey)
```

---

## 9.5 Customer segment analysis

The same statistical workflow is applied to:

- Consumer
- Corporate
- Home Office

This provides a second statistical research question:

> Are sales distributions significantly different across customer segments?

---

# 10. Streamlit Dashboard

Application:

```text
app/dashboard.py
```

The dashboard turns the analysis into an interactive application.

## Dashboard filters

The sidebar contains:

- Region
- Category
- Customer Segment

All KPI values and charts respond to the selected filters.

---

## KPI cards

The dashboard displays:

```text
Total Sales
Total Orders
Total Customers
Average Order Value
```

---

## Visualizations

### Monthly Sales Trend

Interactive Plotly line chart showing sales over time.

### Sales by Region

Bar chart comparing regional performance.

### Sales by Category

Bar chart comparing Technology, Furniture, and Office Supplies.

### Sales by Sub-category

Horizontal bar chart covering all 17 sub-categories.

### Top 10 Products

Horizontal bar chart showing the highest-selling products.

### Customer Segment

Sales distribution across Consumer, Corporate, and Home Office.

### Shipping Analysis

Shows:

- Orders by shipping mode
- Sales by shipping mode
- Average shipping duration

### Business Insights

The dashboard dynamically identifies:

- Top region
- Top category
- Top customer segment
- Top sub-category

### Data Explorer

An expandable section allows users to inspect the filtered transaction-level dataset.

---

# 11. Technology Stack

| Area | Technology |
|---|---|
| Language | Python |
| Data processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Statistics | SciPy, Statsmodels |
| Database | SQLite |
| Query language | SQL |
| Dashboard | Streamlit |
| Development | Jupyter Notebook, VS Code |
| Version control | Git, GitHub |

---

# 12. Installation

Clone the repository:

```bash
git clone https://github.com/SKsudhanshukumar/retail-sales-dashboard.git
cd retail-sales-dashboard
```

Create a virtual environment:

```bash
python -m venv venv
```

Windows activation:

```bash
venv\Scripts activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 13. Running the Project

## Data pipeline

From the project root:

```bash
python src/data_pipeline.py
```

This creates or updates:

```text
data/retail_sales.db
```

## Streamlit application

Run from the project root:

```bash
streamlit run app/dashboard.py
```

The dashboard will open through Streamlit's local development URL.

---

# 14. requirements.txt

Current dependencies:

```text
pandas
numpy
matplotlib
seaborn
scipy
statsmodels
plotly
streamlit
openpyxl
```

---

# 15. Current Project Status

| Component                     | Status          |
| Dataset inspection            | ✅ Completed   |
| Data cleaning                 | ✅ Completed   |
| Date feature engineering      | ✅ Completed   |
| Shipping-duration feature     | ✅ Completed   |
| EDA                           | ✅ Completed   |
| Sales trend analysis          | ✅ Completed   |
| Regional analysis             | ✅ Completed   |
| Category analysis             | ✅ Completed   |
| Product analysis              | ✅ Completed   |
| Customer segment analysis     | ✅ Completed   |
| Shipping analysis             | ✅ Completed   |
| SQLite database               | ✅ Implemented |
| SQL business queries          | ✅ Implemented |
| Statistical analysis          | ✅ Implemented |
| Streamlit dashboard           | ✅ Implemented |
| Dashboard testing/polish      | ⏳ Pending     |
| ML forecasting                | ⏳ Future      |
| Model evaluation              | ⏳ Future      |
| Deployment                    | ⏳ Future      |

---

# 16. Key Findings So Far

Based on the current dataset analysis:

1. Total sales are approximately **$2.26 million**.
2. There are approximately **4,922 unique orders** and **793 customers**.
3. Sales increased substantially after 2016, with 2018 being the strongest year.
4. **Q4** is the strongest quarter.
5. **November** has the highest total monthly sales.
6. **West** has the highest total regional sales.
7. **Technology** is the highest-selling category.
8. **Phones** are the highest-selling sub-category.
9. **Consumer** contributes the largest amount of sales.
10. **Standard Class** is the most commonly used shipping mode.
11. There are no duplicate rows.
12. Sales are right-skewed, so median values and robust statistical checks are useful.

These are descriptive findings. Statistical tests are used separately when assessing whether observed group differences have sufficient statistical evidence.

---

# 17. Data Limitations

The dataset does not contain:

- Profit
- Quantity
- Discount
- Cost
- Customer lifetime value

Therefore, the project does not make unsupported claims about:

- Profitability
- Profit margin
- Discount effectiveness
- Units sold
- Revenue per unit

The project is specifically focused on sales and transaction-level analysis.

---

# 18. Future Machine Learning Phase

The next major phase is to turn this analytics project into a stronger Data Science project by adding sales forecasting.

Planned workflow:

```text
Historical Sales
       ↓
Time-Series Feature Engineering
       ↓
Train / Validation Split
       ↓
Baseline Model
       ↓
ML Models
       ↓
MAE / RMSE Evaluation
       ↓
Model Selection
       ↓
Future Sales Forecast
       ↓
Streamlit Integration
```

Potential models:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting
- XGBoost, if added later

Model selection will be based on measured validation performance.

---

# 19. Future Dashboard Improvements

Planned enhancements:

- Date-range filter
- Better KPI comparisons
- Year-over-year KPI changes
- Downloadable filtered data
- More polished chart formatting
- Forecast visualization
- Model performance section
- Forecast horizon controls
- Deployment

---

# 20. Skills Demonstrated

### Python

- Pandas
- NumPy
- Data cleaning
- Feature engineering
- Aggregation

### Data Science

- EDA
- Trend analysis
- Seasonality analysis
- Segmentation
- KPI development
- Business interpretation

### SQL

- Aggregation
- `GROUP BY`
- `COUNT(DISTINCT)`
- CTEs
- Window functions
- `LAG()`
- SQL views

### Statistics

- Hypothesis testing
- One-way ANOVA
- Levene's test
- Kruskal-Wallis test
- Tukey HSD

### Visualization

- Matplotlib
- Seaborn
- Plotly

### Application Development

- Streamlit
- Interactive filtering
- Dynamic KPIs
- Interactive charts

### Engineering

- Modular project structure
- Data pipeline
- SQLite database
- Requirements management
- Git/GitHub workflow

---

# 21. Project Summary

This project demonstrates an end-to-end retail analytics workflow, starting with raw transaction data and progressing through data cleaning, exploratory analysis, SQL querying, statistical testing, and interactive dashboard development.

The current implementation provides a strong foundation for the next phase: **machine-learning-based sales forecasting**.

The eventual goal is to transform the project from a descriptive analytics application into a complete Data Science solution combining:

```text
Data Engineering
      +
Data Analysis
      +
Statistics
      +
Machine Learning
      +
Visualization
      +
Deployment
```

That gives the project a much stronger portfolio story than simply uploading a notebook full of charts and hoping recruiters interpret the smoke signals correctly.
