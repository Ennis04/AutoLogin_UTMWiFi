# AutoLogin_UTMWiFi
This is a simple python program which helps you to auto login and connects to UTMWifi.

---

<h2>🛠️Installation & Setup</h2>

**1️⃣ Install Python**

If you are not sure whether Python is installed:

**Check Whether Python is Installed:**
1. Open **Command Prompt** (Win + R, type **cmd**, press **Enter**).
2. Type **python --version**, if it shows "Python was not found", follow the step below to install.

**Install Python:**
1. Download Python using the link https://www.python.org/downloads/.
2. Run the downloaded **Python Installer**.
3. **Tick the box "Add Python to PATH"** before installing.
4. After installation, restart your PC.
5. Use the steps stated above to check whether Python is installed.

**2️⃣ Install Visual Studio Code (VS Code)**

Download VS Code using the link https://code.visualstudio.com/.

**3️⃣ Install Python Extension and Requests Module in VS Code**
1. Open VS Code.
2. Open **Extensions** panel (Ctrl + Shift + X).
3. Install **Python** (by Mircosoft).
4. Open **VS Code Terminal**.
5. Type **pip install requests**.


**4️⃣ Clone this Repository**
1. Open **Command Prompt** (Win + R, type **cmd**, press **Enter**).
2. Navigate to the folder where you want to store the project.
3. **git clone https://github.com/Ennis04/AutoLogin_UTMWiFi.git**
4. Navigate to the project folder

**5️⃣Edit your Data**
1. Open "**main.py**".
2. Change and update your Username and Password.
3. Run with debugger (Ctrl + F5).


**6️⃣Set Up Auto-Login on Windows Startup**
1. Press **Win + R**, type **taskchd.msc** and press **Enter**.
2. Click "**Create Basic Task**" and name it as UTMWiFi AutoLogin.
3. At the Trigger section, select "**When I log on**".
4. At the Action section, select "**Start a Program**".
5. Browse for "**python.exe**".
6. Add a the "**main.py**" file path in the arguement.
7. Click **Finish**.

---

<h2>Disable Auto-Login</h2>

If you want to disable it:
1. Press **Win + R**, type **taskchd.msc** and press **Enter**.
2. Go to **Task Scheduler Library**, find UTMWiFi AutoLogin.
3. Click **Disable/ Delete**.

---

## 📌 Credits

- Developed by [Ennis Lam Si Hooog](https://github.com/ennis04)
- Assisted by ChatGPT (https://openai.com/chatgpt)
