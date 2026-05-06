# Woo Attribute Transformer

A simple Python script that converts WooCommerce attribute exports into a clean, flat table for Excel or Sales Layer import.

It takes WooCommerce columns like:

| ID | Attribute 1 name | Attribute 1 value(s) | Attribute 2 name | Attribute 2 value(s) |
|---:|---|---|---|---|
| 185905 | Fabric Grade | Grade 1, Grade 2, Grade 3 | Frame Finish | Bronze Sparkle, Black |
| 186370 | Features | Nestable, Space Saving | Material | Powder-epoxy painted steel |

And transforms them into:

| ID | Fabric Grade | Frame Finish | Features | Material |
|---:|---|---|---|---|
| 185905 | Grade 1, Grade 2, Grade 3 | Bronze Sparkle, Black |  |  |
| 186370 |  |  | Nestable, Space Saving | Powder-epoxy painted steel |

---

## Requirements

You need Python installed.

Install the required libraries:

```bash
pip install pandas openpyxl
```

---

## How to use

Run the script:

```bash
python woo_attribute_transformer.py
```

The script will ask you:

### 1. File path

Example:

```text
Enter path to your Excel file:
```

You can enter something like:

```text
C:\Users\YourName\Downloads\woocommerce-export.xlsx
```

or on Mac:

```text
/Users/yourname/Downloads/woocommerce-export.xlsx
```

### 2. ID column

Example:

```text
Type EXACT name of ID column:
```

Enter:

```text
ID
```

### 3. Attribute start column

The script prints your columns with numbers, like:

```text
0: ID
1: Type
2: SKU
3: Name
10: Attribute 1 name
11: Attribute 1 value(s)
12: Attribute 1 visible
```

If attributes start at column 10, enter:

```text
10
```

### 4. Attribute end column

If your last attribute-related column is 48, enter:

```text
48
```

---

## Output

The script creates:

```text
clean_output.xlsx
```

This file contains:

- One row per ID
- One column per attribute name
- Attribute values correctly placed under their matching attribute columns

---
