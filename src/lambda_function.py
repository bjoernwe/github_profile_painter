from configuration import GITHUB_COMMIT_REPETITIONS
from github import get_number_of_todays_random_commits, send_multiple_random_github_commits
from pattern import get_pattern_intensity_for_today


def aws_lambda_handler(event, context):
    pixel_intensity = get_pattern_intensity_for_today()
    num_existing_commits = get_number_of_todays_random_commits()
    num_target_commits = GITHUB_COMMIT_REPETITIONS * pixel_intensity
    num_new_commits = num_target_commits - num_existing_commits
    if num_new_commits > 0:
        send_multiple_random_github_commits(n=num_new_commits)


if __name__ == '__main__':
    aws_lambda_handler(None, None)
