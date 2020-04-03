import base64
import datetime
import json
import os
import random
import requests

from typing import List

from configuration import GITHUB_TARGET_URL, GITHUB_COMMITS_URL, GITHUB_BRANCH, GITHUB_COMMIT_MESSAGE, \
    GITHUB_ACCESS_TOKEN_ENV_NAME


def send_random_github_commit() -> dict:
    response = _send_random_github_commit()
    return _get_content_dict_from_response(response)


def _send_random_github_commit() -> requests.Response:
    random_new_content = base64.b64encode(bytes(str(random.randint(0, 999999)), encoding='utf-8')).decode('utf-8')
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


def _get_content_dict_from_response(response: requests.Response):
    response_content = response.json()
    if not response.status_code == 200:
        raise RuntimeError(f'Error message from GitHub: {response.status_code} - {response_content["message"]}')
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


def get_number_of_todays_random_commits() -> int:
    todays_random_commits = get_todays_random_commit()
    return len(todays_random_commits)


def get_todays_random_commit() -> List[dict]:
    last_midnight = _get_last_midnight().isoformat() + 'Z'
    data = {'path': '/random.txt',
            'since': last_midnight}
    headers = _get_github_request_headers()
    github_response = requests.get(url=GITHUB_COMMITS_URL, data=json.dumps(data), headers=headers)
    commits = _get_content_dict_from_response(github_response)
    filtered_commits = _filter_commits_for_current_day(commits)
    return filtered_commits


def _filter_commits_for_current_day(commits: List[dict]) -> List[dict]:
    last_midnight = _get_last_midnight().isoformat() + 'Z'
    filtered_commits = [c for c in commits if c['commit']['author']['date'] >= last_midnight]
    return filtered_commits


def _get_last_midnight() -> datetime.datetime:
    return datetime.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)


if __name__ == '__main__':
    print(get_number_of_todays_random_commits())
