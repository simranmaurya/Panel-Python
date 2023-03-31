from github import Github
import os
from dotenv import load_dotenv

load_dotenv()

PAT = os.getenv('GitHub_PAT')
g = Github(PAT)

# All Repos
def get_all_repos(g):
    repo_list = []
    for repo in g.get_user().get_repos():
        repo_list.append(repo.name)
    return repo_list

# Get Repo by Name
def create_connection(g):
    return g.get_user().get_repo("testPanel")

# Get Repo Topic
def get_repo_topics(repo):
    topic_list = repo.get_topics()
    return topic_list

# Get File Content
def get_file_content(repo):
    return repo.get_contents("testfilePanel.txt").decoded_content
