#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"
    params = {"per_page": 10}

    try:
        response = requests.get(url, params=params)
        commits = response.json()

        for commit in commits:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")

    except ValueError:
        print("Error fetching data from GitHub API")
