# Abhishek_jadhav_69137
# Python capstone project

import pandas as pd
import matplotlib.pyplot as plt

print("  SALES ANALYSIS DASHBOARD  ")

try:
    sales_df = pd.read_csv("sales_data.csv")
    targets_df = pd.read_excel("sales_targets.xlsx")

    print("Sales data loaded successfully.")
    print("Sales target data loaded successfully.")

except FileNotFoundError:
    print("Required input file not found.")


required_sales_columns = [
    "Order_ID",
    "Order_Date",
    "Region",
    "Country",
    "Product_Category",
    "Product_Name",
    "Sales_Representative",
    "Quantity",
    "Unit_Price",
    "Sales_Amount"
]

required_target_columns = [
    "Region",
    "Month",
    "Target_Sales",
    "Target_Quantity"
]

if all(column in sales_df.columns for column in required_sales_columns):
    print("Sales data columns are valid.")
else:
    print("Sales data columns are invalid.")

if all(column in targets_df.columns for column in required_target_columns):
    print("Sales target columns are valid.")
else:
    print("Sales target columns are invalid.")


print("\n  DATA CLEANING  ")

# Check missing values
print("\nMissing values in sales data:")
print(sales_df.isnull().sum())

print("\nMissing values in target data:")
print(targets_df.isnull().sum())

# Remove duplicate 
sales_df = sales_df.drop_duplicates()
targets_df = targets_df.drop_duplicates()

# Convert date column
sales_df["Order_Date"] = pd.to_datetime(
    sales_df["Order_Date"],
    errors="coerce"
)

# Convert numeric columns
numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Sales_Amount"
]

for column in numeric_columns:
    sales_df[column] = pd.to_numeric(
        sales_df[column],
        errors="coerce"
    )

targets_df["Target_Sales"] = pd.to_numeric(
    targets_df["Target_Sales"],
    errors="coerce"
)

targets_df["Target_Quantity"] = pd.to_numeric(
    targets_df["Target_Quantity"],
    errors="coerce"
)

# Remove rows where  values are missing
sales_df = sales_df.dropna(
    subset=[
        "Order_ID",
        "Order_Date",
        "Region",
        "Product_Name",
        "Quantity",
        "Sales_Amount"
    ]
)

targets_df = targets_df.dropna(
    subset=[
        "Region",
        "Month",
        "Target_Sales",
        "Target_Quantity"
    ]
)

# Standardize 
text_columns = [
    "Region",
    "Country",
    "Product_Category",
    "Product_Name",
    "Sales_Representative"
]

for column in text_columns:
    sales_df[column] = sales_df[column].str.strip().str.title()

targets_df["Region"] = (
    targets_df["Region"]
    .str.strip()
    .str.title()
)

targets_df["Month"] = (
    targets_df["Month"]
    .str.strip()
    .str.title()
)

print("\nData cleaning completed successfully.")
print("Total cleaned sales records:", len(sales_df))
print("Total target records:", len(targets_df))


print("\n  DATE FEATURES  ")

sales_df["Month"] = sales_df["Order_Date"].dt.strftime("%b")
sales_df["Month_Number"] = sales_df["Order_Date"].dt.month
sales_df["Quarter"] = sales_df["Order_Date"].dt.quarter
sales_df["Year"] = sales_df["Order_Date"].dt.year

print("Date-related columns created successfully.")

print("\nSample date information:")
print(
    sales_df[
        ["Order_Date", "Month", "Month_Number", "Quarter", "Year"]
    ].head()
)

print("\n  DASHBOARD KPIs  ")

total_revenue = sales_df["Sales_Amount"].sum()

total_orders = sales_df["Order_ID"].nunique()

total_quantity = sales_df["Quantity"].sum()

average_order_value = total_revenue / total_orders

regional_sales = sales_df.groupby("Region")["Sales_Amount"].sum()

best_region = regional_sales.idxmax()

representative_sales = sales_df.groupby(
    "Sales_Representative"
)["Sales_Amount"].sum()

top_representative = representative_sales.idxmax()

print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Total Quantity Sold:", total_quantity)
print("Average Order Value:", round(average_order_value, 2))
print("Best Performing Region:", best_region)
print("Top Sales Representative:", top_representative)


print("\n  TARGET ACHIEVEMENT ANALYSIS  ")

monthly_region_sales = sales_df.groupby(
    ["Region", "Month"]
).agg(
    Actual_Sales=("Sales_Amount", "sum"),
    Actual_Quantity=("Quantity", "sum")
).reset_index()

target_analysis = pd.merge(
    monthly_region_sales,
    targets_df,
    on=["Region", "Month"],
    how="left"
)

target_analysis["Achievement_Percentage"] = (
    target_analysis["Actual_Sales"]
    / target_analysis["Target_Sales"]
) * 100

target_analysis["Sales_Variance"] = (
    target_analysis["Actual_Sales"]
    - target_analysis["Target_Sales"]
)

target_analysis["Quantity_Achievement_Percentage"] = (
    target_analysis["Actual_Quantity"]
    / target_analysis["Target_Quantity"]
) * 100

target_analysis["Status"] = "Under Target"

target_analysis.loc[
    target_analysis["Achievement_Percentage"] >= 100,
    "Status"
] = "Target Achieved"

overall_target_sales = target_analysis["Target_Sales"].sum()

overall_target_achievement = (
    total_revenue / overall_target_sales
) * 100

print(
    "Overall Target Achievement:",
    round(overall_target_achievement, 2),
    "%"
)

print("\nRegional Monthly Target Performance:")
print(target_analysis.head(10))


print("\n  REGIONAL ANALYSIS  ")

regional_analysis = sales_df.groupby("Region").agg(
    Total_Sales=("Sales_Amount", "sum"),
    Total_Orders=("Order_ID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Average_Sales=("Sales_Amount", "mean"),
    Maximum_Sale=("Sales_Amount", "max"),
    Minimum_Sale=("Sales_Amount", "min")
).reset_index()

regional_analysis["Contribution_Percentage"] = (
    regional_analysis["Total_Sales"]
    / total_revenue
) * 100

regional_analysis = regional_analysis.sort_values(
    by="Total_Sales",
    ascending=False
)

print(regional_analysis)


print("\n  REGION-WISE MONTHLY GROWTH  ")

regional_monthly_sales = sales_df.groupby(
    ["Region", "Month_Number", "Month"]
)["Sales_Amount"].sum().reset_index()

regional_monthly_sales = regional_monthly_sales.sort_values(
    by=["Region", "Month_Number"]
)

regional_monthly_sales["Growth_Percentage"] = (
    regional_monthly_sales.groupby("Region")["Sales_Amount"]
    .pct_change() * 100
)

print(regional_monthly_sales.head(15))


print("\n  PRODUCT ANALYSIS  ")

product_analysis = sales_df.groupby("Product_Name").agg(
    Total_Sales=("Sales_Amount", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Total_Orders=("Order_ID", "nunique")
).reset_index()

product_analysis["Contribution_Percentage"] = (
    product_analysis["Total_Sales"]
    / total_revenue
) * 100

product_analysis = product_analysis.sort_values(
    by="Total_Sales",
    ascending=False
)

print("\nProduct Performance:")
print(product_analysis)


category_analysis = sales_df.groupby("Product_Category").agg(
    Total_Sales=("Sales_Amount", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Total_Orders=("Order_ID", "nunique")
).reset_index()

category_analysis["Contribution_Percentage"] = (
    category_analysis["Total_Sales"]
    / total_revenue
) * 100

category_analysis = category_analysis.sort_values(
    by="Total_Sales",
    ascending=False
)
print("\nProduct Category Performance:")
print(category_analysis)


top_products = product_analysis.head(10)
print("\nTop 10 Products by Revenue:")
print(top_products)


# =====
# SALES REPRESENTATIVE PERFORMANCE ANALYSIS
# =====
print("\n  SALES REPRESENTATIVE ANALYSIS  ")

representative_analysis = sales_df.groupby(
    "Sales_Representative"
).agg(
    Total_Sales=("Sales_Amount", "sum"),
    Total_Orders=("Order_ID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Average_Sales=("Sales_Amount", "mean")
).reset_index()

representative_analysis = representative_analysis.sort_values(
    by="Total_Sales",
    ascending=False
)

representative_analysis["Rank"] = range(
    1,
    len(representative_analysis) + 1
)

print("\nSales Representative Performance:")
print(representative_analysis)

print(
    "\nTop Sales Representative:",
    representative_analysis.iloc[0]["Sales_Representative"]
)


# =====
# TIME-BASED ANALYSIS
# =====
print("\n===== TIME-BASED SALES ANALYSIS =====")


daily_sales = sales_df.groupby(
    "Order_Date"
)["Sales_Amount"].sum().reset_index()

print("\nDaily Sales:")
print(daily_sales.head(10))


# Monthly Sales
monthly_sales = sales_df.groupby(
    ["Month_Number", "Month"]
)["Sales_Amount"].sum().reset_index()

monthly_sales = monthly_sales.sort_values(
    by="Month_Number"
)

print("\nMonthly Sales:")
print(monthly_sales)


# Quarterly Sales
quarterly_sales = sales_df.groupby(
    "Quarter"
)["Sales_Amount"].sum().reset_index()

print("\nQuarterly Sales:")
print(quarterly_sales)


# Yearly Sales
yearly_sales = sales_df.groupby(
    "Year"
)["Sales_Amount"].sum().reset_index()

print("\nYearly Sales:")
print(yearly_sales)


# Year-to-Date Sales
monthly_sales["YTD_Sales"] = (
    monthly_sales["Sales_Amount"].cumsum()
)

print("\nYear-to-Date Sales:")
print(
    monthly_sales[
        ["Month", "Sales_Amount", "YTD_Sales"]
    ]
)


# ======
# SAVE CLEANED DATA
# ======
print("\n  SAVING CLEANED DATA  ")

import os

if not os.path.exists("output"):
    os.mkdir("output")

sales_df.to_csv(
    "output/cleaned_sales_data.csv",
    index=False
)

print("Cleaned sales data saved successfully.")


# =======
# VISUALIZATION
# ========

def create_charts():

    print("\n===== CREATING CHARTS =====")

    
    #  LINE CHART - MONTHLY SALES 
    

    plt.figure(figsize=(10, 6))

    plt.plot(
        monthly_sales["Month"],
        monthly_sales["Sales_Amount"],
        marker="o"
    )

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount")
    plt.grid()

    plt.tight_layout()

    plt.savefig(
        "output/monthly_sales_trend.png"
    )

    plt.close()

    print("Monthly sales trend chart created.")


    
    #  BAR CHART - REGIONAL SALE
    
    plt.figure(figsize=(8, 6))

    plt.bar(
        regional_analysis["Region"],
        regional_analysis["Total_Sales"]
    )

    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")

    plt.tight_layout()

    plt.savefig(
        "output/regional_sales.png"
    )

    plt.close()

    print("Regional sales chart created.")


    #  PIE CHART - CATEGORY 
    

    plt.figure(figsize=(8, 8))

    plt.pie(
        category_analysis["Total_Sales"],
        labels=category_analysis["Product_Category"],
        autopct="%1.1f%%"
    )

    plt.title(
        "Sales Contribution by Product Category"
    )

    plt.tight_layout()

    plt.savefig(
        "output/category_sales.png"
    )

    plt.close()

    print("Category sales chart created.")


    
    # HORIZONTAL BAR CHART - TOP PRODUCTS
    

    plt.figure(figsize=(10, 6))

    plt.barh(
        top_products["Product_Name"],
        top_products["Total_Sales"]
    )

    plt.title("Top Products by Revenue")
    plt.xlabel("Total Sales")
    plt.ylabel("Product")

    plt.tight_layout()

    plt.savefig(
        "output/top_products.png"
    )

    plt.close()

    print("Top products chart created.")


    
    # STACKED BAR CHART
    # REGION-WISE CATEGORY SALES
    

    region_category_sales = sales_df.pivot_table(
        values="Sales_Amount",
        index="Region",
        columns="Product_Category",
        aggfunc="sum",
        fill_value=0
    )

    region_category_sales.plot(
        kind="bar",
        stacked=True,
        figsize=(10, 6)
    )

    plt.title(
        "Region-wise Category Sales Distribution"
    )

    plt.xlabel("Region")
    plt.ylabel("Sales Amount")

    plt.tight_layout()

    plt.savefig(
        "output/region_category_sales.png"
    )

    plt.close()

    print(
        "Region-wise category sales chart created."
    )


   
    # AREA CHART - REVENUE TREND

    plt.figure(figsize=(10, 6))

    plt.fill_between(
        monthly_sales["Month"],
        monthly_sales["Sales_Amount"],
        alpha=0.5
    )

    plt.plot(
        monthly_sales["Month"],
        monthly_sales["Sales_Amount"],
        marker="o"
    )

    plt.title("Revenue Trend Over Time")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount")

    plt.tight_layout()

    plt.savefig(
        "output/revenue_trend.png"
    )

    plt.close()

    print("Revenue trend chart created.")

    print(
        "\nAll charts saved successfully in output folder."
    )


# ===
# DASHBOARD SUMMARY FUNCTION
# ===

def display_dashboard():

    
    print(" SALES DASHBOARD KPIs ")
    

    print(
        "Total Revenue:",
        round(total_revenue, 2)
    )

    print(
        "Total Orders:",
        total_orders
    )

    print(
        "Total Quantity Sold:",
        total_quantity
    )

    print(
        "Average Order Value:",
        round(average_order_value, 2)
    )

    print(
        "Overall Target Achievement:",
        round(overall_target_achievement, 2),
        "%"
    )

    print(
        "Best Performing Region:",
        best_region
    )

    print(
        "Top Sales Representative:",
        top_representative
    )


# ======
# FILTERED DATA SUMMARY FUNCTION
# ======

def display_filtered_summary(filtered_df):

    if filtered_df.empty:

        print("\nNo sales records found.")

    else:

        filtered_revenue = (
            filtered_df["Sales_Amount"].sum()
        )

        filtered_orders = (
            filtered_df["Order_ID"].nunique()
        )

        filtered_quantity = (
            filtered_df["Quantity"].sum()
        )

        filtered_average = (
            filtered_revenue
            / filtered_orders
        )

        print("\n  FILTERED SALES SUMMARY  ")

        print(
            "Total Revenue:",
            round(filtered_revenue, 2)
        )

        print(
            "Total Orders:",
            filtered_orders
        )

        print(
            "Total Quantity:",
            filtered_quantity
        )

        print(
            "Average Order Value:",
            round(filtered_average, 2)
        )

        print("\nFiltered Records:")

        print(
            filtered_df[
                [
                    "Order_ID",
                    "Order_Date",
                    "Region",
                    "Country",
                    "Product_Category",
                    "Product_Name",
                    "Sales_Representative",
                    "Quantity",
                    "Sales_Amount"
                ]
            ].head(20)
        )


# ======
# INTERACTIVE FILTERS
# ======

def filter_by_region():

    print("\nAvailable Regions:")

    print(
        sales_df["Region"]
        .drop_duplicates()
        .tolist()
    )

    region = input(
        "Enter Region: "
    ).strip().title()

    filtered_df = sales_df[
        sales_df["Region"] == region
    ]

    display_filtered_summary(filtered_df)


def filter_by_country():

    print("\nAvailable Countries:")

    print(
        sales_df["Country"]
        .drop_duplicates()
        .tolist()
    )

    country = input(
        "Enter Country: "
    ).strip().title()

    filtered_df = sales_df[
        sales_df["Country"] == country
    ]

    display_filtered_summary(filtered_df)


def filter_by_category():

    print("\nAvailable Product Categories:")

    print(
        sales_df["Product_Category"]
        .drop_duplicates()
        .tolist()
    )

    category = input(
        "Enter Product Category: "
    ).strip().title()

    filtered_df = sales_df[
        sales_df["Product_Category"]
        == category
    ]

    display_filtered_summary(filtered_df)


def filter_by_product():

    print("\nAvailable Products:")

    print(
        sales_df["Product_Name"]
        .drop_duplicates()
        .tolist()
    )

    product = input(
        "Enter Product Name: "
    ).strip().title()

    filtered_df = sales_df[
        sales_df["Product_Name"]
        == product
    ]

    display_filtered_summary(filtered_df)


def filter_by_representative():

    print("\nAvailable Sales Representatives:")

    print(
        sales_df["Sales_Representative"]
        .drop_duplicates()
        .tolist()
    )

    representative = input(
        "Enter Sales Representative: "
    ).strip().title()

    filtered_df = sales_df[
        sales_df["Sales_Representative"]
        == representative
    ]

    display_filtered_summary(filtered_df)


def filter_by_date():

    try:

        start_date = input(
            "Enter Start Date (YYYY-MM-DD): "
        )

        end_date = input(
            "Enter End Date (YYYY-MM-DD): "
        )

        start_date = pd.to_datetime(
            start_date
        )

        end_date = pd.to_datetime(
            end_date
        )

        filtered_df = sales_df[
            (
                sales_df["Order_Date"]
                >= start_date
            )
            &
            (
                sales_df["Order_Date"]
                <= end_date
            )
        ]

        display_filtered_summary(filtered_df)

    except ValueError:

        print(
            "Invalid date format. "
            "Please use YYYY-MM-DD."
        )


# =======
# CREATE CHART FILES
# =======

create_charts()


# =======
# DASHBOARD MENU
# ========

while True:

    
    print("  SALES ANALYSIS DASHBOARD  ")
    

    print("1. View Dashboard KPIs")
    print("2. Filter by Region")
    print("3. Filter by Country")
    print("4. Filter by Product Category")
    print("5. Filter by Product")
    print("6. Filter by Sales Representative")
    print("7. Filter by Date Range")
    print("8. View Regional Analysis")
    print("9. View Product Analysis")
    print("10. View Representative Analysis")
    print("11. View Monthly Sales")
    print("12. View Quarterly Sales")
    print("13. View Target Analysis")
    print("14. Generate Charts")
    print("15. Exit")

    choice = input(
        "\nEnter your choice: "
    )


    if choice == "1":

        display_dashboard()


    elif choice == "2":

        filter_by_region()


    elif choice == "3":

        filter_by_country()


    elif choice == "4":

        filter_by_category()


    elif choice == "5":

        filter_by_product()


    elif choice == "6":

        filter_by_representative()


    elif choice == "7":

        filter_by_date()


    elif choice == "8":

        print(
            "\n  REGIONAL ANALYSIS  "
        )

        print(regional_analysis)


    elif choice == "9":

        print(
            "\n  PRODUCT ANALYSIS  "
        )

        print(product_analysis)


    elif choice == "10":

        print(
            "\n REPRESENTATIVE ANALYSIS  "
        )

        print(representative_analysis)


    elif choice == "11":

        print(
            "\n  MONTHLY SALES  "
        )

        print(monthly_sales)


    elif choice == "12":

        print(
            "\n  QUARTERLY SALES  "
        )

        print(quarterly_sales)


    elif choice == "13":

        print(
            "\n TARGET ANALYSIS  "
        )

        print(target_analysis)


    elif choice == "14":

        create_charts()


    elif choice == "15":

        print(
            "\nSales Analysis Dashboard closed."
        )

        break


    else:

        print(
            "\nInvalid choice. Please try again."
        )