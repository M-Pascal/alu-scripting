import json
import urllib.error
import urllib.parse
import urllib.request

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    req_object = urllib.request.Request(url, method="GET")
    req_object.add_header('User-Agent', 'OboloScript/1.0')
    
    try:
        with urllib.request.urlopen(req_object) as res_object:
            res_json = json.JSONDecoder().decode(res_object.read().decode("utf-8"))
    except urllib.error.HTTPError:
        return 0
    else:
        return res_json["data"]["subscribers"]

