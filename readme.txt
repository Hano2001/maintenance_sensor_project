# Maintenance Sensor Project

## Description

A **Discord bot** that manages sensors and their data using **SQLite**.

## System Requirements & Dependencies

- **Python 3** (recommended)
- **discord.py**
- **python-dotenv**

Install Python packages via `requirements.txt` (see Installation).

## Installation & Setup

1. Clone the repository or download the project files.
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root and add your bot token:
   ```env
   TOKEN=your_discord_bot_token_here
   ```
5. Configure any other environment variables if your setup requires them.

## Usage

1. Paste the bot invite URL in your browser and choose the Discord server and channel where the bot should operate.
2. Start the bot:
   ```bash
   python3 main.py
   ```

### Commands

| Command | Description | Access |
|--------|-------------|--------|
| `/tables` | Creates the SQLite table `sensors`. | Admin only |
| `/populate` | Fills the sensors table with dummy data. | Admin only |
| `/addsensor [name]` | Creates a sensor with the given name. | Admin only |
| `/deletesensor [id]` | Deletes the sensor with the given ID. | Admin only |
| `/sensors` | Lists all sensors and their information. | Everyone |
| `/status [id]` | Without an ID: status of all sensors. With an ID: status of that sensor. | Everyone |
| `/checktable` | Lists all created database tables. | Everyone |

## File Structure

| Path | Purpose |
|------|---------|
| `storage/` | SQLite database (`database.db`) |
| `cogs/` | Discord slash commands and bot logic |
| `main.py` | Application entry point |
| `readme.txt` | Project documentation (this file) |
