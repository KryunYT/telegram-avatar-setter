# Telegram Avatar Setter

This repository contains a Python script that uses the **Telethon** library to set multiple identical profile avatars on Telegram.

## Usage

1. Install the required dependency:

```bash
pip install telethon
```

2. Obtain your `api_id` and `api_hash` from the Telegram API development site at [my.telegram.org](https://my.telegram.org).

3. Place an avatar image named `avatar.jpg` in the same directory as the script.

4. Run the script and follow the prompts to enter your credentials and specify how many avatars to set:

```bash
python avatar_uploader.py
```

The script will upload the selected avatar multiple times and report how many avatars were set successfully.
