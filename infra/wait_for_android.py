import subprocess
import time
import sys

CONTAINER_NAME = "android-container"
STATUS_FILE = "device_status"
EXPECTED_STATUS = "READY"
SLEEP_SECONDS = 5
TIMEOUT_SECONDS = 300

print("⏳ Aguardando device ficar READY...")

start_time = time.time()

while True:
    try:
        result = subprocess.check_output(
            ["docker", "exec", "-i", CONTAINER_NAME, "cat", STATUS_FILE],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()
    except subprocess.CalledProcessError:
        result = ""

    print(f"📱 Status atual: '{result}'")

    if result == EXPECTED_STATUS:
        print("✅ Device está READY!")
        sys.exit(0)

    if time.time() - start_time > TIMEOUT_SECONDS:
        print(f"❌ Timeout após {TIMEOUT_SECONDS}s aguardando o device ficar READY")
        sys.exit(1)

    time.sleep(SLEEP_SECONDS)
