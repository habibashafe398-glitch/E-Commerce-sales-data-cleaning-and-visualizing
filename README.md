# E-Commerce-sales-data-cleaning-and-visualizing

## Project Overview

This project is about analyzing an e-commerce sales dataset containing 34,500 transaction records.

The main goal of the project is to understand sales performance, customer behavior, product performance, profit, returns, delivery time, and sales trends.

Python and Pandas were used for cleaning and preparing the data. Power BI was then used to analyze the data and create the dashboard.

## Tools Used

* Python
* Pandas
* Power BI
* CSV

## Dataset

The dataset contains information about e-commerce transactions, including:

* Order ID
* Customer ID
* Product ID
* Category
* Price
* Discount
* Quantity
* Payment Method
* Order Date
* Delivery Time
* Region
* Return Status
* Total Amount
* Shipping Cost
* Profit Margin
* Customer Age
* Customer Gender

## Data Cleaning

The data was cleaned and prepared using Python and Pandas.

The main steps were:

* Checking for missing values
* Checking for duplicate rows
* Converting the order date to datetime format
* Making sure numeric columns had the correct data types
* Calculating the total amount
* Creating a month column from the order date
* Grouping customer ages into age groups
* Checking delivery time values
* Checking negative profit values

No missing values or duplicate rows were found in the dataset.

## Business Questions

The project was used to answer the following questions:

1. Which product category has the highest sales?
2. Which region has the highest sales?
3. Which payment method is used the most?
4. What is the overall return rate?
5. Which category has the highest return rate?
6. How does discount affect sales performance?
7. Which category has the highest quantity sold?
8. Is there a difference in delivery time between returned and non-returned orders?
9. Which category generates the highest profit?
10. How do sales and order volume change over time?

## Main KPIs

* Total Sales Revenue: $5,865,293.05
* Total Net Profit: $970,019.41
* Total Orders: 34,500
* Average Delivery Time: 4.81 days
* Overall Return Rate: 5.52%

## Key Findings

Electronics had the highest sales, with approximately $3.32M in revenue, and also generated the highest profit at approximately $344.3K. Its return rate was 7.30%.

Grocery generated approximately $82K in sales but had a net profit loss of $9,187.96. One of the main factors was the shipping cost compared with the low order values.

Fashion generated approximately $128.8K in profit but had the highest return rate at 8.28%.

Sales were relatively balanced between the regions. South had the highest sales at approximately $1.30M, while Central had the lowest at approximately $940.5K.

## Recommendations

Based on the analysis, some recommendations were made:

* Review shipping costs for Grocery products.
* Consider a minimum order amount for low-margin products.
* Improve sizing information and product descriptions for Fashion products.
* Improve quality checks for categories with higher return rates.
* Focus more on categories with higher profit margins.
* Work on reducing delivery times.

## Power BI Dashboard

The cleaned data was imported into Power BI to create an interactive dashboard.

The dashboard includes analysis of:

* Sales
* Profit
* Categories
* Regions
* Payment methods
* Returns
* Discounts
* Delivery time
* Monthly sales
* Customer age groups

## Project Structure

```text
E-Commerce-Sales-Analysis/
│
├── data/
│   ├── ecommerce_sales_34500.csv
│   └── cleaned_ecommerce_sales.csv
│
├── python/
│   └── data_cleaning.py
│
├── powerbi/
│   └── ecommerce_sales_dashboard.pbix
│
├── screenshots/
│   └── dashboard.png
│
└── README.md
```

## Conclusion

This project shows the process of taking raw e-commerce data, cleaning and preparing it using Python and Pandas, and then using Power BI to analyze the data and create a dashboard.

The analysis helped identify differences in sales, profit, returns, delivery performance, and category performance, and showed some areas that could be improved.
