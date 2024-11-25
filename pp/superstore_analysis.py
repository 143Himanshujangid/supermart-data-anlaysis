import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Superstore Analysis", layout="wide")

# Function to load the data
@st.cache_data
def load_data(file_path):
    try:
        # Adding encoding to handle special characters
        data = pd.read_csv(file_path, encoding='latin1')
        data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
        data.dropna(subset=['Order Date'], inplace=True)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load the dataset
file_url = "https://raw.githubusercontent.com/143Himanshujangid/supermart-data-anlaysis/main/pp/superstore.csv"
superstore_data = load_data(file_path)

if superstore_data is not None:
    # Sidebar for navigation
    st.sidebar.title("Superstore Analysis")
    option = st.sidebar.selectbox(
        "Select Analysis Question",
        [
            "Overview",
            "Q1: Sales by Category",
            "Q2: Sales by Sub-Category",
            "Q3: Sales by Region",
            "Q4: Profit by Region",
            "Q5: Order Count by State",
            "Q6: Sales and Profit by State",
            "Q7: Sales by Ship Mode",
            "Q8: Monthly Trends in Sales",
            "Q9: Monthly Profit Trends",
            "Q10: Average Order Value by Category",
            "Q11: Most Profitable Products",
            "Q12: Product Category with Highest Sales",
            "Q13: Top 10 Selling Products",
            "Q14: Profitability by Sub-Category",
            "Q15: Sales vs Discounts Analysis",
            "Q16: Sales by Customer Segment",
            "Q17: Average Sales per Order by Sub-Category",
            "Q18: Annual Order Counts",
            "Q19: Profit by Ship Mode",
            "Q20: Regional Sales Distribution",
            "Q21: Sales by State and Segment",
            "Q22: Product Sales Distribution by Region",
            "Q23: Profit vs Sales Analysis",
            "Q24: Monthly Order Counts",
            "Q25: Sales Trend by Product Type",
            "Q26: Profit by Customer Segment",
            "Q27: Sales by Salesperson",
            "Q28: Monthly Discount Trends",
            "Q29: Regional Sales per Employee",
            "Q30: Best Performing Ship Mode",
            "Q31: Sales per Customer",
            "Q32: Profit by Product",
            "Q33: Category vs Profit",
            "Q34: Discount vs Profit",
            "Q35: Sales and Profit by Ship Mode",
            "Q36: Profit Margin by Sub-Category",
            "Q37: Sales Correlation Matrix",
            "Q38: Yearly Sales Growth",
            "Q39: Sales vs Region by Sub-Category",
            "Q40: Product Profitability Comparison",
            "Q41: Monthly Customer Purchase Frequency",
            "Q42: Profit by Year",
            "Q43: Top 5 Most Ordered Products",
            "Q44: Correlation Between Sales and Quantity",
            "Q45: Sales Trends by Customer"
        ]
    )

    # Main Page
    st.title("Superstore Analysis Dashboard")

    if option == "Overview":
        st.subheader("Dataset Overview")
        st.write("### First 10 Rows")
        st.dataframe(superstore_data.head(10))
        st.write("### Dataset Summary")
        st.write(superstore_data.describe())

    elif option == "Q1: Sales by Category":
        st.subheader("Q1: Sales by Category")
        category_sales = superstore_data.groupby('Category')['Sales'].sum()
        fig, ax = plt.subplots()
        category_sales.plot(kind='bar', color=['blue', 'green', 'orange'], ax=ax)
        ax.set_title("Sales by Category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Total Sales")
        st.pyplot(fig)

    elif option == "Q2: Sales by Sub-Category":
        st.subheader("Q2: Sales by Sub-Category")
        sub_category_sales = superstore_data.groupby('Sub-Category')['Sales'].sum().sort_values()
        fig, ax = plt.subplots(figsize=(10, 8))
        sub_category_sales.plot(kind='barh', color='purple', ax=ax)
        ax.set_title("Sales by Sub-Category")
        ax.set_xlabel("Total Sales")
        ax.set_ylabel("Sub-Category")
        st.pyplot(fig)

    elif option == "Q3: Sales by Region":
        st.subheader("Q3: Sales by Region")
        region_sales = superstore_data.groupby('Region')['Sales'].sum()
        fig, ax = plt.subplots()
        region_sales.plot(kind='bar', color='red', ax=ax)
        ax.set_title("Sales by Region")
        ax.set_xlabel("Region")
        ax.set_ylabel("Total Sales")
        st.pyplot(fig)

    elif option == "Q4: Profit by Region":
        st.subheader("Q4: Profit by Region")
        region_profit = superstore_data.groupby('Region')['Profit'].sum()
        fig, ax = plt.subplots()
        region_profit.plot(kind='bar', color='orange', ax=ax)
        ax.set_title("Profit by Region")
        ax.set_xlabel("Region")
        ax.set_ylabel("Profit")
        st.pyplot(fig)

    elif option == "Q5: Order Count by State":
        st.subheader("Q5: Order Count by State")
        state_order_count = superstore_data.groupby('State')['Order ID'].nunique()
        fig, ax = plt.subplots(figsize=(12, 8))
        state_order_count.plot(kind='barh', color='cyan', ax=ax)
        ax.set_title("Order Count by State")
        ax.set_xlabel("Order Count")
        ax.set_ylabel("State")
        st.pyplot(fig)

    elif option == "Q6: Sales and Profit by State":
        st.subheader("Q6: Sales and Profit by State")
        state_sales_profit = superstore_data.groupby('State')[['Sales', 'Profit']].sum()
        st.write(state_sales_profit)

    elif option == "Q7: Sales by Ship Mode":
        st.subheader("Q7: Sales by Ship Mode")
        ship_mode_sales = superstore_data.groupby('Ship Mode')['Sales'].sum()
        fig, ax = plt.subplots()
        ship_mode_sales.plot(kind='bar', color='purple', ax=ax)
        ax.set_title("Sales by Ship Mode")
        ax.set_xlabel("Ship Mode")
        ax.set_ylabel("Total Sales")
        st.pyplot(fig)

    elif option == "Q8: Monthly Trends in Sales":
        st.subheader("Q8: Monthly Trends in Sales")
        superstore_data['Month'] = superstore_data['Order Date'].dt.to_period('M')
        monthly_sales = superstore_data.groupby('Month')['Sales'].sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        monthly_sales.plot(kind='line', marker='o', color='green', ax=ax)
        ax.set_title("Monthly Sales Trends")
        ax.set_xlabel("Month")
        ax.set_ylabel("Total Sales")
        st.pyplot(fig)

    elif option == "Q9: Monthly Profit Trends":
        st.subheader("Q9: Monthly Profit Trends")
        monthly_profit = superstore_data.groupby('Month')['Profit'].sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        monthly_profit.plot(kind='line', marker='o', color='red', ax=ax)
        ax.set_title("Monthly Profit Trends")
        ax.set_xlabel("Month")
        ax.set_ylabel("Total Profit")
        st.pyplot(fig)

    elif option == "Q10: Average Order Value by Category":
        st.subheader("Q10: Average Order Value by Category")
        avg_order_value = superstore_data.groupby('Category')['Sales'].mean()
        fig, ax = plt.subplots()
        avg_order_value.plot(kind='bar', color='yellow', ax=ax)
        ax.set_title("Average Order Value by Category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Average Sales")
        st.pyplot(fig)

    # Additional Questions (Q11-Q30 with visualizations)
    elif option == "Q11: Most Profitable Products":
        st.subheader("Q11: Most Profitable Products")
        product_profit = superstore_data.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(10, 6))
        product_profit.plot(kind='bar', color='brown', ax=ax)
        ax.set_title("Top 10 Most Profitable Products")
        ax.set_xlabel("Product")
        ax.set_ylabel("Profit")
        st.pyplot(fig)

    elif option == "Q12: Product Category with Highest Sales":
        st.subheader("Q12: Product Category with Highest Sales")
        highest_sales_category = superstore_data.groupby('Category')['Sales'].sum().idxmax()
        st.write(f"Product category with highest sales: {highest_sales_category}")

    elif option == "Q13: Top 10 Selling Products":
        st.subheader("Q13: Top 10 Selling Products")
        top_10_products = superstore_data.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(10, 6))
        top_10_products.plot(kind='barh', color='skyblue', ax=ax)
        ax.set_title("Top 10 Selling Products")
        ax.set_xlabel("Sales")
        ax.set_ylabel("Product")
        st.pyplot(fig)

    elif option == "Q14: Profitability by Sub-Category":
        st.subheader("Q14: Profitability by Sub-Category")
        sub_category_profit = superstore_data.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        sub_category_profit.plot(kind='barh', color='orange', ax=ax)
        ax.set_title("Profit by Sub-Category")
        ax.set_xlabel("Profit")
        ax.set_ylabel("Sub-Category")
        st.pyplot(fig)

    elif option == "Q15: Sales vs Discounts Analysis":
        st.subheader("Q15: Sales vs Discounts Analysis")
        sales_discount_corr = superstore_data[['Sales', 'Discount']].corr()
        st.write(sales_discount_corr)

    # Continue adding more questions with visualizations like Q16, Q17, etc.

