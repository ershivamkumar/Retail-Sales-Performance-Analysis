from pathlib import Path

import pandas as pd


# ============================================================
# 1. LOAD DATA
# ============================================================

# The script is stored inside the "python" folder.
# The dataset is stored inside the "data" folder.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "retail_sales.csv"
CLEANED_DATA_PATH = PROJECT_ROOT / "data" / "retail_sales_cleaned.csv"

data = pd.read_csv(DATA_PATH)

print("=" * 60)
print("RETAIL SALES PERFORMANCE ANALYSIS")
print("=" * 60)

print(f"\nDataset shape: {data.shape}")
print(f"Rows: {len(data):,}")
print(f"Columns: {len(data.columns)}")


# ============================================================
# 2. DATA CLEANING & VALIDATION
# ============================================================

# Convert date columns from text to datetime.
data["Order_Date"] = pd.to_datetime(data["Order_Date"])
data["Ship_Date"] = pd.to_datetime(data["Ship_Date"])

print("\n--- DATA QUALITY CHECK ---")

print("\nMissing values:")
print(data.isnull().sum())

print(f"\nDuplicate rows: {data.duplicated().sum():,}")

print("\nData types:")
print(data.dtypes)

print("\nNumeric ranges:")
print(f"Quantity : {data['Quantity'].min()} to {data['Quantity'].max()}")
print(f"Discount : {data['Discount'].min()} to {data['Discount'].max()}")
print(f"Sales    : {data['Sales'].min():,.4f} to {data['Sales'].max():,.4f}")
print(f"Profit   : {data['Profit'].min():,.4f} to {data['Profit'].max():,.4f}")


# ============================================================
# 3. OVERALL KPIs
# ============================================================

total_sales = data["Sales"].sum()
total_profit = data["Profit"].sum()
total_quantity = data["Quantity"].sum()
total_orders = data["Order_ID"].nunique()
average_discount = data["Discount"].mean()

overall_kpis = pd.DataFrame(
    {
        "Metric": [
            "Total Sales",
            "Total Profit",
            "Total Quantity",
            "Total Orders",
            "Average Discount",
        ],
        "Value": [
            total_sales,
            total_profit,
            total_quantity,
            total_orders,
            average_discount,
        ],
    }
)

print("\n--- OVERALL KPIs ---")
print(overall_kpis.to_string(index=False))


# ============================================================
# 4. CATEGORY ANALYSIS
# ============================================================

category_analysis = (
    data.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Total_Orders=("Order_ID", "nunique"),
    )
)

category_analysis["Profit_Margin_%"] = (
    category_analysis["Total_Profit"]
    / category_analysis["Total_Sales"]
) * 100

category_analysis = category_analysis.sort_values(
    "Total_Sales", ascending=False
)

print("\n--- CATEGORY ANALYSIS ---")
print(category_analysis.to_string())


# ============================================================
# 5. SUBCATEGORY ANALYSIS
# ============================================================

subcategory_analysis = (
    data.groupby("Sub_Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Total_Orders=("Order_ID", "nunique"),
    )
)

subcategory_analysis["Profit_Margin_%"] = (
    subcategory_analysis["Total_Profit"]
    / subcategory_analysis["Total_Sales"]
) * 100

subcategory_analysis = subcategory_analysis.sort_values(
    "Total_Sales", ascending=False
)

print("\n--- SUBCATEGORY ANALYSIS ---")
print(subcategory_analysis.to_string())


# ============================================================
# 6. DISCOUNT ANALYSIS
# ============================================================

discount_analysis = (
    data.groupby("Discount")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Profit=("Profit", "mean"),
        Total_Quantity=("Quantity", "sum"),
    )
    .sort_index()
)

discount_analysis["Profit_Margin_%"] = (
    discount_analysis["Total_Profit"]
    / discount_analysis["Total_Sales"]
) * 100

print("\n--- DISCOUNT ANALYSIS ---")
print(discount_analysis.to_string())


# ============================================================
# 7. CATEGORY + DISCOUNT ANALYSIS
# ============================================================

category_discount = (
    data.groupby(["Category", "Discount"])
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum"),
    )
    .reset_index()
)

category_discount["Profit_Margin_%"] = (
    category_discount["Total_Profit"]
    / category_discount["Total_Sales"]
) * 100

print("\n--- CATEGORY + DISCOUNT ANALYSIS ---")
print(category_discount.to_string(index=False))


# ============================================================
# 8. SUBCATEGORY + DISCOUNT ANALYSIS
# ============================================================

subcategory_discount = (
    data.groupby(["Sub_Category", "Discount"])
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum"),
    )
    .reset_index()
)

subcategory_discount["Profit_Margin_%"] = (
    subcategory_discount["Total_Profit"]
    / subcategory_discount["Total_Sales"]
) * 100

loss_making = (
    subcategory_discount[subcategory_discount["Total_Profit"] < 0]
    .sort_values("Total_Profit")
)

print("\n--- LOSS-MAKING SUBCATEGORY + DISCOUNT COMBINATIONS ---")
print(loss_making.to_string(index=False))


# ============================================================
# 9. REGIONAL ANALYSIS
# ============================================================

region_analysis = (
    data.groupby("Region")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Total_Orders=("Order_ID", "nunique"),
    )
)

region_analysis["Profit_Margin_%"] = (
    region_analysis["Total_Profit"]
    / region_analysis["Total_Sales"]
) * 100

region_analysis = region_analysis.sort_values(
    "Total_Sales", ascending=False
)

print("\n--- REGIONAL ANALYSIS ---")
print(region_analysis.to_string())


# ============================================================
# 10. STATE ANALYSIS
# ============================================================

state_analysis = (
    data.groupby("State")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Total_Orders=("Order_ID", "nunique"),
    )
)

state_analysis["Profit_Margin_%"] = (
    state_analysis["Total_Profit"]
    / state_analysis["Total_Sales"]
) * 100

top_states_by_profit = state_analysis.sort_values(
    "Total_Profit", ascending=False
).head(10)

bottom_states_by_profit = state_analysis.sort_values(
    "Total_Profit", ascending=True
).head(10)

print("\n--- TOP 10 STATES BY PROFIT ---")
print(top_states_by_profit.to_string())

print("\n--- BOTTOM 10 STATES BY PROFIT ---")
print(bottom_states_by_profit.to_string())


# ============================================================
# 11. YEARLY ANALYSIS
# ============================================================

year_analysis = (
    data.groupby(data["Order_Date"].dt.year)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Total_Orders=("Order_ID", "nunique"),
    )
)

year_analysis["Profit_Margin_%"] = (
    year_analysis["Total_Profit"]
    / year_analysis["Total_Sales"]
) * 100

print("\n--- YEARLY ANALYSIS ---")
print(year_analysis.to_string())


# ============================================================
# 12. MONTHLY ANALYSIS
# ============================================================

monthly_analysis = (
    data.groupby(data["Order_Date"].dt.to_period("M"))
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Total_Orders=("Order_ID", "nunique"),
    )
)

monthly_analysis["Profit_Margin_%"] = (
    monthly_analysis["Total_Profit"]
    / monthly_analysis["Total_Sales"]
) * 100

print("\n--- MONTHLY ANALYSIS ---")
print(monthly_analysis.to_string())


# ============================================================
# 13. SAVE CLEANED DATASET
# ============================================================

data.to_csv(CLEANED_DATA_PATH, index=False)

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)
print(f"Cleaned dataset saved to:\n{CLEANED_DATA_PATH}")
