# test GitHub actions

from datetime import datetime

print("Hello, this is a test print from Python.")

with open("test.txt", "w") as file:
    file.write(f"Hello, this is a test write from Python. {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
