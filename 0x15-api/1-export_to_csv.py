#!/usr/bin/python3
"""extend your Python script to export data in the CSV format."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": "{}".format(argv[1])},
    )
    todos = tasks.json()
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    )
    user = response.json()

    with open("{}.csv".format(user.get("id")), "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for t in todos:
            writer.writerow(
                [
                    "{}".format(to.get("userId")),
                    "{}".format(user_.get("name")),
                    "{}".format(to.get("completed")),
                    "{}".format(to.get("title")),
                ]
            )