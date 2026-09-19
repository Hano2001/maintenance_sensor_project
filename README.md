# Maintenance Sensor Project

Discord bot for managing maintenance sensors and reading sensor data stored in SQLite.

## Description

The bot runs in your Discord server and exposes prefix commands (default prefix **`/`**) to create tables, add or remove sensors, populate test data, and query status.

## Requirements

- Python 3.9+
- Dependencies (see `requirements.txt`):
  - [discord.py](https://pypi.org/project/discord.py/) 2.7.1
  - [python-dotenv](https://pypi.org/project/python-dotenv/) 1.2.3

## Installation

1. Clone this repository.
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   # .venv\Scripts\activate    # Windows
   ```

3. Install packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Add a `.env` file in the project root:

   ```env
   TOKEN=your_discord_bot_token
   ```

5. Invite the bot to your server (Discord Developer Portal → OAuth2 → URL Generator), then choose the target channel.

## Usage

Start the bot:

```bash
python3 main.py
```

When the bot is online, run commands in Discord (messages starting with `/`).

## Commands

| Command              | Description                                                                       | Who           |
| -------------------- | --------------------------------------------------------------------------------- | ------------- |
| `/tables`            | Create the `sensors` SQLite table                                                 | Server admins |
| `/populate`          | Insert sample sensor rows                                                         | Server admins |
| `/addsensor <name>`  | Add a sensor with the given name, names with more than one word must be in qoutes | Server admins |
| `/deletesensor <id>` | Delete a sensor by ID                                                             | Server admins |
| `/sensors`           | List all sensors                                                                  | Anyone        |
| `/status`            | Status for all sensors                                                            | Anyone        |
| `/status <id>`       | Status for one sensor                                                             | Anyone        |
| `/checktable`        | List database tables                                                              | Anyone        |

## Project layout

```
maintenance_sensor_project/
├── cogs/           # Bot command modules (admin, status)
├── storage/        # SQLite database (database.db)
├── main.py         # Entry point
├── modules.py      # Shared helpers
├── classes.py      # Data models
└── requirements.txt
```
