import json
import os
import requests

from configuration import GITHUB_TARGET_URL, GITHUB_BRANCH, GITHUB_COMMIT_MESSAGE, GITHUB_FILE_CONTENT, \
    GITHUB_FILE_SHA, GITHUB_ACCESS_TOKEN_ENV_NAME


def send_empty_github_commit() -> requests.Response:
    url = GITHUB_TARGET_URL
    data = {'branch': GITHUB_BRANCH,
            'message': GITHUB_COMMIT_MESSAGE,
            'content': GITHUB_FILE_CONTENT,
            'sha': GITHUB_FILE_SHA}
    token = os.environ[GITHUB_ACCESS_TOKEN_ENV_NAME]
    headers = {'Content-Type': 'application/json', 'Authorization': f'token {token}'}
    github_response = requests.put(url=url, data=json.dumps(data), headers=headers)
    if not github_response.status_code == 200:
        error_message = json.loads(github_response.content)
        raise RuntimeError(f'Error message from GitHub: {error_message}')
    return github_response


def send_empty_github_commits(n: int):
    last_response = None
    for _ in range(n):
        last_response = send_empty_github_commit()
    return last_response
