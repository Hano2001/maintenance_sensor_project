================================================================================
MAINTENANCE SENSOR PROJECT
================================================================================

-------------------------------------------------------------------------------
DESCRIPTION
--------------------------------------------------------------------------------
 Description: A discord bot that handles sensors and their data using Sqlite
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
SYSTEM REQUIREMENTS & DEPENDENCIES
--------------------------------------------------------------------------------
discord.py, python-dotenv
--------------------------------------------------------------------------------
4. INSTALLATION & SETUP
--------------------------------------------------------------------------------
Step-by-step instructions to get the project running:
1. Clone the repository or download the files.
2. Create a virtual environment (venv) and activate it
3. pip install -r requirements.txt
4. Create an .env file and paste the token and name it TOKEN
5. Configure environment variables if necessary.

--------------------------------------------------------------------------------
5. USAGE
--------------------------------------------------------------------------------
Instructions on how to use the software or interpret the data files:
- paste the URL and choose what channel you want the bot to work in
- Run the main script: `python3 main.py`
- Commands:
    /tables - Creates a Sqlite table called sensors. - Admin only
    /populate - populates the sensors-table with dummy data - Admin only
    /addsensor [name] - creates a sensor with given name - Admin only
    /deletesensor [id] - Deletes the sensor of the ID provided - Admin only
    /sensors - Lists all the sensors and their info
    /status [id] - If no argument is provided, lists the current status of all the sensors,
            else current status of the sensor which ID is given in the argument.
    /checktable - lists all created tables

    

--------------------------------------------------------------------------------
6. FILE STRUCTURE
--------------------------------------------------------------------------------
Briefly explain what each main file or folder does:
- /database   - Contains the Sqlite database file.
- /cogs        - Contains the different bot commands.
- main.py     - Entry point of the application.
- README.txt  - This documentation file.

------------------------------------------------------------------------------
