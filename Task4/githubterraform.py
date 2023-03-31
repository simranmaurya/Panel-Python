from github import Github
from dotenv import load_dotenv
import os
import hcl2

load_dotenv()
PAT = os.getenv('GitHub_PAT')
g = Github(PAT)
repo = g.get_user().get_repo("testPanel")

