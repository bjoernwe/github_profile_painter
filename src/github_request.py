import json
import os
import requests


def send_empty_commit() -> requests.Response:
    url = 'https://api.github.com/repos/bjoernwe/github_profile_painter/contents/res/commit_target.txt'
    data = {'message': '🎨 API commit',
            'content': 'IyBUaGlzIGZpbGUgYmUgcmVwZWF0ZWRseSB1cGRhdGVkIHRvIGdlbmVyYXRl\nIGNvbW1pdHM=\n',
            'sha': '639e1cf495c7b24501f1f152d8623ae4ba807af2'}
    token = os.environ['GITHUB_ACCESS_TOKEN']
    headers = {'Content-Type': 'application/json', 'Authorization': f'token {token}'}
    response = requests.put(url=url, data=json.dumps(data), headers=headers)
    return response


def main():
    send_empty_commit()


if __name__ == '__main__':
    main()
