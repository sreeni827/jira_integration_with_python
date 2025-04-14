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
url = "https://sreenuramanaboina.atlassian.net/rest/api/3/issue"

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "issuetype": {
      "id": "10002"
    },
  
   
     "project": {
      "key": "SCRUM"
    },
  
 
    "summary": "i am creating this jira using python",
 
 
  },
  "update": {}
} )
auth = HTTPBasicAuth(email, api_token)
response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))