# Abhishek_jadhav_69137
# Assignment_8 

import pandas as pd;
import matplotlib.pyplot as plt;


# Load sales data and target data from CSV 
sales_df = pd.read_csv("sales_data.csv");
target_df = pd.read_excel("sales_targets.xlsx");


sales_df.drop_duplicates(inplace=True);

sales_df["Sales_Amount"] = pd.to_numeric(
    sales_df["Sales_Amount"],
    errors="coerce"
);

sales_df.dropna(inplace=True);

print("Cleaned Sales Data:");
print(sales_df);


# Total Sale
total_sales = sales_df["Sales_Amount"].sum();

print("\nTotal Sales:");
print(total_sales);

# Average Sale
average_sales = sales_df["Sales_Amount"].mean();

print("\nAverage Sales:");
print(average_sales);

# Sale by Region
region_sales = sales_df.groupby(
    "Region"
)["Sales_Amount"].sum();

print("\nSales by Region:");
print(region_sales);

# Sale Summary by Region
region_summary = sales_df.groupby(
    "Region"
)["Sales_Amount"].agg(
    ["sum", "mean", "max", "min"]
);

print("\nRegion Sales Summary:");
print(region_summary);


# Sale by Product Category
category_sales = sales_df.groupby(
    "Product_Category"
)["Sales_Amount"].sum();

print("\nSales by Product Category:");
print(category_sales);

# Sale by Product
product_sales = sales_df.groupby(
    "Product_Name"
)["Sales_Amount"].sum();

print("\nSales by Product:");
print(product_sales);


# Sale by Sales Representative
representative_sales = sales_df.groupby(
    "Sales_Representative"
)["Sales_Amount"].sum();

print("\nSales by Sales Representative:");
print(representative_sales);


# sale data for East Region
east_sales = sales_df[
    sales_df["Region"] == "East"
];

print("\nEast Region Sales Data:");
print(east_sales);

# Calc Actual Sale by Region
actual_sales = sales_df.groupby(
    "Region"
)["Sales_Amount"].sum().reset_index();


# Calc Total Target Sale by Region
regional_target = target_df.groupby(
    "Region"
)["Target_Sales"].sum().reset_index();


# combine Actual Sale with Target Sale
performance = pd.merge(
    actual_sales,
    regional_target,
    on="Region"
);


# Calc Achievement Percentage
performance["Achievement %"] = (
    performance["Sales_Amount"] /
    performance["Target_Sales"]
) * 100;

print("\nSales Target Performance:");
print(performance);

# Line Chart 
category_sales.plot(
    kind="line",
    marker="o",
    figsize=(10, 5)
);

plt.title("Product Category Sales");
plt.xlabel("Product Category");
plt.ylabel("Sales");
plt.grid(True);
plt.show();


# Pie Chart
region_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7, 7)
);

plt.title("Regional Sales Contribution");
plt.ylabel("");
plt.show();