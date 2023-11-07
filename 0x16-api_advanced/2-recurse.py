#!/usr/bin/python3
"""A function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """A function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit."""
    article_list = hot_list
    params = {"limit": "100"}
    if after:
        params["after"] = after
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={
            "User-Agent": "subscribercheck",
        },
        params=params,
        allow_redirects=False,
    )
    if response.status_code is not 200:
        return None
    resp = response.json()["data"]["children"]
    if resp:
        for i in resp:
            article_list.append(i["data"]["title"])

        afterd = response.json()["data"]["after"]
        if afterd is None:
            return article_list
        else:
            return recurse(subreddit, article_list, afterd)

if __name__ == "__main__":
    subreddit = "programming"  # Replace with the subreddit you want to check
    articles = recurse(subreddit)
    for i, article in enumerate(articles, start=1):
        print(f"{i}. {article}")
