import json
import os
import pytest
import requests

from configuration import GITHUB_ACCESS_TOKEN_ENV_NAME, GITHUB_TARGET_URL, GITHUB_FILE_SHA


class TestGithubAccess:

    @pytest.fixture
    def valid_token(self):
        return os.environ[GITHUB_ACCESS_TOKEN_ENV_NAME]

    @pytest.fixture
    def github_response(self, valid_token):
        url = GITHUB_TARGET_URL
        token = os.environ[GITHUB_ACCESS_TOKEN_ENV_NAME]
        headers = {'Content-Type': 'application/json', 'Authorization': f'token {token}'}
        response = requests.get(url=url, headers=headers)
        return response

    def test_access_token_is_valid(self, github_response):
        assert github_response.status_code == 200

    def test_github_file_has_correct_hash(self, github_response):
        content = json.loads(github_response.content)
        file_hash = content['sha']
        assert file_hash == GITHUB_FILE_SHA
