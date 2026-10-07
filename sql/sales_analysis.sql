USE retail_sales_db;


-- ============================================================
-- 1. OVERALL BUSINESS KPIs
-- ============================================================

SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM retail_sales;


-- ============================================================
-- 2. SALES & PROFIT BY CATEGORY
-- ============================================================

SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity
FROM retail_sales
GROUP BY Category
ORDER BY Total_Sales DESC;


-- ============================================================
-- 3. CATEGORY PROFIT MARGIN
-- ============================================================

SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin
FROM retail_sales
GROUP BY Category
ORDER BY Profit_Margin DESC;


-- ============================================================
-- 4. FURNITURE SUBCATEGORY PROFITABILITY
-- Used to investigate the profitability problem within Furniture.
-- ============================================================

SELECT
    Sub_Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin
FROM retail_sales
WHERE Category = 'Furniture'
GROUP BY Sub_Category
ORDER BY Total_Profit ASC;


-- ============================================================
-- 5. TABLES: DISCOUNT VS PROFITABILITY
-- ============================================================

SELECT
    Discount,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin
FROM retail_sales
WHERE Sub_Category = 'Tables'
GROUP BY Discount
ORDER BY Discount;


-- ============================================================
-- 6. REGIONAL PERFORMANCE
-- ============================================================

SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin
FROM retail_sales
GROUP BY Region
ORDER BY Total_Sales DESC;


-- ============================================================
-- 7. YEARLY SALES & PROFIT TREND
-- ============================================================

SELECT
    YEAR(Order_Date) AS Order_Year,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM retail_sales
GROUP BY YEAR(Order_Date)
ORDER BY Order_Year;


-- ============================================================
-- 8. TOP 10 PRODUCTS BY PROFIT
-- ============================================================

SELECT
    Product_Name,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM retail_sales
GROUP BY Product_Name
ORDER BY Total_Profit DESC
LIMIT 10;


-- ============================================================
-- 9. TOP 10 LOSS-MAKING PRODUCTS
-- ============================================================

SELECT
    Product_Name,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM retail_sales
GROUP BY Product_Name
HAVING SUM(Profit) < 0
ORDER BY Total_Profit ASC
LIMIT 10;


-- ============================================================
-- 10. OVERALL DISCOUNT VS PROFITABILITY
-- ============================================================

SELECT
    Discount,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin
FROM retail_sales
GROUP BY Discount
ORDER BY Discount;


-- ============================================================
-- 11. TOP 10 STATES BY PROFIT
-- ============================================================

SELECT
    State,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM retail_sales
GROUP BY State
ORDER BY Total_Profit DESC
LIMIT 10;


-- ============================================================
-- 12. BOTTOM 10 STATES BY PROFIT
-- ============================================================

SELECT
    State,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM retail_sales
GROUP BY State
ORDER BY Total_Profit ASC
LIMIT 10;


-- ============================================================
-- 13. SUBCATEGORY PROFITABILITY
-- ============================================================

SELECT
    Sub_Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin
FROM retail_sales
GROUP BY Sub_Category
ORDER BY Total_Profit DESC;


-- ============================================================
-- 14. CUSTOMER SEGMENT PERFORMANCE
-- ============================================================

SELECT
    Segment,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin
FROM retail_sales
GROUP BY Segment
ORDER BY Total_Sales DESC;


-- ============================================================
-- 15. SHIPPING MODE PERFORMANCE
-- ============================================================

SELECT
    Ship_Mode,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin
FROM retail_sales
GROUP BY Ship_Mode
ORDER BY Total_Orders DESC;


-- ============================================================
-- 16. MONTHLY SALES & PROFIT TREND
-- Used for the Power BI time-series dashboard.
-- ============================================================

SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS Month,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM retail_sales
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Month;
