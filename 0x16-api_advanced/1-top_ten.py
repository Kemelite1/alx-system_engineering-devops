import requests

def top_ten(subreddit):
    # Define the Reddit API URL for the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid too many requests error
    headers = {"User-Agent": "MyBot/1.0"}

    # Send a GET request to the API
    response = requests.get(url, headers=headers)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and print the titles of the first 10 hot posts
        for i, post in enumerate(data['data']['children'][:10], start=1):
            print(f"{i}. {post['data']['title']}")
    else:
        # Print None for invalid or non-existent subreddits
        print(None)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
