# DnD-Bot
 DnD mechanics helper discord bot

# Setup
 In main directory, you need a .py file named config.py with variables TOKEN and APP_ID set equal to your bot's private token and application id (both as strings). This is imported in mainbot.py

# Initial features
 Dice rolling command to simulate dice rolling
 Use format nds+nds+m where n is the number of dice, s is the number of sides, and m is the modifier.
 Example: 2d6+4d4+3 to roll 2 d6 dice, 4 d4 dice, and add a +4 modifier to the roll. To cast *Eldritch Blast* as a 1st level Warlock with the *Agonizing Blast* Eldritch invocation, use /roll 1d10+3
