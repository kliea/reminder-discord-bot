# Reminder Discord Bot

A simple Discord bot that sends daily countdown reminders to a specified channel until an event date.

## Features

- Sends a daily reminder at 8 PM UTC with a countdown to the event.
- Allows users to check the remaining time using the `/countdown` command.
- Uses `.env` file for storing sensitive credentials securely.

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/kliea/reminder-discord-bot.git
cd reminder-discord-bot
```

### 2. Create a Virtual Environment (Optional but Recommended)

```sh
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure the `.env` File

Create a `.env` file in the project directory and add:

```
BOT_TOKEN=your_discord_bot_token
CHANNEL_ID=your_channel_id
```

### 5. Run the Bot

```sh
python bot.py
```

## Commands

- `/countdown` → Check the remaining time until the event.

## Notes

- Make sure your bot has the necessary permissions to send messages.
- Keep your `.env` file safe and **never commit it to GitHub**.

## Contributing

Pull requests are welcome! Please open an issue first to discuss major changes.

## License

This project is licensed under the MIT License. Feel free to use and modify it.

---

### Author

Developed by [kliea](https://github.com/kliea) 🚀
