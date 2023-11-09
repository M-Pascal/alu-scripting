#!/usr/bin/python3
"""
This module contains the top_ten function that queries the Reddit API
and prints the titles of the top 10 hot posts of a subreddit.
"""


import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts of a subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Prints:
        The title of each of the first 10 hot posts listed for the given subreddit.
        Prints None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'python3:top-ten:v1.0 (by /u/yourusername)'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: ./1-top_ten.py <subreddit>")
        sys.exit(1)

    top_ten(sys.argv[1])
