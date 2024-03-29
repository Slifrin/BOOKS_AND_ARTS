"""
    https://www.atlassian.com/git/tutorials/git-hooks
"""


import sys, os, re
from subprocess import check_output

# Collect the parameters
previous_head = sys.argv[1]
new_head = sys.argv[2]
is_branch_checkout = sys.argv[3]

if is_branch_checkout == "0":
    print("post-checkout: This is a file checkout. Nothing to do.")
    sys.exit(0)

print("post-checkout: Deleting all '.pyc' files in working directory")
for root, dirs, files in os.walk('.'):
    for filename in files:
        ext = os.path.splitext(filename)[1]
        if ext == '.pyc':
            os.unlink(os.path.join(root, filename))