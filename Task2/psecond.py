import panel as pn
import pandas as pd
import numpy as np
import sqlite3
import product
pn.extension(template = 'fast')

# DIRECT
# connection = sqlite3.connect("data.db")
# retdata = product.get_all(connection)
# print(retdata)

connection = product.connect()
def create_once(connection):
    product.create_table(connection)
    product.insert_val(connection)

create_once(connection)

# def access_data(connection):
#     data_value = product.get_all(connection)
#     col_name = product.get_columns(connection)
#     return data_value,col_name


# data_value,col_name = access_data(connection)
# print(data_value)
# print("break")
# print(col_name)

pn.pane.Markdown('''
## TASK2
### Training for PANEL
''').servable(target='sidebar')

df = pd.read_sql_query("SELECT * FROM product_table", connection)
df['Sales'] = df['Quantity'] * df['Price']
dfrow, dfcol = df.shape
print(dfrow)

grid = pn.GridSpec(height = 300,width = 500)
colname = df.keys()
for j in range(dfcol):
    grid[0,j] = colname[j]
for i in range(dfrow):
    grid[i,0] = df.loc[i,'Product']
    grid[i,1] = df.loc[i].at['Price']
    grid[i,2] = df.loc[i].at['Quantity']
    grid[i,3] = df.loc[i].at['Sales']

grid.servable(target='main')


data = list(df['Product'].unique())
total_sales_button = pn.widgets.Button(name = 'Total Sales', button_type = 'primary')
multiselectbutton = pn.widgets.MultiSelect(name = 'Products',value = ['Watch'] ,options = data)
product_sales_button = pn.widgets.Button(name = 'Product Sales', button_type = 'primary')
str_val = multiselectbutton.value[0]

# # Total Sales
# @pn.depends(total_sales_button)
# def total_sales(tselect):
#     if tselect:
#         return df['Sales'].sum()

@pn.depends(multiselectbutton,product_sales_button)
def product_sales(mselect,pselect):
    if pselect:
        val = 0
        print(len(mselect))
        for i in range(len(mselect)):
            val = val + df[df['Product'] == mselect[i]]['Sales'].sum()
        return val

pn.Column(
    multiselectbutton,
    product_sales_button,
    product_sales,
    # total_sales_button,
    # total_sales
).servable(target='main')


