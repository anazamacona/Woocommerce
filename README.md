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

## What this script does

The script reads a WooCommerce Excel export and converts repeated attribute columns into normal spreadsheet columns.

### Before

WooCommerce exports attributes like this:

```text
Attribute 1 name        Attribute 1 value(s)
Frame Finish            Black, White, Silver

Attribute 2 name        Attribute 2 value(s)
Material                Aluminum
```

### After

The script turns them into this:

```text
Frame Finish            Material
Black, White, Silver    Aluminum
```

This makes the file easier to import into Sales Layer or edit in Excel.

---

## Visual flow

```text
WooCommerce export
        |
        v
Attribute 1 name + Attribute 1 value(s)
Attribute 2 name + Attribute 2 value(s)
Attribute 3 name + Attribute 3 value(s)
        |
        v
One clean table
        |
        v
ID | Fabric Grade | Frame Finish | Features | Material | ...
```

---

## Why this is useful

WooCommerce stores attributes in repeated pairs:

```text
Attribute X name
Attribute X value(s)
```

That format is hard to use in a PIM.

This script creates one clean column per attribute name, which is much easier for:

- Excel cleanup
- Sales Layer imports
- PIM mapping
- Product/variant data preparation

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

## Example

### Input

| ID | Attribute 1 name | Attribute 1 value(s) | Attribute 2 name | Attribute 2 value(s) |
|---:|---|---|---|---|
| 185905 | Fabric Grade | Grade 1, Grade 2 | Frame Finish | Bronze Sparkle, Black |
| 186370 | Features | Nestable, Space Saving | Material | Steel |
| 186589 | Outdoor HDPE Panels | Dark Ash, Teak | Frame Finish | Textured Black |

### Output

| ID | Fabric Grade | Frame Finish | Features | Material | Outdoor HDPE Panels |
|---:|---|---|---|---|---|
| 185905 | Grade 1, Grade 2 | Bronze Sparkle, Black |  |  |  |
| 186370 |  |  | Nestable, Space Saving | Steel |  |
| 186589 |  | Textured Black |  |  | Dark Ash, Teak |

---

## Important notes

### Do not rely on column position manually

The script does **not** guess where values go.

It only maps:

```text
Attribute X name -> Attribute X value(s)
```

This avoids mistakes like:

```text
Features value appearing under Luggage Cart Deck Length
```

or:

```text
Outdoor HDPE Panels value appearing under Full Kit Cart Dimensions
```

### Duplicate attributes

If the same attribute appears more than once in the same row, the script joins the values with:

```text
|
```

Example:

```text
Black | White
```

---

## Recommended GitHub files

Your repository can look like this:

```text
woo-attribute-transformer/
├── README.md
└── woo_attribute_transformer.py
```

Optional later:

```text
examples/
├── sample_input.xlsx
└── sample_output.xlsx
```

---

## Version

Version 1.0

---

## Future improvements

Possible upgrades:

- Auto-detect attribute columns
- Detect products vs variants
- Add Sales Layer attribute sets
- Create a drag-and-drop web tool
- Add CSV support
