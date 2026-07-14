import os
import time
from plyer import notification

# The folder we want to monitor
FOLDER_TO_WATCH = "./secure_folder"

print(f"[*] Starting Real-Time Monitor on: {FOLDER_TO_WATCH}")
print("[*] Waiting for new files... (Press Ctrl+C to stop)\n")

# Make sure the folder exists so the script doesn't crash
if not os.path.exists(FOLDER_TO_WATCH):
    os.makedirs(FOLDER_TO_WATCH)

# Get a starting list of files already inside the folder
existing_files = set(os.listdir(FOLDER_TO_WATCH))

# Run the monitor loop continuously
while True:
    try:
        # Pause for 2 seconds between checks so we don't overload the CPU
        time.sleep(2)
        
        # Check the folder contents again
        current_files = set(os.listdir(FOLDER_TO_WATCH))
        
        # Find if there are any new files (files in current but not in existing)
        new_files = current_files - existing_files
        
        # If a new file is detected, trigger the alert!
        for file_name in new_files:
            print(f"[ALERT] New file detected: {file_name}")
            
            # Send a real notification to the Windows screen
            notification.notify(
                title="⚠️ SECURITY ALERT",
                message=f"New file added to secure folder: {file_name}",
                app_name="System Monitor",
                timeout=5
            )
            
        # Update our list of existing files
        existing_files = current_files
        
    except KeyboardInterrupt:
        print("\n[*] Stopping System Monitor. Goodbye!")
        break
