# 🚀 Daily Routine Automation & Scheduling

This project is a Python script developed to automate the start of the work and study routine. It combines web automation (to open tabs and log into essential platforms) and system commands (to schedule an automatic computer shutdown).

The goal is to save time every day by executing repetitive tasks with a single click!

---

## 🛠️ Features

1.  **Automatic Shutdown Scheduling:** Calculates the exact time and schedules a silent PC shutdown for a specific time (e.g., 14:28). Includes a visual pop-up alert on the screen confirming the schedule.
2.  **Clean Browser Launch:** Opens Google Chrome in Incognito and Dark Mode, bypassing basic automation banners to avoid detection.
3.  **Automated Sequential Logins:**
    * **Google / Gmail:** Fills in email and password and accesses the inbox.
    * **Google Gemini:** Opens in a new tab and waits for it to load.
    * **GitHub:** Navigates to the login page, inserts credentials, and accesses the main dashboard.
    * **SENAI Student Portal:** Opens the student portal login page (Note: Auto-filling this specific page is currently under development due to Flutter framework restrictions).
4.  **Final Search Tab:** Leaves an extra blank Google tab open, ready to start working.

---

## 💻 Prerequisites and Installation

To run this project on your machine, you will need **Python** and **Google Chrome** installed.

1. Download or clone this project to your computer.
2. Open the terminal (or command prompt) in the project folder.
3. Install the necessary libraries by running the following command:

    ```bash
    pip install selenium webdriver-manager pyautogui
    ```

---

## 🔐 Tutorial: Configuring your Credentials (IMPORTANT)

For the robot to log in for you, it needs to know your emails and passwords. However, **we must NEVER put passwords directly in the main code (`main.py`)**. 

To keep your accounts secure, we use a separate file called `Credentials.py`. Follow the step-by-step guide below to configure it:

### Step 1: Create the file
In the same folder where your main automation script is located, create a new text file and name it exactly: `Credentials.py`

### Step 2: Copy the template
Open the `Credentials.py` file you just created and paste the code below into it:

    ```python
    # Google Credentials
    email = "YOUR_EMAIL_HERE@gmail.com"
    password = "YOUR_GOOGLE_PASSWORD_HERE"

    # GitHub Credentials
    github_email = "YOUR_GITHUB_USER_OR_EMAIL"
    github_password = "YOUR_GITHUB_PASSWORD_HERE"

    # SENAI Credentials
    senai_user = "YOUR_CPF_OR_EMAIL_HERE"
    senai_password = "YOUR_SENAI_PASSWORD_HERE"
    ```

### Step 3: Fill with your real data
Replace the generic texts (like `"YOUR_EMAIL_HERE@gmail.com"`) with your real data. 
**Attention:** Keep the double quotes (`" "`) around your emails and passwords!

### Step 4: Protect the file (GitHub Warning)
If you are going to upload this project to GitHub or any other version control system, **you must ignore the credentials file**. 
Create a file called `.gitignore` in the same folder and write only this inside it:
    
    Credentials.py

This ensures GitHub ignores your password file and only uploads the robot's code.

---

## ▶️ How to Run the Project

With the libraries installed and the `Credentials.py` file configured, you are ready to go!

Open your terminal in the project folder and run the main script (replace `your_file_name.py` with the actual name of your script):

    ```bash
    python your_file_name.py
    ```

**What will happen:**
1. A pop-up will appear confirming in how many seconds your PC will shut down.
2. Google Chrome will open by itself in incognito mode.
3. Do not move your mouse or keyboard while the robot is working.
4. At the end, you will have all your tabs logged in and ready to use!