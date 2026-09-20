import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# Page configuration
st.set_page_config(
    page_title="Retail Sales Dashboard",
    page_icon="📊",
    layout="wide"
)



# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = BASE_DIR / "data" / "processed" / "retail_cleaned.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Title
st.title("📊 Retail Sales Analytics Dashboard")

st.markdown(
    """
    Analyze sales performance, customer segments,
    product categories, regional performance,
    and shipping behavior.
    """
)

st.sidebar.header("🔎 Filters")

# Region filter
regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

# Category filter
categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

# Segment filter
segments = st.sidebar.multiselect(
    "Select Customer Segment",
    options=sorted(df["Segment"].unique()),
    default=sorted(df["Segment"].unique())
)

# Apply the filters
filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories)) &
    (df["Segment"].isin(segments))
]


# KPI cards
total_sales = filtered_df["Sales"].sum()

total_orders = filtered_df["Order ID"].nunique()

total_customers = filtered_df["Customer ID"].nunique()

average_order_value = (
    total_sales / total_orders
    if total_orders > 0
    else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Total Sales",
    f"${total_sales:,.0f}"
)

col2.metric(
    "🛒 Total Orders",
    f"{total_orders:,}"
)

col3.metric(
    "👥 Customers",
    f"{total_customers:,}"
)

col4.metric(
    "📦 Avg Order Value",
    f"${average_order_value:,.2f}"
)

st.divider()

# Sales trend chart
monthly_sales = (
    filtered_df
    .groupby("Year_Month", as_index=False)["Sales"]
    .sum()
)

monthly_sales["Year_Month"] = (
    monthly_sales["Year_Month"]
    .astype(str)
)

fig_monthly = px.line(
    monthly_sales,
    x="Year_Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

fig_monthly.update_layout(
    xaxis_title="Month",
    yaxis_title="Sales"
)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)

col1, col2 = st.columns(2)

with col1:
    region_sales = (
        filtered_df
        .groupby("Region", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig_region = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        title="Sales by Region",
        text_auto=".2s"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

    # Category chart
    with col2:

        category_sales = (
            filtered_df
            .groupby("Category", as_index=False)["Sales"]
            .sum()
            .sort_values("Sales", ascending=False)
        )

        fig_category = px.bar(
            category_sales,
            x="Category",
            y="Sales",
            title="Sales by Category",
            text_auto=".2s"
        )

        st.plotly_chart(
            fig_category,
            use_container_width=True
        )

# Sub-category analysis
subcategory_sales = (
    filtered_df
    .groupby("Sub-Category", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=True)
)

fig_subcategory = px.bar(
    subcategory_sales,
    x="Sales",
    y="Sub-Category",
    orientation="h",
    title="Sales by Sub-Category",
    text_auto=".2s"
)

st.plotly_chart(
    fig_subcategory,
    use_container_width=True
)

# Top 10 products
top_products = (
    filtered_df
    .groupby("Product Name", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
    .head(10)
    .sort_values("Sales", ascending=True)
)

fig_products = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales",
    text_auto=".2s"
)

st.plotly_chart(
    fig_products,
    use_container_width=True
)

# Customer segment chart
segment_sales = (
    filtered_df
    .groupby("Segment", as_index=False)["Sales"]
    .sum()
)
fig_segment = px.pie(
    segment_sales,
    names="Segment",
    values="Sales",
    title="Sales by Customer Segment"
)

st.plotly_chart(
    fig_segment,
    use_container_width=True
)

# Shipping analysis
shipping = (
    filtered_df
    .groupby("Ship Mode")
    .agg(
        Orders=("Order ID", "nunique"),
        Sales=("Sales", "sum"),
        Avg_Shipping_Days=("Shipping_Days", "mean")
    )
    .reset_index()
)

shipping["Avg_Shipping_Days"] = (
    shipping["Avg_Shipping_Days"].round(2)
)

st.subheader("🚚 Shipping Analysis")

st.dataframe(
    shipping,
    use_container_width=True,
    hide_index=True
)

# Add a shipping chart
fig_shipping = px.bar(
    shipping,
    x="Ship Mode",
    y="Avg_Shipping_Days",
    title="Average Shipping Time by Shipping Mode",
    text_auto=".2f"
)

st.plotly_chart(
    fig_shipping,
    use_container_width=True
)

# Add business insights
st.divider()

st.header("💡 Key Business Insights")
best_region = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .idxmax()
)

best_category = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .idxmax()
)

best_segment = (
    filtered_df.groupby("Segment")["Sales"]
    .sum()
    .idxmax()
)

best_subcategory = (
    filtered_df.groupby("Sub-Category")["Sales"]
    .sum()
    .idxmax()
)

st.write(
    f"• **Top Region:** {best_region}"
)

st.write(
    f"• **Top Category:** {best_category}"
)

st.write(
    f"• **Top Customer Segment:** {best_segment}"
)

st.write(
    f"• **Top Sub-Category:** {best_subcategory}"
)

# Add a raw-data explorer
st.divider()

st.header("📄 Data Explorer")

with st.expander("View filtered transaction data"):

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )