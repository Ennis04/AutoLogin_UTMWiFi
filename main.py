import subprocess
import requests
import time

# WiFi and Login Credentials
WIFI_NAME = "UTMWiFi"
LOGIN_URL = "https://wifi.utm.my/login.php"
USERNAME = "ennis"
PASSWORD = "Ennis04*"

# Function to check if connected to UTMWIFI
def is_connected_to_wifi():
    result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
    return WIFI_NAME in result.stdout

# Function to connect to UTMWIFI
def connect_to_wifi():
    subprocess.run(["netsh", "wlan", "connect", f"name={WIFI_NAME}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Function to check if internet is available
def is_internet_available():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Function to log in to UTMWIFI
def login_to_wifi():
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

    session = requests.Session()
    response = session.post(LOGIN_URL, data=payload, headers=headers)

    if "success" in response.text.lower():  # Modify this based on the actual response message
        print("✅ Login successful!")
    else:
        print("❌ Login failed. Check credentials or login form structure.")

# Main Logic
while not is_connected_to_wifi():
    print("🔄 Connecting to UTMWIFI...")
    connect_to_wifi()
    time.sleep(5)

print("✅ Connected to UTMWIFI.")

if not is_internet_available():
    print("🔄 Logging in to WiFi...")
    login_to_wifi()
else:
    print("✅ Already connected to the internet!")
