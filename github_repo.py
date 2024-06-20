import requests

"""fetch github repo api
1. create a function to fetch api with the stars greater than 50,000 and only JavaScript, Python, Ruby, Golang.
2. create a function to returns the parameters (query string).
3. called the function to fetch api.
4. looping the response from fetch api function.
5. and then print out the result to the console.
"""

api_url = "https://api.github.com/search/repositories"

def create_query(languages, min_stars = 50000):
    query = f"stars:>{min_stars} "

    for lang in languages:
        query += f"language:{lang} "

    return query

def fetch_github_repo(languages, order = "stars", sort = "desc"):
    query = create_query(languages)
    params = {"q": query, "order": order, "sort": sort}

    response = requests.get(api_url, params)
    # response = requests.get(api_url, params, headers={"Authorization": "Bearer fake_token"}) # for testing the error handler
    
    status_code = response.status_code
    
    if status_code != 200:
        raise RuntimeError(f"An error occurred. Status code was: {status_code}")
    else:
        response_json = response.json()['items']
        return response_json;

if __name__ == '__main__':
    languages = ["JavaScript", "Python", "Ruby", "Go"]
    
    result = fetch_github_repo(languages)

    for data in result:
        lang = data["language"]
        name = data["name"]
        stars = data["stargazers_count"]
        
        print(f"{name} is a {lang} repo with {stars}.")
        