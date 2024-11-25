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
        data = pd.read_csv(file_path, encoding='latin1', delimiter=',', error_bad_lines=False)
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

    elif option == "Q21: Sales by State and Segment":
        st.subheader("Q21: Sales by State and Segment")
        sales_by_state_segment = superstore_data.groupby(['State', 'Segment'])['Sales'].sum().unstack()
        fig, ax = plt.subplots(figsize=(12, 8))
        sales_by_state_segment.plot(kind='bar', ax=ax)
        ax.set_title("Sales by State and Segment")
        ax.set_xlabel("State")
        ax.set_ylabel("Sales")
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif option == "Q22: Product Sales Distribution by Region":
        st.subheader("Q22: Product Sales Distribution by Region")
        sales_dist_by_region = superstore_data.groupby(['Region', 'Category'])['Sales'].sum().unstack()
        fig, ax = plt.subplots(figsize=(10, 6))
        sales_dist_by_region.plot(kind='bar', ax=ax)
        ax.set_title("Product Sales Distribution by Region")
        ax.set_xlabel("Region")
        ax.set_ylabel("Sales")
        st.pyplot(fig)

    elif option == "Q23: Profit vs Sales Analysis":
        st.subheader("Q23: Profit vs Sales Analysis")
        fig, ax = plt.subplots()
        sns.scatterplot(x='Sales', y='Profit', data=superstore_data, ax=ax)
        ax.set_title("Profit vs Sales")
        st.pyplot(fig)

    elif option == "Q24: Monthly Order Counts":
        st.subheader("Q24: Monthly Order Counts")
        monthly_order_counts = superstore_data.groupby('Month')['Order ID'].nunique()
        fig, ax = plt.subplots(figsize=(12, 6))
        monthly_order_counts.plot(kind='line', marker='o', color='purple', ax=ax)
        ax.set_title("Monthly Order Counts")
        ax.set_xlabel("Month")
        ax.set_ylabel("Number of Orders")
        st.pyplot(fig)

    elif option == "Q25: Sales Trend by Product Type":
        st.subheader("Q25: Sales Trend by Product Type")
        sales_trend_by_product = superstore_data.groupby(['Month', 'Category'])['Sales'].sum().unstack()
        fig, ax = plt.subplots(figsize=(12, 6))
        sales_trend_by_product.plot(kind='line', marker='o', ax=ax)
        ax.set_title("Sales Trend by Product Type")
        ax.set_xlabel("Month")
        ax.set_ylabel("Sales")
        st.pyplot(fig)

    elif option == "Q26: Profit by Customer Segment":
        st.subheader("Q26: Profit by Customer Segment")
        profit_by_segment = superstore_data.groupby('Segment')['Profit'].sum()
        fig, ax = plt.subplots()
        profit_by_segment.plot(kind='bar', color='green', ax=ax)
        ax.set_title("Profit by Customer Segment")
        ax.set_xlabel("Segment")
        ax.set_ylabel("Profit")
        st.pyplot(fig)

    elif option == "Q27: Sales by Salesperson":
        st.subheader("Q27: Sales by Salesperson")
        sales_by_salesperson = superstore_data.groupby('Salesperson')['Sales'].sum().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        sales_by_salesperson.plot(kind='bar', color='blue', ax=ax)
        ax.set_title("Sales by Salesperson")
        ax.set_xlabel("Salesperson")
        ax.set_ylabel("Sales")
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif option == "Q28: Monthly Discount Trends":
        st.subheader("Q28: Monthly Discount Trends")
        monthly_discount_trends = superstore_data.groupby('Month')['Discount'].mean()
        fig, ax = plt.subplots(figsize=(12, 6))
        monthly_discount_trends.plot(kind='line', marker='o', color='orange', ax=ax)
        ax.set_title("Monthly Discount Trends")
        ax.set_xlabel("Month")
        ax.set_ylabel("Average Discount")
        st.pyplot(fig)

    elif option == "Q29: Regional Sales per Employee":
        st.subheader("Q29: Regional Sales per Employee")
        # Assuming 'Salesperson' represents employees
        regional_sales_per_employee = superstore_data.groupby('Region')['Salesperson'].nunique()
        regional_sales = superstore_data.groupby('Region')['Sales'].sum()
        sales_per_employee = regional_sales / regional_sales_per_employee
        fig, ax = plt.subplots()
        sales_per_employee.plot(kind='bar', color='purple', ax=ax)
        ax.set_title("Regional Sales per Employee")
        ax.set_xlabel("Region")
        ax.set_ylabel("Sales per Employee")
        st.pyplot(fig)

    elif option == "Q30: Best Performing Ship Mode":
        st.subheader("Q30: Best Performing Ship Mode")
        best_ship_mode = superstore_data.groupby('Ship Mode')['Profit'].sum().idxmax()
        st.write(f"Best performing ship mode (based on profit): {best_ship_mode}")

        # Visualization (optional):
        fig, ax = plt.subplots()
        superstore_data.groupby('Ship Mode')['Profit'].sum().plot(kind='bar', ax=ax)
        ax.set_title("Profit by Ship Mode")
        ax.set_xlabel("Ship Mode")
        ax.set_ylabel("Profit")
        st.pyplot(fig)

    elif option == "Q31: Sales per Customer":
        st.subheader("Q31: Sales per Customer")
        sales_per_customer = superstore_data.groupby('Customer ID')['Sales'].sum().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        sales_per_customer.head(10).plot(kind='bar', color='brown', ax=ax)  # Showing top 10 customers
        ax.set_title("Sales per Customer (Top 10)")
        ax.set_xlabel("Customer ID")
        ax.set_ylabel("Sales")
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif option == "Q32: Profit by Product":
        st.subheader("Q32: Profit by Product")
        profit_by_product = superstore_data.groupby('Product Name')['Profit'].sum().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        profit_by_product.head(10).plot(kind='bar', color='green', ax=ax)  # Showing top 10 products
        ax.set_title("Profit by Product (Top 10)")
        ax.set_xlabel("Product Name")
        ax.set_ylabel("Profit")
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif option == "Q33: Category vs Profit":
        st.subheader("Q33: Category vs Profit")
        category_profit = superstore_data.groupby('Category')['Profit'].sum()
        fig, ax = plt.subplots()
        category_profit.plot(kind='bar', color='blue', ax=ax)
        ax.set_title("Category vs Profit")
        ax.set_xlabel("Category")
        ax.set_ylabel("Profit")
        st.pyplot(fig)

    elif option == "Q34: Discount vs Profit":
        st.subheader("Q34: Discount vs Profit")
        fig, ax = plt.subplots()
        sns.scatterplot(x='Discount', y='Profit', data=superstore_data, ax=ax)
        ax.set_title("Discount vs Profit")
        st.pyplot(fig)

    elif option == "Q35: Sales and Profit by Ship Mode":
        st.subheader("Q35: Sales and Profit by Ship Mode")
        sales_profit_by_ship_mode = superstore_data.groupby('Ship Mode')[['Sales', 'Profit']].sum()
        fig, ax = plt.subplots()
        sales_profit_by_ship_mode.plot(kind='bar', ax=ax)
        ax.set_title("Sales and Profit by Ship Mode")
        ax.set_xlabel("Ship Mode")
        ax.set_ylabel("Amount")
        st.pyplot(fig)

    elif option == "Q36: Profit Margin by Sub-Category":
        st.subheader("Q36: Profit Margin by Sub-Category")
        superstore_data['Profit Margin'] = (superstore_data['Profit'] / superstore_data['Sales']) * 100
        profit_margin_by_subcat = superstore_data.groupby('Sub-Category')['Profit Margin'].mean().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        profit_margin_by_subcat.plot(kind='bar', color='orange', ax=ax)
        ax.set_title("Profit Margin by Sub-Category")
        ax.set_xlabel("Sub-Category")
        ax.set_ylabel("Profit Margin (%)")
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif option == "Q37: Sales Correlation Matrix":
        st.subheader("Q37: Sales Correlation Matrix")
        corr_matrix = superstore_data[['Sales', 'Quantity', 'Discount', 'Profit']].corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
        ax.set_title("Sales Correlation Matrix")
        st.pyplot(fig)

    elif option == "Q38: Yearly Sales Growth":
        st.subheader("Q38: Yearly Sales Growth")
        yearly_sales = superstore_data.groupby('Year')['Sales'].sum()
        yearly_sales_growth = yearly_sales.pct_change() * 100  # Calculate percentage change
        fig, ax = plt.subplots()
        yearly_sales_growth.plot(kind='line', marker='o', color='green', ax=ax)
        ax.set_title("Yearly Sales Growth (%)")
        ax.set_xlabel("Year")
        ax.set_ylabel("Sales Growth (%)")
        st.pyplot(fig)

    elif option == "Q39: Sales vs Region by Sub-Category":
        st.subheader("Q39: Sales vs Region by Sub-Category")
        sales_by_region_subcat = superstore_data.groupby(['Region', 'Sub-Category'])['Sales'].sum().unstack()
        fig, ax = plt.subplots(figsize=(12, 8))
        sales_by_region_subcat.plot(kind='bar', ax=ax)
        ax.set_title("Sales vs Region by Sub-Category")
        ax.set_xlabel("Region")
        ax.set_ylabel("Sales")
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif option == "Q40: Product Profitability Comparison":
        st.subheader("Q40: Product Profitability Comparison")
        # Select top 5 most profitable and least profitable products
        top_5_profitable = superstore_data.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(5)
        top_5_least_profitable = superstore_data.groupby('Product Name')['Profit'].sum().sort_values().head(5)

        # Combine the data for visualization
        profitability_comparison = pd.concat([top_5_profitable, top_5_least_profitable])

        fig, ax = plt.subplots(figsize=(10, 6))
        profitability_comparison.plot(kind='bar', color=['green', 'red'], ax=ax)
        ax.set_title("Product Profitability Comparison (Top 5 & Bottom 5)")
        ax.set_xlabel("Product Name")
        ax.set_ylabel("Profit")
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif option == "Q41: Monthly Customer Purchase Frequency":
        st.subheader("Q41: Monthly Customer Purchase Frequency")
        monthly_customer_purchases = superstore_data.groupby(['Month', 'Customer ID'])['Order ID'].nunique().reset_index()
        monthly_purchase_frequency = monthly_customer_purchases.groupby('Month')['Customer ID'].count()
        fig, ax = plt.subplots(figsize=(12, 6))
        monthly_purchase_frequency.plot(kind='line', marker='o', color='blue', ax=ax)
        ax.set_title("Monthly Customer Purchase Frequency")
        ax.set_xlabel("Month")
        ax.set_ylabel("Number of Customers")
        st.pyplot(fig)

    elif option == "Q42: Profit by Year":
        st.subheader("Q42: Profit by Year")
        profit_by_year = superstore_data.groupby('Year')['Profit'].sum()
        fig, ax = plt.subplots()
        profit_by_year.plot(kind='bar', color='purple', ax=ax)
        ax.set_title("Profit by Year")
        ax.set_xlabel("Year")
        ax.set_ylabel("Profit")
        st.pyplot(fig)

    elif option == "Q43: Top 5 Most Ordered Products":
        st.subheader("Q43: Top 5 Most Ordered Products")
        most_ordered_products = superstore_data.groupby('Product Name')['Quantity'].sum().sort_values(ascending=False).head(5)
        fig, ax = plt.subplots(figsize=(10, 6))
        most_ordered_products.plot(kind='bar', color='orange', ax=ax)
        ax.set_title("Top 5 Most Ordered Products")
        ax.set_xlabel("Product Name")
        ax.set_ylabel("Quantity Ordered")
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif option == "Q44: Correlation Between Sales and Quantity":
        st.subheader("Q44: Correlation Between Sales and Quantity")
        sales_quantity_corr = superstore_data[['Sales', 'Quantity']].corr()
        st.write(sales_quantity_corr)

        # Scatter plot (optional)
        fig, ax = plt.subplots()
        sns.scatterplot(x='Sales', y='Quantity', data=superstore_data, ax=ax)
        ax.set_title("Correlation Between Sales and Quantity")
        st.pyplot(fig)

    elif option == "Q45: Sales Trends by Customer":
        st.subheader("Q45: Sales Trends by Customer")
        # Select top 5 customers with highest total sales
        top_5_customers = superstore_data.groupby('Customer ID')['Sales'].sum().sort_values(ascending=False).head(5).index

        # Filter data for the top 5 customers
        top_customer_sales = superstore_data[superstore_data['Customer ID'].isin(top_5_customers)]

        # Group by month and customer ID to get monthly sales for each customer
        monthly_sales_by_customer = top_customer_sales.groupby(['Month', 'Customer ID'])['Sales'].sum().unstack()

        fig, ax = plt.subplots(figsize=(12, 6))
        monthly_sales_by_customer.plot(kind='line', marker='o', ax=ax)
        ax.set_title("Sales Trends by Customer (Top 5)")
        ax.set_xlabel("Month")
        ax.set_ylabel("Sales")
        st.pyplot(fig)
