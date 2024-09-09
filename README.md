# Python Keyloggers

## Basic Python Keylogger Using `pynput`
This Python script implements a basic keylogger using the `pynput.keyboard` module to capture and log keystrokes. It logs the keys pressed by the user into a file (`keylogs.txt` or `output.txt`) and hides the console window to make it more discreet.

### Keylogger Features
1. **Keystroke Logging**: Logs every keystroke into a file, including special keys like spaces, enter, and others.
2. **Console Window Hidden**: Hides the console window for stealth, using the `win32api`, `win32console`, and `win32gui` modules.
3. **Termination with Ctrl+E**: The keylogger can be terminated by pressing the Ctrl+E combination.

### Prerequisites
Make sure you have the following Python modules installed:
- `pynput`: To capture keyboard inputs.
- `pywin32`: To manipulate the Windows console window.

Install them using pip:
```bash
pip install pynput pywin32
```
### Example Output
The log file (`keylogs.txt`) will contain entries like this:

```bash
    2023-09-09 12:34:56,789: 'a'
    2023-09-09 12:34:57,123: 'b'
    2023-09-09 12:34:57,456: Key.space
```

## Enhanced Keylogger with Hidden Console and Custom Logging `StealthKey`
This version hides the console window and allows better handling of special keys.

### How It Works
 1. **Logging**: The script listens for keystrokes and logs them into output.txt. If a special key is pressed (e.g., space or enter), it logs a symbol for it.
 2. **Exiting the Keylogger**: The keylogger can be terminated by pressing the Ctrl+E key combination.

## Disclaimer:
This script is intended **strictly for educational purposes**. It is designed to demonstrate how keylogging works, as part of security research and learning. Unauthorized use of keyloggers or any similar software to record keystrokes without explicit consent from the user is **illegal** and violates privacy laws in many countries.

By using this script, you agree to the following:
- You will not use this script in any way that violates local, state, national, or international law.
- You will not use this script for any malicious purposes, including but not limited to unauthorized access to personal data or passwords.
- The developer(s) of this script hold no responsibility for any misuse or damage caused by this code.

Use responsibly and ethically, and always seek permission from the user before logging their keystrokes.
