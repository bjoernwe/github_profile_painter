import contextlib
import datetime
import os
import subprocess

import pattern

from configuration import GITHUB_COMMIT_REPETITIONS, GITHUB_COMMIT_MESSAGE, GITHUB_BRANCH


def set_system_date_to_past(days_back=0):
    past_date = get_datetime_from_past(days_back=days_back)
    set_system_date(dt=past_date)


def get_datetime_from_past(days_back=0):
    now = datetime.datetime.now()
    today = datetime.datetime(now.year, now.month, now.day, 12)
    timedelta = datetime.timedelta(days=days_back)
    day_in_past = today - timedelta
    return day_in_past


def set_system_date(dt: datetime.datetime):
    new_date_str = f'{dt.year}-{dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
    print(f'Setting system date to {new_date_str}')
    subprocess.call(['date', '-s', new_date_str])


@contextlib.contextmanager
def preserve_system_date():
    now = datetime.datetime.now()
    yield
    set_system_date(dt=now)


def preserve_cwd(func):
    def func_wrapper(*args, **kwargs):
        cwd = os.getcwd()
        func(*args, **kwargs)
        os.chdir(cwd)
    return func_wrapper


@preserve_cwd
def create_random_git_commit(git_dir: str, message: str, branch: str = 'master'):
    os.chdir(git_dir)
    subprocess.call(['git', 'checkout', '-b', branch])
    with open('random.txt', 'w') as f:
        subprocess.call(['shuf', '-i', '0-999999', '-n1'], stdout=f)
    subprocess.call(['git', 'add', 'random.txt'])
    subprocess.call(['git', 'commit', '-a', '-m', message])


def commit_pattern_in_past(git_dir: str, days_back: int = 2*365):
    for i in range(days_back):
        with preserve_system_date():
            set_system_date_to_past(days_back=i)
            pixel_intensity = pattern.get_pattern_intensity_for_today()
            if pixel_intensity:
                n_commits = GITHUB_COMMIT_REPETITIONS * pixel_intensity
                for _ in range(n_commits):
                    create_random_git_commit(git_dir=git_dir,
                                             message=GITHUB_COMMIT_MESSAGE,
                                             branch=GITHUB_BRANCH)


def main():
    local_git_dir = '/home/bjoern/Desktop/profile-pattern'
    commit_pattern_in_past(git_dir=local_git_dir, days_back=365)


if __name__ == '__main__':
    main()
