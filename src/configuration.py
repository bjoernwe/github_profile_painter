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
GITHUB_BRANCH = 'paint_commits'
GITHUB_COMMIT_MESSAGE = '🎨 API commit'
GITHUB_ACCESS_TOKEN_ENV_NAME = 'GITHUB_ACCESS_TOKEN'
GITHUB_COMMIT_REPETITIONS = 4  # makes the color more robust against accidental additional commits
