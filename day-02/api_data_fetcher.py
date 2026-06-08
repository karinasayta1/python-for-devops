import requests
import json
def get_repo_using_api():
    user_name = input("\nEnter the GitHub user name: ")
    
    token = "ADD_TOKEN"
    url = f"https://api.github.com/users/{user_name}/repos"
    headers = {
        "Authorization" : f"Bearer {token}",
        "Accept" : "Application/json"
    }
    response = requests.get(url, headers=headers)
    repo_name=[]    

    with open("output.json", "w") as file:
        for repo in response.json():
            repo_name.append(repo['name'])
            print(repo['name'])

        json.dump(repo_name, file, indent=2)

get_repo_using_api()
