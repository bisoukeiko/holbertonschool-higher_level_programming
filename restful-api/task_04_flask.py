#!/usr/bin/python3
"""
    RESTful API - task04
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def get_usernames():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_users(username):

    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 400


@app.route("/add_user", methods=['POST'])
def add_user():
    post_data = request.get_json()

    if "username" not in post_data:
        return jsonify({"error": "Username is required"}), 400

    new_user = {
        "username": post_data["username"],
        "name": post_data["name"],
        "age": post_data["age"],
        "city": post_data["city"]
    }

    users[post_data["username"]] = new_user

    return_message = {
        "message": "User added",
        "user": users[post_data["username"]]
    }

    return jsonify(return_message)


if __name__ == "__main__":
    app.run()
