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
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps({
  "key": "SRP1",
  "name": "creatingprojectwithpython",
  "projectTypeKey": "business",
  "projectTemplateKey": "com.atlassian.jira-core-project-templates:jira-core-simplified-process-control",
  "description": "Sreenivasulu practicing project",
  "leadAccountId": "712020:55e1c3ef-21d3-4bff-9f9a-ea7186a10122"
})
auth = HTTPBasicAuth(email, api_token)
response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
