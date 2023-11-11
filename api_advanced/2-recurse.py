#!/usr/bin/python3
"""
1-main
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    1-main
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'pasco user agent 1.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:

        return None
    posts = response.json().get('data').get('children')
    hot_list = hot_list
    for post in posts:
        hot_list.append(post['data']['title'])
    return recurse(subreddit, hot_list)
