import datetime
import json
import os
import pytest
import requests

from lambda_function import get_day_of_week, get_week_index
from lambda_function import GITHUB_ACCESS_TOKEN_ENV_NAME, GITHUB_TARGET_URL, GITHUB_FILE_SHA


class TestDateTimeCalculation:

    @pytest.fixture
    def dt_sat(self):
        return datetime.datetime(2020, 3, 21)

    @pytest.fixture
    def dt_sun(self):
        return datetime.datetime(2020, 3, 22)

    @pytest.fixture
    def dt_mon(self):
        return datetime.datetime(2020, 3, 23)

    def test_week_starts_with_sunday(self, dt_sat, dt_sun, dt_mon):
        assert get_day_of_week(date_time=dt_sat) == 6
        assert get_day_of_week(date_time=dt_sun) == 0
        assert get_day_of_week(date_time=dt_mon) == 1

    def test_week_index_increases_on_sunday(self, dt_sat, dt_sun, dt_mon):
        week_index_sat = get_week_index(date_time=dt_sat)
        week_index_sun = get_week_index(date_time=dt_sun)
        week_index_mon = get_week_index(date_time=dt_mon)
        diff_sat_to_sun = week_index_sun - week_index_sat
        diff_sun_to_mon = week_index_mon - week_index_sun
        assert diff_sat_to_sun == 1
        assert diff_sun_to_mon == 0


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
