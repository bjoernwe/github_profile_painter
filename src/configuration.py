PATTERN = [[3, 4, 4, 4, 2, 1, 2, 3, 3, 4, 4, 3, 3, 1, 2, 3, 4, 4, 2, 1, 1, 3, 4, 2, 1, 1, 2],
           [4, 3, 2, 3, 4, 3, 1, 1, 2, 3, 4, 4, 1, 1, 3, 4, 3, 3, 4, 2, 1, 2, 4, 3, 1, 2, 4],
           [2, 1, 1, 1, 2, 4, 3, 1, 1, 2, 3, 4, 1, 2, 4, 2, 1, 2, 3, 4, 1, 1, 3, 4, 3, 4, 3],
           [1, 2, 4, 4, 1, 2, 4, 2, 1, 1, 2, 4, 1, 2, 4, 1, 1, 1, 2, 4, 2, 1, 2, 3, 4, 3, 1],
           [2, 4, 3, 3, 4, 1, 4, 3, 2, 1, 2, 4, 3, 1, 3, 4, 3, 2, 3, 4, 3, 1, 1, 4, 3, 2, 1],
           [4, 3, 2, 1, 3, 1, 3, 2, 3, 2, 1, 3, 4, 2, 1, 1, 2, 3, 4, 3, 4, 2, 1, 4, 3, 1, 1],
           [4, 2, 1, 0, 2, 3, 2, 1, 2, 3, 4, 4, 4, 4, 3, 3, 4, 4, 3, 2, 2, 3, 4, 3, 2, 1, 2]]

PATTERN_WIDTH = 27

assert len(PATTERN) == 7
assert len(PATTERN[0]) == PATTERN_WIDTH

GITHUB_TARGET_URL = 'https://api.github.com/repos/bjoernwe/github_profile_painter/contents/res/commit_target.txt'
GITHUB_FILE_CONTENT = 'IyBUaGlzIGZpbGUgYmUgcmVwZWF0ZWRseSB1cGRhdGVkIHRvIGdlbmVyYXRl\nIGNvbW1pdHM=\n'
GITHUB_FILE_SHA = '639e1cf495c7b24501f1f152d8623ae4ba807af2'
GITHUB_BRANCH = 'master'
GITHUB_COMMIT_MESSAGE = '🎨 Painting ...'
GITHUB_ACCESS_TOKEN_ENV_NAME = 'GITHUB_ACCESS_TOKEN'
GITHUB_COMMIT_REPETITIONS = 2  # makes the color more robust against accidental additional commits
