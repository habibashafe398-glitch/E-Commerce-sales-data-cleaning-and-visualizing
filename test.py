import pandas as pd

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("ecommerce_sales_34500.csv")

print("===== DATASET INFORMATION =====")

print("First 5 rows:")
print(df.head())

print()
print("Shape:")
print(df.shape)

print()
print("Columns:")
print(df.columns)

print()
print("Data types:")
print(df.dtypes)

print()
print("Missing values:")
print(df.isnull().sum())

print()
print("Duplicate rows:")
print(df.duplicated().sum())

print()
print("Statistics:")
print(df.describe())


# ==========================================
# 2. CHECK DATA VALUES
# ==========================================

print()
print("===== DATA CHECK =====")

print("Categories:")
print(df["category"].unique())

print()
print("Payment methods:")
print(df["payment_method"].unique())

print()
print("Regions:")
print(df["region"].unique())

print()
print("Returned:")
print(df["returned"].unique())

print()
print("Gender:")
print(df["customer_gender"].unique())

print()
print("Price range:")
print(df["price"].min(), df["price"].max())

print()
print("Discount range:")
print(df["discount"].min(), df["discount"].max())

print()
print("Quantity range:")
print(df["quantity"].min(), df["quantity"].max())

print()
print("Delivery time range:")
print(df["delivery_time_days"].min(), df["delivery_time_days"].max())

print()
print("Age range:")
print(df["customer_age"].min(), df["customer_age"].max())

print()
print("Shipping cost range:")
print(df["shipping_cost"].min(), df["shipping_cost"].max())


# ==========================================
# 3. CLEAN DATA
# ==========================================

print()
print("===== CLEANING DATA =====")

# remove extra spaces from text columns
df["category"] = df["category"].str.strip()
df["payment_method"] = df["payment_method"].str.strip()
df["region"] = df["region"].str.strip()
df["returned"] = df["returned"].str.strip()
df["customer_gender"] = df["customer_gender"].str.strip()

# convert order_date to date
df["order_date"] = pd.to_datetime(df["order_date"])

print("Cleaning completed!")


# ==========================================
# 4. VERIFY CLEANING
# ==========================================

print()
print("===== VERIFY CLEANING =====")

print("Missing values:")
print(df.isnull().sum())

print()
print("Duplicate rows:")
print(df.duplicated().sum())

print()
print("Order date type:")
print(df["order_date"].dtype)

print()
print("Invalid dates:")
print(df["order_date"].isnull().sum())


# ==========================================
# 5. SAVE CLEANED DATA
# ==========================================

df["month"] = df["order_date"].dt.to_period("M")

df.to_csv("ecommerce_sales_cleaned.csv", index=False)

print()
print("Cleaned dataset saved successfully!")

# ==========================================
# 6. BASIC KPIs
# ==========================================

print()
print("===== BASIC ANALYSIS =====")

print("Total orders:")
print(len(df))

print()
print("Total sales:")
print(df["total_amount"].sum())

print()
print("Average order value:")
print(df["total_amount"].mean())

print()
print("Total quantity sold:")
print(df["quantity"].sum())

print()
print("Average profit margin:")
print(df["profit_margin"].mean())

print()
print("Total shipping cost:")
print(df["shipping_cost"].sum())


# ==========================================
# 7. SALES BY CATEGORY
# ==========================================

print()
print("===== SALES BY CATEGORY =====")

category_sales = df.groupby("category")["total_amount"].sum()
print(category_sales)

print()
print("Average order value by category:")

category_average = df.groupby("category")["total_amount"].mean()
print(category_average)

print()
print("Average profit margin by category:")

category_profit = df.groupby("category")["profit_margin"].mean()
print(category_profit)


# ==========================================
# 8. SALES BY REGION
# ==========================================

print()
print("===== SALES BY REGION =====")

region_sales = df.groupby("region")["total_amount"].sum()
print(region_sales)

print()
print("Orders by region:")

region_orders = df.groupby("region")["order_id"].count()
print(region_orders)

print()
print("Average order value by region:")

region_average = df.groupby("region")["total_amount"].mean()
print(region_average)


# ==========================================
# 9. PAYMENT METHODS
# ==========================================

print()
print("===== PAYMENT METHODS =====")

payment_orders = df["payment_method"].value_counts()
print(payment_orders)

print()
print("Sales by payment method:")

payment_sales = df.groupby("payment_method")["total_amount"].sum()
print(payment_sales)


# ==========================================
# 10. RETURN ANALYSIS
# ==========================================

print()
print("===== RETURNS =====")

return_count = df["returned"].value_counts()
print(return_count)

returned_orders = (df["returned"] == "Yes").sum()

total_orders = len(df)

return_rate = (returned_orders / total_orders) * 100

print()
print("Return rate:")
print(return_rate)


# ==========================================
# 11. RETURNS BY CATEGORY
# ==========================================

print()
print("===== RETURN RATE BY CATEGORY =====")

category_return_rate = df.groupby("category")["returned"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print(category_return_rate)


# ==========================================
# 12. DISCOUNT ANALYSIS
# ==========================================

print()
print("===== DISCOUNT ANALYSIS =====")

print("Discount levels:")
print(df["discount"].value_counts().sort_index())

print()
print("Average order value by discount:")

discount_sales = df.groupby("discount")["total_amount"].mean()
print(discount_sales)

print()
print("Total sales by discount:")

discount_total_sales = df.groupby("discount")["total_amount"].sum()
print(discount_total_sales)


# ==========================================
# 13. QUANTITY BY CATEGORY
# ==========================================

print()
print("===== QUANTITY BY CATEGORY =====")

category_quantity = df.groupby("category")["quantity"].sum()
print(category_quantity)

print()
print("Average quantity per order by category:")

category_avg_quantity = df.groupby("category")["quantity"].mean()
print(category_avg_quantity)


# ==========================================
# 14. DELIVERY TIME AND RETURNS
# ==========================================

print()
print("===== DELIVERY TIME AND RETURNS =====")

delivery_return = df.groupby("returned")["delivery_time_days"].mean()
print(delivery_return)

print()
print("Average delivery time by category:")

delivery_category = df.groupby("category")["delivery_time_days"].mean()
print(delivery_category)


# ==========================================
# 15. PROFIT MARGIN BY CATEGORY
# ==========================================

print()
print("===== PROFIT MARGIN BY CATEGORY =====")

profit_category = df.groupby("category")["profit_margin"].mean()

print(profit_category.sort_values(ascending=False))


# ==========================================
# 16. MONTHLY SALES
# ==========================================

df["month"] = df["order_date"].dt.to_period("M")

print()
print("===== MONTHLY SALES =====")

monthly_sales = df.groupby("month")["total_amount"].sum()
print(monthly_sales)

print()
print("Monthly orders:")

monthly_orders = df.groupby("month")["order_id"].count()
print(monthly_orders)