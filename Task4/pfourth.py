import panel as pn
import hcl2
import githubterraform as gt
from time import perf_counter

pn.extension(template = 'fast')
pn.pane.Markdown(''' ## TASK4
### Training for Panel ''').servable(target='sidebar')

t_start = perf_counter()

# Access GitHub Content
content = gt.repo.get_contents("qa.tfvars","qa").decoded_content
content = content.decode()

# Access Commented Lines
x = content.split("\n")
k = []
for i in x:
    k.append(i.split("//")[-1])  
del k[0]
del k[-1]


# Write to file
f = open('Task4/test.tfvars' , "w")
f.writelines(content)
f.close()

# Read from the file
with open("Task4/test.tfvars", 'r') as file:
    dict = hcl2.load(file)


grid = pn.GridSpec(height = 250, width = 700)
grid[0,0] = pn.pane.Markdown(''' ### KEY''')
grid[0,1] = pn.pane.Markdown(''' ### VALUE''')
grid[0,2] = pn.pane.Markdown(''' ### DESCRIPTION''')

i = 1
for key in dict.keys():
    grid[i,0] = key
    grid[i,1] = dict[key]
    grid[i,2] = k[i-1]
    i += 1

t_stop = perf_counter()
card = pn.Card(t_stop-t_start, title='Time Taken', background='Yellow',sizing_mode = 'stretch_both')

pn.Column(grid,
          pn.layout.HSpacer(height=60),
          card).servable(target='main')


