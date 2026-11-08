# Retail ETL Pipeline

A  ETL pipeline that extracts raw retail data from CSV files, transforms it using Pandas, and loads it into a PostgreSQL data warehouse using a Star Schema.

## Overview

This project simulates a retail data engineering workflow by integrating data from three sources:

- **Sales:** Weekly sales transactions by store and department.
- **Stores:** Store information, including type and size.
- **Features:** External factors such as temperature, fuel prices, promotions, CPI, and unemployment.

## Architecture

```text
Raw CSV Files
     |
     v
 extract.py
     |
     v
transform.py
     |
     v
   load.py
     |
     v
  main.py
     |
     v
PostgreSQL Data Warehouse
```

## Data Warehouse Schema

The data is organized using a Star Schema consisting of:

- **fact_sales:** Weekly sales by store and department.
- **dim_store:** Store attributes such as type and size.
- **dim_date:** Date attributes including week, month, year, and holiday flag.
- **dim_features:** Economic indicators and promotional markdowns.

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- CSV


