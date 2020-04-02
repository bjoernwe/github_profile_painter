import base64
import json
import numpy as np
import os
import requests

from configuration import GITHUB_TARGET_URL, GITHUB_BRANCH, GITHUB_COMMIT_MESSAGE, GITHUB_ACCESS_TOKEN_ENV_NAME


def send_random_github_commit() -> dict:
    response = _send_random_github_commit()
    return _get_content_dict_from_response(response)


def _send_random_github_commit() -> requests.Response:
    random_new_content = base64.b64encode(bytes(str(np.random.randint(1000000)), encoding='utf8'))
    last_content_sha = get_last_random_content_from_github()['sha']
    data = {'branch': GITHUB_BRANCH,
            'message': GITHUB_COMMIT_MESSAGE,
            'content': random_new_content,
            'sha': last_content_sha}
    headers = _get_github_request_headers()
    github_response = requests.put(url=GITHUB_TARGET_URL, data=json.dumps(data), headers=headers)
    return github_response


def _get_github_request_headers() -> dict:
    token = os.environ[GITHUB_ACCESS_TOKEN_ENV_NAME]
    headers = {'Authorization': f'token {token}', 'Content-Type': 'application/json'}
    return headers


def _get_content_dict_from_response(response: requests.Response) -> dict:
    response_content = json.loads(response.content)
    if not response.status_code == 200:
        raise RuntimeError(f'Error message from GitHub: {response_content}')
    return response_content


def get_last_random_content_from_github() -> dict:
    response = _get_last_random_content_from_github()
    return _get_content_dict_from_response(response)


def _get_last_random_content_from_github() -> requests.Response:
    headers = _get_github_request_headers()
    github_response = requests.get(url=GITHUB_TARGET_URL, headers=headers)
    return github_response


def send_multiple_random_github_commits(n: int):
    last_response = None
    for _ in range(n):
        last_response = send_random_github_commit()
    return last_response
