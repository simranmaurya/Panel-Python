import panel as pn
import pandas as pd
import githubfile
# from github import Github

pn.extension(template='fast')

g = githubfile.g
repo = githubfile.create_connection(g)
filecontent = githubfile.get_file_content(repo)

filecontent = filecontent.decode()

pn.pane.Markdown(''' ## TASK3
### Training for Panel ''').servable(target='sidebar')

card = pn.Card(filecontent, title='GitHub File', background='Yellow',height=200, width=200, )
card.servable(target='main')
