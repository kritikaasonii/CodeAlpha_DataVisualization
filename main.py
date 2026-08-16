import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")

# Check the dataset
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())


# -------------------------------
# CHART 1: SALES BY REGION
# -------------------------------

region_sales = df.groupby("Region")["Sales_Amount"].sum()

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("charts/sales_by_region.png")
plt.show()
plt.close()


# -------------------------------
# CHART 2: SALES BY SALES REPRESENTATIVE
# -------------------------------

rep_sales = df.groupby("Sales_Rep")["Sales_Amount"].sum()

plt.figure(figsize=(8, 5))
rep_sales.plot(kind="bar")

plt.title("Total Sales by Sales Representative")
plt.xlabel("Sales Representative")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("charts/sales_by_sales_rep.png")
plt.show()
plt.close()


# -------------------------------
# CHART 3: SALES BY PRODUCT CATEGORY
# -------------------------------

category_sales = df.groupby("Product_Category")["Sales_Amount"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")

plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
plt.show()
plt.close()


# -------------------------------
# KEY FINDINGS
# -------------------------------

print("\n===== KEY FINDINGS =====")

print("\nSales by Region:")
print(region_sales.sort_values(ascending=False))

print("\nSales by Sales Representative:")
print(rep_sales.sort_values(ascending=False))

print("\nSales by Product Category:")
print(category_sales.sort_values(ascending=False))

# -------------------------------
# CHART 4: MONTHLY SALES TREND
# -------------------------------

df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

df_2023 = df[df["Sale_Date"].dt.year == 2023]

monthly_sales = df_2023.groupby(
    df_2023["Sale_Date"].dt.to_period("M")
)["Sales_Amount"].sum()

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("charts/monthly_sales_trend.png")

plt.show()
plt.close()