# E-Commerce Sales & Customer Insights — Business Report

**Dataset:** Olist Brazilian E-Commerce Public Dataset  
**Tools:** Python, Pandas, SQL, DuckDB, Matplotlib, Power BI  
**Analysis Period:** 2016–2018

## 1. Executive Summary

This project analyzes 99,441 historical e-commerce orders to understand sales performance, customer distribution, product categories, and delivery efficiency.

The analysis combines Python-based data preparation, SQL queries, and an interactive Power BI dashboard to identify business patterns and opportunities.

## 2. Key Performance Indicators

| Metric | Result |
|---|---:|
| Total Orders | 99,441 |
| Delivered Orders | 96,478 |
| Delivered-Order Item Sales | R$13,221,498.11 |
| Average Item Sales per Delivered Order | R$137.04 |
| Late Deliveries | 6,534 |
| Late Delivery Rate | 6.77% |

*Sales values reflect listed product prices associated with delivered orders, excluding freight and refunds. Delivery performance was calculated using 96,470 delivered orders with valid actual and estimated delivery dates.*

## 3. Key Findings

### Sales Performance

November 2017 recorded the highest monthly order count, with 7,544 orders. It also recorded approximately R$987,765 in delivered-order item sales.

Sales increased substantially during 2017 and remained relatively strong through much of 2018. The dataset's limited coverage in later months should be considered before interpreting changes in performance.

### Customer Geography

São Paulo (SP) generated the highest number of orders, followed by Rio de Janeiro (RJ) and Minas Gerais (MG).

This suggests that Brazil's southeastern states are important markets within the dataset.

### Product Category Performance

The Power BI analysis identified Health & Beauty, Watches & Gifts, and Bed & Bath among the leading product categories by delivered-order item sales.

These categories may warrant further investigation into profitability, product availability, and customer demand.

### Delivery Performance

Among 96,470 delivered orders with valid delivery dates, 6,534 arrived after their estimated delivery dates.

This represents a late-delivery rate of approximately 6.77%.

## 4. Business Recommendations

1. **Investigate delivery delays:** Identify states, sellers, and shipping routes associated with late deliveries.
2. **Prioritize high-demand categories:** Evaluate stock availability and profitability in the leading product categories.
3. **Improve regional planning:** Analyze order demand and delivery performance in São Paulo, Rio de Janeiro, and Minas Gerais.
4. **Monitor monthly KPIs:** Track order counts, delivered-item sales, fulfillment performance, and category trends using Power BI.
5. **Investigate seasonal demand:** Examine the November 2017 sales peak to determine whether promotions or seasonal shopping contributed.

## 5. Conclusion

This project demonstrates an end-to-end data analytics workflow, including data exploration, initial cleaning, SQL analysis, data modeling, visualization, and business reporting.

The findings highlight opportunities to investigate delivery efficiency, improve inventory planning, and better understand customer demand.

**Limitations:** The analysis uses historical data and listed item prices rather than audited revenue or profit. Business recommendations require further validation before implementation.