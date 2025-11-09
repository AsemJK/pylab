import os
import subprocess #subprocess is used to run the batch file
import time
import random

batch_file_path = 'git_push.bat'  # Replace with the actual path to your .bat file

interval_seconds = 470 # Interval

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
up_to = 600 #times to run the batch file
for _ in range(up_to):
    filename = os.path.join(os.path.dirname(__file__), 'data.txt')
    with open(filename,"a") as file:
        file.write(time.ctime() + "\n")
        time.sleep(2)
        file.flush()
    run_batch_file()
    print(time.ctime())
    time.sleep(interval_seconds + random.randint(0,120))  # Sleep for the defined interval plus a small random delay