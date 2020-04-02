import base64
import json
import os
import pytest
import requests

import github

from configuration import GITHUB_ACCESS_TOKEN_ENV_NAME


class TestGithubAccess:

    @pytest.fixture
    def access_token(self):
        return os.environ[GITHUB_ACCESS_TOKEN_ENV_NAME]

    def test_github_access_token_is_defined(self, access_token):
        assert access_token is not None
        assert access_token != ''

    @pytest.fixture
    def github_response(self):
        return github._get_last_random_content_from_github()

    def test_github_response_has_status_200(self, github_response):
        assert github_response.status_code == 200

    @pytest.fixture
    def github_response_dict(self):
        return github.get_last_random_content_from_github()

    def test_random_content_from_github_in_valid_range(self, github_response_dict):
        file_content = base64.b64decode(github_response_dict['content'])
        random_number = int(file_content)
        assert 0 <= random_number < 1000000
