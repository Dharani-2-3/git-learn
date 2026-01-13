import subprocess

branch = "branch-name"

result = subprocess.run(
    ["git", "branch", "-d", branch],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Branch deleted successfully")
else:
    print("Error:", result.stderr)
