import requests
import json
def get_repo_using_api():
    user_name = input("\nEnter the GitHub user name: ")
    token = "Your_Token"
    url = f"https://api.github.com/users/{user_name}/repos"
    headers = {
        "Authorization" : f"Bearer {token}",
        "Accept" : "Application/json"
    }
    response = requests.get(url, headers=headers)
    try:
        repo_name=[]
        with open("output.json", "w") as file:
            for repo in response.json():
                repo_name.append(repo['name'])
                print(repo['name'])
            json.dump(repo_name, file, indent=2)
    except Exception as e:
        if(response.status_code == 404):
            print("User not found. Please check the username and try again.")
            
get_repo_using_api()
