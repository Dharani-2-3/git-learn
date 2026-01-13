import subprocess
result = subprocess.run(
    ["git", "branch", "-d", branch],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Branch deleted successfully")
elif result.returncode == 1:
    print("Error:", result.stderr)
else:
    print("Unexpected result:", result)
