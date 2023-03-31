import asyncio
import os
from time import perf_counter

import hcl2
import panel as pn
from diskcache import Cache, FanoutCache
from dotenv import load_dotenv
from github import Github

pn.extension(template = 'fast')
pn.pane.Markdown(''' ## TASK5
### Training for Panel ''').servable(target='sidebar')

grid = pn.GridSpec(height = 400, width = 700)
grid[0,0] = pn.pane.Markdown(''' ### KEY''')
grid[0,1] = pn.pane.Markdown(''' ### VALUE''')

t_start = perf_counter()
cache = FanoutCache('Task5/cache.tfvars',shards = 2)
if not 'access_token' in cache:
    load_dotenv()
    access_token = os.getenv('GitHub_PAT')
    cache.set('access_token', access_token, expire=10, read=True)
        
else:
    access_token = cache['access_token']

def add_to_UI():
    i = 1
    for key in cache:
        if key == 'access_token':
            continue
        grid[i,0] = key
        grid[i,1] = cache.get(key)
        i += 1

if not 'resources_value' in cache:
    g = Github(access_token)
    repo = g.get_user().get_repo("testPanel")

    # Access GitHub Content
    content = repo.get_contents("qa.tfvars","qa").decoded_content
    content = content.decode()

    # Access Commented Lines
    x = content.split("\n")
    k = []
    for i in x:
        k.append(i.split("//")[-1])  
    del k[0]
    del k[-1]

    # Write to file
    f = open('Task5/test.tfvars' , "w")
    f.writelines(content)
    f.close()

    # Read from the file
    with open("Task5/test.tfvars", 'r') as file:
        dict = hcl2.load(file)
    
    l = 0
    for key in dict.keys():
        cache.set(f"{key}_value", dict[key],expire=10, read=True)
        cache.set(f"{key}_description",k[l],expire=10, read=True)
        l = l+1
    
    add_to_UI()

else:
    add_to_UI()


t_stop = perf_counter()
card = pn.Card(t_stop-t_start, title='Time Taken', background='Yellow',sizing_mode = 'stretch_both')

pn.Column(grid,
          pn.layout.HSpacer(height=60),
          card).servable(target='main')
