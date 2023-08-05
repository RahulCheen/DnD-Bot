import discord
from discord import app_commands
from discord.ext import commands
import pandas as pd
import random

class DiceRoller(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Dice Roller cog loaded')

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f'Synced {len(fmt)} commands.')

    @app_commands.command(name="roll", description="Roll some dice. Submit 'help' for formatting help.")
    async def roll(self, interaction: discord.Interaction, input: str):
        try:
            split_rolls = input.lower().split("+")
            outcomes_data = {}
            for roll in split_rolls:
                if "d" in roll:
                    roll_values = roll.split("d")
                    n_dice = int(roll_values[0])
                    val_dice = int(roll_values[1])
                    for roll_num in range(n_dice):
                        outcomes_column = f"d{val_dice} #{roll_num+1}" if n_dice > 1 else f"d{val_dice}"
                        result = random.randint(1, val_dice)
                        outcomes_data[outcomes_column] = result
                else:
                    modifier = int(roll)
                    outcomes_data["Modifier"] = modifier

            total = sum(outcomes_data.values())
            outcomes_data["Roll Total"] = total

            outcomes = pd.DataFrame(outcomes_data, index=["Values"])
            
            msg = f"```{outcomes.to_string()}```"
            
        except:
            msg = """
Use format nds+nds+m where n is the number of dice, s is the number of sides, and m is the modifier.
Example: 2d6+4d4+3 to roll 2 d6 dice, 4 d4 dice, and add a +4 modifier to the roll.
To cast *Eldritch Blast* as a 1st level Warlock with the *Agonizing Blast* Eldritch invocation, use /roll 1d10+3
            """

        await interaction.response.send_message(msg)

async def setup(bot):
    await bot.add_cog(DiceRoller(bot))
