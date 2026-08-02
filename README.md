# Inventory Reorder Alert System

## Overview

The Inventory Reorder Alert System is a Python application that helps identify products that require restocking based on their current stock levels and predefined reorder thresholds. The program reads inventory data from a CSV file, analyzes stock levels, and generates a report of items that need to be reordered.

## Features

- Read inventory data from a CSV file
- Detect items below the reorder threshold
- Display a formatted reorder report
- Export the report to a new CSV file
- Handle missing input files using exception handling

## Technologies Used

- Python 3
- CSV Module

## Project Structure

```
Inventory-Reorder-Alert-System/
│
├── inventory_alert.py
├── inventory.csv
├── restock_report.csv
└── README.md
```

## How to Run

1. Clone the repository

2. Navigate to the project folder

3. Run:

```
python inventory_alert.py
```

## Sample Output

```
Items that need reordering

Item Name           : Laptop
Current Quantity    : 10
Reorder Threshold   : 15
Status              : Needs Reorder
```

## Author

Rahul PV
