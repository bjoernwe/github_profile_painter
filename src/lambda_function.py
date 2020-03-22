import datetime
import json
import os
import requests


PATTERN = [[2, 3, 3, 3, 1, 0, 1, 2, 2, 3, 3, 2, 2, 0, 1, 2, 3, 3, 1, 0, 0, 2, 3, 1, 0, 0, 1],
           [3, 2, 1, 2, 3, 2, 0, 0, 1, 2, 3, 3, 0, 0, 2, 3, 2, 2, 3, 1, 0, 1, 3, 2, 0, 1, 3],
           [1, 0, 0, 0, 1, 3, 2, 0, 0, 1, 2, 3, 0, 1, 3, 1, 0, 1, 2, 3, 0, 0, 2, 3, 2, 3, 2],
           [0, 1, 3, 3, 0, 1, 3, 1, 0, 0, 1, 3, 0, 1, 3, 0, 0, 0, 1, 3, 1, 0, 1, 2, 3, 2, 0],
           [1, 3, 2, 2, 3, 0, 3, 2, 1, 0, 1, 3, 2, 0, 2, 3, 2, 1, 2, 3, 2, 0, 0, 3, 2, 1, 0],
           [3, 2, 1, 0, 2, 0, 2, 1, 2, 1, 0, 2, 3, 1, 0, 0, 1, 2, 3, 2, 3, 1, 0, 3, 2, 0, 0],
           [3, 1, 0, 0, 1, 2, 1, 0, 1, 2, 3, 3, 3, 3, 2, 2, 3, 3, 2, 1, 1, 2, 3, 2, 1, 0, 1]]

PATTERN_WIDTH = 27

assert len(PATTERN) == 7
assert len(PATTERN[0]) == PATTERN_WIDTH

GITHUB_TARGET_URL = 'https://api.github.com/repos/bjoernwe/github_profile_painter/contents/res/commit_target.txt'
GITHUB_FILE_CONTENT = 'IyBUaGlzIGZpbGUgYmUgcmVwZWF0ZWRseSB1cGRhdGVkIHRvIGdlbmVyYXRl\nIGNvbW1pdHM=\n'
GITHUB_FILE_SHA = '639e1cf495c7b24501f1f152d8623ae4ba807af2'
GITHUB_COMMIT_MESSAGE = '🎨 API commit'
GITHUB_ACCESS_TOKEN_ENV_NAME = 'GITHUB_ACCESS_TOKEN'


def get_pattern_intensity_for_today() -> int:
    row = get_day_of_week()
    col = get_week_index() % PATTERN_WIDTH
    return PATTERN[row][col]


def get_day_of_week(date_time=None) -> int:
    if not date_time:
        date_time = datetime.datetime.utcnow()
    return date_time.isoweekday() % 7


def get_week_index(date_time=None) -> int:
    if not date_time:
        date_time = datetime.datetime.utcnow()
    ref_date_time = datetime.datetime(2020, 3, 1)
    diff_in_days = (date_time - ref_date_time).days
    return int(diff_in_days // 7)


def send_empty_github_commit() -> requests.Response:
    url = GITHUB_TARGET_URL
    data = {'message': GITHUB_COMMIT_MESSAGE,
            'content': GITHUB_FILE_CONTENT,
            'sha': GITHUB_FILE_SHA}
    token = os.environ[GITHUB_ACCESS_TOKEN_ENV_NAME]
    headers = {'Content-Type': 'application/json', 'Authorization': f'token {token}'}
    response = requests.put(url=url, data=json.dumps(data), headers=headers)
    return response


if __name__ == '__main__':
    intensity = get_pattern_intensity_for_today()
    for _ in range(intensity):
        send_empty_github_commit()