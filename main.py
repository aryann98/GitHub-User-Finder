import requests as rt


username = input("Enter Github Username: ")

url = f"https://api.github.com/users/{username}"
try:
    response = rt.get(url , timeout=5)
    if response.status_code == 200:
        data = response.json()
        print("User Name: ",data["login"])
        print("Name: " , data["name"])
        print("User Followers: " , data["followers"])
        print("User Repo's: " , data["public_repos"])
        email = data.get("email")
        if email:
            print("Use Email: " , email)
        else:
            print("User Email not available")
    elif response.status_code == 404:
        print('User not exists!')
    elif response.status_code == 500:
        print("Server Issue!")
    elif response.status_code == 403:
        print("Access Rate Limit issue!")
    else:
        print("Something went wrong!")
except rt.exceptions.RequestException:
    print("Request Failed!")