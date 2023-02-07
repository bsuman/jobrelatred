import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

credentials = None
if os.path.exists('token.pickle'):
    print('Loading Credentials From File..')
    with open("token.pickle", 'rb') as token:
        credentials = pickle.load(token)

if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        print("Refreshing Access Token..")
        credentials.refresh(Request())
    else:
        print("Fetching New Tokens..")
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json",
                                                         scopes=["https://www.googleapis.com/auth/jobs","https://www.googleapis.com/auth/cloud-platform"])
        flow.run_local_server(port=8080, prompt="consent", authorization_prompt_message="")
        credentials = flow.credentials
        with open("token.pickle", 'wb') as token:
            print("Save The New Credentials..")
            pickle.dump(credentials,token)

parent = 'projects/talentsearchapi'
client_service = build('jobs', 'v3',credentials=credentials)
request_metadata = {
    'user_id': 'HashedUserId',
    'session_id': 'HashedSessionId',
    'domain': 'www.google.com'
}
job_query = {'query': "Python Developer"}
company_name = "Google"
if company_name is not None:
    job_query.update({'company_names': [company_name]})
request = {
    'search_mode': 'JOB_SEARCH',
    'request_metadata': request_metadata,
    'job_query': job_query,
}
response = client_service.projects().jobs().search(parent=parent, body=request).execute()
print(response["matchingJobs"])