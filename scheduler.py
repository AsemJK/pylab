import subprocess #subprocess is used to run the batch file
import time

batch_file_path = 'git_push.bat'  # Replace with the actual path to your .bat file

interval_seconds = 12000 # Interval

def run_batch_file():
    try:
        result = subprocess.run(batch_file_path, shell=True, check=True, capture_output=True, text=True)
        print("Batch file executed successfully.")
        print("Output:", result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing batch file: {e}")
        print("Output:", e.stdout)
        print("Errors:", e.stderr)

# Main loop to schedule the task
up_to = 6 #times to run the batch file
for _ in range(up_to):
    run_batch_file()
    time.sleep(interval_seconds)