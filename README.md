# Organize_files

Organize_files is a small, easy-to-use tool (written in Python) that helps you organize files into folders based on configurable rules. If you just want to use it quickly, there's a prebuilt binary available — simply download the `dist` folder and run the `.exe` file.

This README explains what the project does, how to use the prebuilt executable, how to run from source, and provides tips for troubleshooting and contributing.


<img width="597" height="488" alt="image" src="https://github.com/user-attachments/assets/b1705f0b-68e2-4923-97c5-7c6b1162f8ba" />


## Features

- Sort files into folders by extension, size.
- Lightweight and fast — suitable for ad-hoc cleanup tasks.
- Prebuilt executable available for quick use (Windows).
- Can be run from source with Python for customization.

## Quick Start — Run the prebuilt executable (recommended)

1. Download the `dist` directory from this repository's releases or the `dist` folder in the repo.
2. Inside `dist`, locate the `.exe` file (for example `Organize_files.exe`).
3. Run the executable:
   - Double-click the `.exe` file in File Explorer
   - OR run it from a Command Prompt:
     ```
     C:\path\to\dist\Organize_files.exe
     ```
4. Follow the on-screen prompts (if any). The program will organize files according to its bundled default rules.

Notes:
- The prebuilt executable is provided for Windows. If you're on macOS / Linux, see "Run from source" below.
- If Windows Defender or other antivirus warnings appear, you may need to allow the executable or run it after verifying the source.

## Run from source

If you want to inspect or customize the tool, run it from source:

1. Clone the repo:
   ```
   git clone https://github.com/UNKN0WN4O4/Organize_files.git
   cd Organize_files
   ```
2. Create a virtual environment (recommended) and install dependencies:
   ```
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate

   pip install -r requirements.txt
   ```
   If there is no requirements.txt, the script may require only the Python standard library.
3. Run the main script:
   ```
   python organize_files.py
   ```
4. Configure rules or modify code as you need.

## Typical Usage Patterns

- Quick local cleanup:
  - Place the executable or run the script in the folder containing files you want to organize.
  - Run it and let it create folders and move files based on the bundled rules.

- Scheduled or automated runs:
  - Use Windows Task Scheduler or a cron job to run the script periodically.
  - If using the exe, call it from a scheduled task:
    ```
    C:\path\to\dist\Organize_files.exe --target "C:\Users\You\Downloads"
    ```
  - (If the exe supports CLI args — consult the source for supported arguments.)


Always test changes on a small folder before running on important data.

## Troubleshooting

- The executable won't start / shows a security warning:
  - Right-click -> Properties -> Unblock, or allow in your antivirus if you trust the source.

- No `dist` folder or exe present:
  - Build it from source with PyInstaller (if comfortable), or run the Python script directly.

## Building your own executable (optional)

If you want to build the `.exe` yourself (using PyInstaller):

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. From the repo directory:
   ```
   pyinstaller --onefile organize_files.py
   ```
3. The generated executable will be in `dist/`.

## Contributing

Contributions are welcome. Recommended workflow:
1. Fork the repo.
2. Create a branch for your feature/fix.
3. Make changes and include tests where sensible.
4. Open a pull request describing the change.

Please include clear descriptions for configuration changes or behavioral changes.


## Contact / Support

If you have issues or feature requests, open an issue on the repository (https://github.com/UNKN0WN4O4/Organize_files/issues).

Enjoy organizing!
