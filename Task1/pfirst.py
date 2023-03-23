import panel as pn
import pandas as pd
import numpy as np

pn.extension(template='fast')

pn.pane.Markdown(
    '''
    ## TASK1
    ### Training for PANEL
    '''
).servable(target='sidebar')

df = pd.DataFrame({
    'Product' : ['Burger','Pizza','Noodles','Wings','Momos','Burger'],
    'Quantity' : [3,2,1,4,5,2],
    'Price' : [50,80,60,70,50,50],
})

df['Sales'] = df['Quantity'] * df['Price']
df.index = np.arange(1, len(df) + 1)
df.index = df.index.rename('Serial No.')
dfrow,dfcol = df.shape

grid = pn.GridSpec(width = 500,height = 300,scroll = True)
colname = df.keys()
for j in range(dfcol):
    grid[0,j] = colname[j]

for i in range(1,dfrow+1):
    grid[i,0] = df.loc[i,'Product']
    grid[i,1] = df.loc[i].at['Price']
    grid[i,2] = df.loc[i].at['Quantity']
    grid[i,3] = df.loc[i].at['Sales']
grid.servable(target='main')

total_sales_button = pn.widgets.Button(name = 'Total Sales', button_type = 'primary')
multiselectbutton = pn.widgets.MultiSelect(name = 'Products',value = ['Burger'],options = ['Burger','Pizza','Noodles','Wings'])
product_sales_button = pn.widgets.Button(name = 'Product Sales', button_type = 'primary')
str_val = multiselectbutton.value[0]

# For Total Sales
# @pn.depends(total_sales_button)
# def total_sales(tselect):
#     if tselect:
#         return df['Sales'].sum()

# For selected Products Sales
@pn.depends(multiselectbutton,product_sales_button)
def product_sales(mselect,pselect):
    if pselect:
        val = 0
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
