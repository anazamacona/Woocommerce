# VERSION 1.0 - Woo Attribute Transformer
# Converts WooCommerce attribute export into flat table (Sales Layer ready)

"""
This script converts WooCommerce attribute columns into a clean table format.
It takes "Attribute X name" + "Attribute X value(s)" and turns them into proper columns.
The result is a flat file (one row per product) ready for Excel or Sales Layer import.
"""

import pandas as pd

# -----------------------------
# STEP 1: Load file
# -----------------------------
file_path = input("👉 Enter path to your Excel file: ")

df = pd.read_excel(file_path)

# -----------------------------
# STEP 2: Show columns
# -----------------------------
print("\n✅ Columns in your file:\n")
for i, col in enumerate(df.columns):
    print(f"{i}: {col}")

# -----------------------------
# STEP 3: Ask user inputs
# -----------------------------
id_column = input("\n👉 Type EXACT name of ID column: ")

start_col_index = int(input("👉 Column number where attributes START (e.g. 5): "))
end_col_index = int(input("👉 Column number where attributes END (e.g. 30): "))

# -----------------------------
# STEP 4: Transform data
# -----------------------------
output = []
attribute_headers = []

for _, row in df.iterrows():
    new_row = {"ID": row[id_column]}

    for col_index in range(start_col_index, end_col_index + 1):
        col_name = df.columns[col_index]

        if "Attribute" in col_name and "name" in col_name:
            value_col_name = col_name.replace("name", "value(s)")

            if value_col_name in df.columns:
                attr_name = row[col_name]
                attr_value = row[value_col_name]

                if pd.notna(attr_name):
                    attr_name = str(attr_name).strip()

                    if attr_name not in attribute_headers:
                        attribute_headers.append(attr_name)

                    if attr_name in new_row and new_row[attr_name]:
                        new_row[attr_name] += " | " + str(attr_value)
                    else:
                        new_row[attr_name] = attr_value

    output.append(new_row)

# -----------------------------
# STEP 5: Build final table
# -----------------------------
final_headers = ["ID"] + attribute_headers
out_df = pd.DataFrame(output)
out_df = out_df.reindex(columns=final_headers)

# -----------------------------
# STEP 6: Save file
# -----------------------------
output_file = "clean_output.xlsx"
out_df.to_excel(output_file, index=False)

print(f"\n✅ DONE — file saved as {output_file}")
