import nbformat as nbf   # library to Create Jupyter Notebook

nb = nbf.v4.new_notebook()  #Create Jupyter Notebook

# MarkDown Cells
text = """\
# Create or Open CSV
"""

text1="""\
# Read CSV files."""

text2="""\
# Writing to Existing File"""

#Code Cells
code = """\
import csv
with open('employee_details.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Email-ID"])
    writer.writerow([1, "Namrata Patted", "pattednamrata@gmail.com"])
    writer.writerow([2, "Ram Krishna", "krishnaram@gmail.com"])
    writer.writerow([3, "Nalini Mohan", "mohannaline@gmail.com"])"""

code1="""\
data = open('employee_details.csv',encoding="utf-8")
csv_data=csv.reader(data)
datalines=list(csv_data)
datalines"""

code2="""\
with open('employee_details.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["4", "Raj Deep", "deepraj@gmail.com"])"""

code3="""\
data = open('employee_details.csv',encoding="utf-8")
csv_data=csv.reader(data)
datalines=list(csv_data)
datalines"""

# Create Markdown Cells and Code Cells
nb['cells'] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_code_cell(code),
               nbf.v4.new_markdown_cell(text1),
               nbf.v4.new_code_cell(code1),
               nbf.v4.new_markdown_cell(text2),
               nbf.v4.new_code_cell(code2),
               nbf.v4.new_code_cell(code3)]
fname = 'Task_7B_jnb.ipynb'    # Give name for Jupyter notebook

with open(fname, 'w') as f:
    nbf.write(nb, f)