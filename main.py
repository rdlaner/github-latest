"""Github API test script"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    response = requests.get(f"https://api.github.com/users/{username}/events")
    events = response.json()

    print(events[0]["created_at"])
