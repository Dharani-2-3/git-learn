import subprocess

branch = "dashboard"

subprocess.run(["git", "checkout", "-b", branch])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Add dashboard feature"])
subprocess.run(["git", "push", "-u", "origin", branch])

print("Branch pushed. Open a Pull Request in GitHub/GitLab.")
