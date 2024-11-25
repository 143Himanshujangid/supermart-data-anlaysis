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
        # Adding encoding to handle special characters, specifying delimiter, and skipping bad lines
        data = pd.read_csv(file_path, encoding='latin1', delimiter=',', on_bad_lines='skip')

        # Print problematic rows
        for i, row in data.iterrows():
            try:
                pd.to_datetime(row['Order Date'])
            except ValueError:
                print(f"Error parsing date in row {i}: {row['Order Date']}")

        data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
        data.dropna(subset=['Order Date'], inplace=True)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load the dataset
file_path = r"https://github.com/143Himanshujangid/supermart-data-anlaysis/blob/main/pp/superstore.csv"
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
        fig, ax = plt.subplots(figsize=(12, 6))
        state_sales_profit.plot(kind='bar', ax=ax)
        ax.set_title("Sales and Profit by State")
        ax.set_xlabel("State")
        ax.set_ylabel("Amount")
        st.pyplot(fig)

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

    # Additional Questions (Q11-Q45 with visualizations)
    elif option == "Q11: Most Profitable Products":
        st.subheader("Q11: Most Profitable Products")
        product_profit = superstore_data.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(10, 6))
        product_profit.plot(kind='bar', color='brown', ax=ax)
        ax.set_title("Top 10 Most Profitable Products")
        ax.set_xlabel("Product")
        ax.set_ylabel("Profit")
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        st.pyplot(fig)

    elif option == "Q12: Product Category with Highest Sales":
        st.subheader("Q12: Product Category with Highest Sales")
        highest_sales_category = superstore_data.groupby('Category')['Sales'].sum().idxmax()
        st.write(f"Product category with highest sales: {highest_sales_category}")

        # Visualization (optional):
        fig, ax = plt.subplots()
        superstore_data.groupby('Category')['Sales'].sum().plot(kind='bar', ax=ax)
        ax.set_title("Sales by Category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Total Sales")
        st.pyplot(fig)

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
        # Correlation matrix
        sales_discount_corr = superstore_data[['Sales', 'Discount']].corr()
        st.write(sales_discount_corr)

        # Scatter plot (optional)
        fig, ax = plt.subplots()
        sns.scatterplot(x='Sales', y='Discount', data=superstore_data, ax=ax)
        ax.set_title("Sales vs Discounts")
        st.pyplot(fig)

    elif option == "Q16: Sales by Customer Segment":
        st.subheader("Q16: Sales by Customer Segment")
        segment_sales = superstore_data.groupby('Segment')['Sales'].sum()
        fig, ax = plt.subplots()
        segment_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
        ax.set_title("Sales by Customer Segment")
        st.pyplot(fig)

    elif option == "Q17: Average Sales per Order by Sub-Category":
        st.subheader("Q17: Average Sales per Order by Sub-Category")
        avg_sales_per_order = superstore_data.groupby('Sub-Category')['Sales'].mean().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        avg_sales_per_order.plot(kind='bar', color='green', ax=ax)
        ax.set_title("Average Sales per Order by Sub-Category")
        ax.set_xlabel("Sub-Category")
        ax.set_ylabel("Average Sales")
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif option == "Q18: Annual Order Counts":
        st.subheader("Q18: Annual Order Counts")
        superstore_data['Year'] = superstore_data['Order Date'].dt.year
        annual_order_counts = superstore_data.groupby('Year')['Order ID'].nunique()
        fig, ax = plt.subplots()
        annual_order_counts.plot(kind='bar', color='blue', ax=ax)
        ax.set_title("Annual Order Counts")
        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Orders")
        st.pyplot(fig)

    elif option == "Q19: Profit by Ship Mode":
        st.subheader("Q19: Profit by Ship Mode")
        profit_by_ship_mode = superstore_data.groupby('Ship Mode')['Profit'].sum()
        fig, ax = plt.subplots()
        profit_by_ship_mode.plot(kind='bar', color='red', ax=ax)
        ax.set_title("Profit by Ship Mode")
        ax.set_xlabel("Ship Mode")
        ax.set_ylabel("Profit")
        st.pyplot(fig)

    elif option == "Q20: Regional Sales Distribution":
        st.subheader("Q20: Regional Sales Distribution")
        regional_sales_dist = superstore_data.groupby('Region')['Sales'].sum()
        fig, ax = plt.subplots()
        regional_sales_dist.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
        ax.set_title("Regional Sales Distribution")
        st.pyplot(fig)
