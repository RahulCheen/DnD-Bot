# DnD-Bot
 DnD mechanics helper discord bot

# Setup
 You will need a JSON in your parent directory with key "TOKEN" and "APP_ID" containing your bot's private token and application id respectively. These values must both be saved as strings.
 You will also need a JSON in your cogs directory with the key "APP_ID" corresponding to your bot's application id. This value must be saved as an integer.

# Initial features
 Dice rolling command to simulate dice rolling
 Use format nds+nds+m where n is the number of dice, s is the number of sides, and m is the modifier.
 Example: 2d6+4d4+3 to roll 2 d6 dice, 4 d4 dice, and add a +4 modifier to the roll. To cast *Eldritch Blast* as a 1st level Warlock with the *Agonizing Blast* Eldritch invocation, use /roll 1d10+3
