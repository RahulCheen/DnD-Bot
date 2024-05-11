import discord
from discord import app_commands
from discord.ext import commands
import requests
import json
import random

class MonsterIndex(commands.Cog):
    URL = "https://www.dnd5eapi.co/api/monsters"
    PAYLOAD = {}
    HEADERS = {
        'Accept': 'application/json'
    }
    
    def __init__(self, bot: commands.Bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Monster Index cog loaded')

    def get_random_monster(self, challenge=None):
        url = self.URL
        if challenge:
            url += f'?challenge_rating={challenge}'
        response = requests.request("GET", url, headers=self.HEADERS, data=self.PAYLOAD)
        monster_list = json.loads(response.text)
        
        count = monster_list['count']
        idx = random.randrange(count)
        rand_monster = monster_list['results'][idx]
        
        return rand_monster
    
    def get_monster_dat(self, monster):
        monster_url = self.URL+'/'+monster.lower()
        response = requests.request("GET", monster_url, headers=self.HEADERS, data=self.PAYLOAD)
        monster_dat = json.loads(response.text)
        
        return monster_dat
        
    
    def format_stat_block(self, monster):
        lines = []
        lines.append(f"# **Name:** {monster['name']}")
        lines.append(f"### **Size/Type/Alignment:** {monster['size']} / {monster['type']} / {monster['alignment']}")
        lines.append(f"### **Armor Class:** {monster['armor_class'][0]['value']} ({monster['armor_class'][0]['type']})")
        lines.append(f"### **Hit Points:** {monster['hit_points']} ({monster['hit_points_roll']})")
        lines.append(f"### **Speed:** {monster['speed']['walk']}")
        lines.append("")
        lines.append("# Stats:")
        lines.append(f"###  **STR:** {monster['strength']}  **DEX:** {monster['dexterity']}  **CON:** {monster['constitution']}  **INT:** {monster['intelligence']}  **WIS:** {monster['wisdom']}  **CHA:** {monster['charisma']}")
        lines.append("")
        lines.append("### Proficiencies:")
        for proficiency in monster['proficiencies']:
            lines.append(f"  - **{proficiency['proficiency']['name']}:** +{proficiency['value']}")
        lines.append("")
        lines.append("### Senses:")
        lines.append(f"  **Passive Perception:** {monster['senses']['passive_perception']}")
        lines.append(f"### Languages:")
        lines.append(f"{monster['languages']}")
        lines.append(f"### Challenge Rating:")
        lines.append(f"{monster['challenge_rating']} (XP: {monster['xp']})")
        lines.append("")
        lines.append("### Special Abilities:")
        for ability in monster['special_abilities']:
            lines.append(f"  - **{ability['name']}:** {ability['desc']}")
        lines.append("")
        lines.append("### Actions:")
        for action in monster['actions']:
            lines.append(f"  - **{action['name']}:** {action['desc']}")
            if 'damage' in action:
                damage_info = ", ".join([f"{d['damage_dice']} {d['damage_type']['name']} damage" for d in action['damage']])
                lines.append(f"    **Damage:** {damage_info}")
        
        return "\n".join(lines)
        
    @app_commands.command(name='monster', description='Get a random monster!')
    async def rand_monster(self, interaction: discord.Interaction):
        random_monster = self.get_random_monster()
        monster_dat = self.get_monster_dat(random_monster['index'])
        monster_stats = self.format_stat_block(monster_dat)

        await interaction.response.send_message(monster_stats)
        
    @app_commands.command(name='monster_by_cr', description='Get a random monster by CR!')
    async def rand_monster_cr(self, interaction: discord.Interaction, input: str):
        try:
            random_monster = self.get_random_monster(challenge=input)
        except ValueError:
            await interaction.response.send_message(f'No monster with cr{input} found')
            return
        monster_dat = self.get_monster_dat(random_monster['index'])
        monster_stats = self.format_stat_block(monster_dat)
        
        await interaction.response.send_message(monster_stats)

async def setup(bot):
    await bot.add_cog(MonsterIndex(bot))
