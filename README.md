# Smart Inventory Automator

## Overview
This project solves the "out-of-stock" problem in small-scale environments (like a home office) by using threshold-based logic to trigger alerts.

## Setup
1. Ensure you have **Python 3.x** installed.
2. Clone this repo: `git clone [YOUR_URL]`.
3. Run the script: `python inventory_manager.py`.

## Features
- **Data Persistence:** Uses JSON to save state across sessions.
- **Threshold Logic:** Automatically flags items when they fall below a user-defined limit.