<div align="center">

# 📂 Sortify

**Smart CLI File & Downloads Organizer for Linux**

![Platform](https://img.shields.io/badge/Platform-Linux-51A2DA?style=for-the-badge&logo=linux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![UI](https://img.shields.io/badge/Terminal_UI-Rich-1E1E2E?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-2EA043?style=for-the-badge)

</div>

---

## 📋 Overview

**Sortify** is a fast, lightweight Python CLI tool designed to automatically clean up cluttered directories (such as `~/Downloads` or `~/Unduhan`). Powered by `pathlib`, `shutil`, and `rich`, it organizes scattered files into structured subfolders without overwriting existing files.

## ✨ Key Features

- **🗂️ Dual Sorting Modes:** Organize files either by exact file extension (`--mode ext`, e.g., `pdf/`, `docx/`, `png/`) or broad categories (`--mode category`, e.g., `Documents/`, `Images/`, `Archives/`).
- **🛡️ Safe Dry-Run Preview:** Simulate file movements with `--dry-run` before touching any files on disk.
- **🔄 Collision Protection:** Automatically renames duplicate filenames (e.g., `file_1.pdf`) to prevent accidental data overwrites.
- **🌍 Locale-Aware Default:** Automatically detects `~/Unduhan` or `~/Downloads` as the default target folder.

---

## 📖 Tutorial: How to Use & Run in Terminal

### 1. Clone the Repository & Enter the Folder
```bash
git clone [https://github.com/Azyska/sortify.git](https://github.com/Azyska/sortify.git)
cd sortify
```

### 2. Set Up Virtual Environment & Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Sortify Commands
- **Preview cleanup safely (Dry-Run):**
  ```bash
  python3 sortify.py --dry-run
  ```
- **Organize default Downloads/Unduhan folder by extension:**
  ```bash
  python3 sortify.py
  ```
- **Organize by broad category (`Documents`, `Images`, etc.):**
  ```bash
  python3 sortify.py --mode category
  ```
- **Organize a custom directory:**
  ```bash
  python3 sortify.py --path ~/Desktop --dry-run
  ```

### 4. (Optional) Create a Global Terminal Alias
```bash
echo 'alias sortify="~/Projects/sortify/venv/bin/python ~/Projects/sortify/sortify.py"' >> ~/.bashrc
source ~/.bashrc
```

---

## 🛠️ CLI Command Reference

| Command | Description |
| :--- | :--- |
| `python3 sortify.py --dry-run` | Preview files to be moved without making changes |
| `python3 sortify.py` | Organize default `~/Unduhan` or `~/Downloads` by extension |
| `python3 sortify.py -m category` | Organize files into broad category folders |
| `python3 sortify.py -p <path>` | Specify a custom target directory |
| `python3 sortify.py --help` | Show CLI help message and options |

---

## 📂 Project Structure

```text
sortify/
├── sortify.py          # Main CLI entry point & sorting logic
├── requirements.txt    # Python dependencies (rich)
├── .gitignore          # Excludes virtual environment and bytecode caches
├── LICENSE             # MIT License
└── README.md           # Project documentation & terminal tutorial
```

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](./LICENSE) for more information.

---

<div align="center">
  <sub>Built on Fedora Linux by <a href="https://github.com/Azyska">Aziz Khoirul Setiawan</a></sub>
</div>
