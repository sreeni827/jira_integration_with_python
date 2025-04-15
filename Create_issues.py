import os
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
from flask import Flask, jsonify

# Load environment variables
load_dotenv()

email = os.getenv("ATLASSIAN_EMAIL")
api_token = os.getenv("ATLASSIAN_API_TOKEN")

# Make sure both are set
if not email or not api_token:
    raise ValueError("Environment variables ATLASSIAN_EMAIL and ATLASSIAN_API_TOKEN must be set.")

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():
    url = "https://sreenuramanaboina.atlassian.net/rest/api/3/issue"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "issuetype": {
                "id": "10002"
            },
            "project": {
                "key": "SCRUM"
            },
            "summary": "I am creating this Jira using Python"
        }
    }

    auth = HTTPBasicAuth(email, api_token)

    response = requests.post(
        url,
        data=json.dumps(payload),
        headers=headers,
        auth=auth
    )

    return jsonify(response.json()), response.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
