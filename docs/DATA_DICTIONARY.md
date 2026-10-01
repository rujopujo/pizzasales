# Data Dictionary

This document provides schema specifications for the raw sales transaction dataset as well as the multidimensional Star Schema tables.

---

## 1. Raw Dataset (`data/pizza_sales.csv`)

| Column Name | Data Type | Nullable | Example | Description |
|---|---|---|---|---|
| `order_id` | `VARCHAR(16)` | No | `ORD-00001` | Unique order identifier. One order may span multiple pizza line items. |
| `order_date` | `DATE` | No | `2025-03-15` | Date when the order was placed (`YYYY-MM-DD`). |
| `order_time` | `TIME` | No | `19:24:10` | Timestamp when the order was entered (`HH:MM:SS`). |
| `pizza_category` | `VARCHAR(32)` | No | `Supreme` | Pizza category (`Classic`, `Veggie`, `Supreme`, `Chicken`). |
| `pizza_size` | `VARCHAR(8)` | No | `L` | Pizza size abbreviation (`S`, `M`, `L`, `XL`, `XXL`). |
| `pizza_name` | `VARCHAR(64)` | No | `Deluxe Supreme` | Commercial menu name of the pizza item. |
| `quantity` | `INT` | No | `2` | Number of identical pizzas ordered in this line item ($1 \le q \le 5$). |
| `unit_price` | `FLOAT` | No | `18.75` | Unit price per pizza in USD. |
| `total_price` | `FLOAT` | No | `37.50` | Line total (`quantity * unit_price`). |

---

## 2. Star Schema Data Warehouse Tables

### 2.1 Fact Table: `Fact_Sales`
- **Granularity**: One row per distinct sales order line item.
- **Estimated Row Count**: 3,000 rows.

| Column | Key Type | References | Data Type | Description |
|---|---|---|---|---|
| `sale_id` | Primary Key | — | `INT` | Auto-incrementing surrogate identifier. |
| `order_id` | Degenerate Dim | — | `VARCHAR(16)` | Grouping key representing customer order basket. |
| `date_key` | Foreign Key | `Dim_Date(date_key)` | `INT` | Date surrogate key in `YYYYMMDD` format. |
| `time_key` | Foreign Key | `Dim_Time(time_key)` | `INT` | Time surrogate key in `HHMMSS` format. |
| `pizza_key` | Foreign Key | `Dim_Pizza(pizza_key)` | `INT` | Surrogate key referencing pizza product catalog. |
| `quantity` | Measure | — | `INT` | Count of units purchased. |
| `unit_price` | Measure | — | `FLOAT` | Price per single unit. |
| `total_price` | Measure | — | `FLOAT` | Additive revenue measure ($quantity \times unit\_price$). |
| `margin_rate` | Measure | — | `FLOAT` | Synthetic profit margin percentage ($0.65 - 0.75$). |

---

### 2.2 Dimension Table: `Dim_Pizza`
- **Granularity**: Unique combination of Pizza Name, Category, and Size.

| Column | Key Type | Data Type | Description |
|---|---|---|---|
| `pizza_key` | Primary Key | `INT` | Product surrogate key. |
| `pizza_name` | Attribute | `VARCHAR(64)` | Specific pizza variety (e.g., Margherita, Pepperoni, BBQ Chicken). |
| `pizza_category` | Attribute | `VARCHAR(32)` | High-level menu category (Classic, Veggie, Supreme, Chicken). |
| `pizza_size` | Attribute | `VARCHAR(8)` | Size classification (S, M, L, XL, XXL). |

---

### 2.3 Dimension Table: `Dim_Time`
- **Granularity**: Distinct order timestamp down to the second.

| Column | Key Type | Data Type | Description |
|---|---|---|---|
| `time_key` | Primary Key | `INT` | Integer timestamp representation `HHMMSS`. |
| `order_time` | Attribute | `TIME` | Formatted `HH:MM:SS` string. |
| `hour` | Attribute | `INT` | 24-hour hour integer ($10 \le \text{hour} \le 23$). |
| `peak_period` | Attribute | `VARCHAR(16)` | `Lunch` (12–14), `Dinner` (19–22), or `Off-Peak`. |

---

### 2.4 Dimension Table: `Dim_Date`
- **Granularity**: Unique calendar day across the year 2025.

| Column | Key Type | Data Type | Description |
|---|---|---|---|
| `date_key` | Primary Key | `INT` | Integer date format `YYYYMMDD`. |
| `date` | Attribute | `DATE` | Standard ISO date `YYYY-MM-DD`. |
| `day_of_week` | Attribute | `VARCHAR(16)` | Monday, Tuesday, ..., Sunday. |
| `is_weekend` | Attribute | `BOOLEAN` | `True` for Saturday and Sunday. |
| `month_name` | Attribute | `VARCHAR(16)` | January, February, ..., December. |
| `quarter` | Attribute | `VARCHAR(4)` | Calendar quarter (`Q1`, `Q2`, `Q3`, `Q4`). |
