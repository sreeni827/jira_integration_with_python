import os
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

email = os.getenv("ATLASSIAN_EMAIL")
api_token = os.getenv("ATLASSIAN_API_TOKEN")

# Make sure both are set
if not email or not api_token:
    raise ValueError("Environment variables ATLASSIAN_EMAIL and ATLASSIAN_API_TOKEN must be set.")
url = "https://sreenuramanaboina.atlassian.net/rest/api/3/project"

headers = {
  "Accept": "application/json"
}
auth = HTTPBasicAuth(email, api_token)
response = requests.request(
   "GET",
   url,
   headers=headers,
    auth=auth
   )

lists = json.loads(response.text)

for list in lists:
    print(list["name"])