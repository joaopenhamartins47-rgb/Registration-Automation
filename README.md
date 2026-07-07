# Registration Automation

First episode of the Hashtag Treinamentos course, where we learned about the pyautogui library. The goal of the project is to automate a product database registration process, saving hours of manual work.

The script reads a CSV with the products (code, brand, type, category, unit price, cost, and notes) and fills in each field by itself on a web system, simulating keyboard and mouse, until it finishes the whole list.

The code was built specifically to solve this automation problem in Hashtag's training environment. The email and password are just illustrative, on a site with no real login verification, and the screen coordinates were set based on my screen positions, at 1920x1080 resolution (so running it on a different resolution will probably break the clicks).

Other than that, it solves a real repetitive manual registration problem and shows a bit of what pyautogui automation can do.

Stack: Python, pandas (CSV reading) and pyautogui (mouse and keyboard simulation).

To run: `uv sync` then `uv run codigo.py`.