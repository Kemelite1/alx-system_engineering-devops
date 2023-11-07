import requests

def number_of_subscribers(subreddit):
    # Define the Reddit API URL for the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid too many requests error
    headers = {"User-Agent": "MyBot/1.0"}

    # Send a GET request to the API
    response = requests.get(url, headers=headers)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and return the number of subscribers
        return data['data']['subscribers']
    else:
        # Return 0 for invalid or non-existent subreddits
        return 0

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
