#!/usr/bin/pyton3
"""
    RESTful API - task0
"""
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"
csv_file = "posts.csv"


def fetch_and_print_posts():
    """ Define a function that fetches all post from JSONPlaceholde
        Print the status code of the response
        Parse fetched data into a JSON object and print out
        the titles of all the posts
    """

    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        data = response.json()
        for post_dict in data:
            print(post_dict["title"])


def fetch_and_save_posts():
    """ Define a function that fetches all post from JSONPlaceholde
        Parse fetched data into a JSON object and structure the data into
        a list of dictionaries where each dictionary represents a post with
        keys and values for id, title, and body
        write this data into a CSV file
    """

    response = requests.get(url)

    if response.status_code == 200:

        with open(csv_file, "w") as file:
            columns = ["id", "title", "body"]
            writer = csv.DictWriter(file, columns, extrasaction='ignore')
            writer.writeheader()

            data = response.json()

            for post_dict in data:
                writer.writerow(post_dict)
