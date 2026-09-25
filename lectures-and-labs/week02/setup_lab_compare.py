# Before attached to coverstation.
#setup_lab.py is an environment checker for the setup lab. It prints one result per check and exits with status 0 when the essential setup is valid, or 1 when something essential is missing.

# After attached to coverstation.
# setup_lab.py is an environment preflight checker. It:
# Checks Python is version 3.10 or newer.
# Confirms README.md and requirements.txt exist beside the script.
# Tries importing numpy and pandas.
# Reports whether it is running in GitHub Codespaces.
# Reports whether the GitHub CLI is authenticated.
# Checks that the Git remote is a student copy, not the original module repository.
# Prints Ready. and exits with status 0 if the essential checks pass; otherwise it exits with status 1.
# The Codespace, GitHub login, and repository-copy checks are informational only. Python, the lab files, and the packages are essential.