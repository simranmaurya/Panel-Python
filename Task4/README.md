## README FILE

Step 1:
Create a branch called 'qa' in 'testPanel' repository in your GitHub

Step 2:
Add a 'qa.tfvars' terraform file in the 'qa' branch

Step 3:
Follow the Steps 1 to 5 in Panel README.md 

Step 4:
Create a file '.env' in Task4 folder and add the following code : 
```bash
    GitHub_PAT = <YOUR_GITHUB_PAT>
```
where <YOUR_GITHUB_PAT> is your GitHub Personal Access Token 

Step 5:
Run the following command :
```bash
    python Task4/githubterraform.py
```

Step 6:
Run the following command :
```bash
    panel serve --autoreload --show Task4/pfourth.py
```

![Screenshot 2023-03-28 235808](https://user-images.githubusercontent.com/101667353/228333661-dff766cc-9e3a-4b52-a2ea-ae421a0d55b5.png)
