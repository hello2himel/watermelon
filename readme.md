# 🍉 Watermelon App

A playful yet profound desktop app written in Python using Tkinter. At first glance, it seems like just a quirky little virus—every time you close a watermelon window, it multiplies. But dig a little deeper, and you'll find something more.  

**This app is a metaphor for how destruction often leads to creation. Each watermelon window that spawns is a symbol of the perpetual cycle of life—how even in moments of chaos and apparent destruction, something new and unexpected is born. It’s a reminder that our actions, no matter how small, ripple out into the world, creating endless possibilities.**

> "When you destroy a watermelon, you spread its seeds."

Each window that spawns carries the idea that even in destruction, there is creation. It’s a reminder of the cyclical nature of things—how the smallest actions can ripple out, creating endless possibilities. Perhaps chaos, too, has its own kind of order.  

---

## 📚 Table of Contents
- [What It Does](#what-it-does)
- [Screenshots](#screenshots)
- [How It Works](#how-it-works)
- [How to Run](#how-to-run)
- [How to Export](#how-to-export)
  - [For Linux](#for-linux)
  - [For Windows (32-bit or 64-bit)](#for-windows-32-bit-or-64-bit)
- [Dependencies](#dependencies)
- [License](#license)

---

## 🌀 What It Does

- Displays a watermelon image and a message.
- If you close the window, it:
  - Opens 2 more windows,
  - Replaces the watermelon with seeds,
  - Shows a dialog: _"When you destroy a watermelon, you spread its seeds."_
- Every window behaves the same. It multiplies forever.

---

## 📸 Screenshots

*(Insert screenshots or GIFs here)*

---

## ⚙️ How It Works

- Built using `Tkinter` and `Pillow`
- Recursively spawns new windows on close
- Uses image swapping and message boxes for effects
- Packaged into a standalone executable for Linux and Windows

---

## ▶️ How to Run

Clone the repo:

```bash
git clone https://github.com/yourusername/Watermelon-App.git
cd Watermelon-App
```

Create a virtual environment (optional but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run it:

```bash
python app.py
```

---

## 📦 How to Export

### ✅ For Linux

Make sure PyInstaller is installed:

```bash
pip install pyinstaller
```

Export to a single `.AppImage`-style executable:

```bash
pyinstaller --onefile --windowed \
  --add-data "res/watermelon.png:res" \
  --add-data "res/seeds.png:res" \
  app.py
```

Result: `dist/app` ← you can double-click this to run.

---

### 🪟 For Windows (32-bit or 64-bit)

Install Python for Windows (32-bit recommended for max compatibility). Then:

```bash
pip install pyinstaller
```

Build it:

```bash
pyinstaller --onefile --windowed ^
  --add-data "res\\watermelon.png;res" ^
  --add-data "res\\seeds.png;res" ^
  app.py
```

Result: `dist/app.exe` ← fully portable. No Python required.

---

## 📦 Dependencies

Listed in `requirements.txt`, but in case you need them:

```txt
Pillow
```

Also uses `tkinter`, which comes built-in with Python on most platforms.

---

## 📝 License

MIT License. Do whatever you want. Share the chaos 🌱

---
