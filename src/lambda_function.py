from configuration import GITHUB_COMMIT_REPETITIONS
from github import send_multiple_random_github_commits
from pattern import get_pattern_intensity_for_today


def aws_lambda_handler(event, context):
    pixel_intensity = get_pattern_intensity_for_today()
    num_commits = GITHUB_COMMIT_REPETITIONS * pixel_intensity
    send_multiple_random_github_commits(n=num_commits)
