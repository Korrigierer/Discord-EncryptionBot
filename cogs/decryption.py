import discord
from discord import app_commands
from discord.ext import commands

from encryptions.base64 import base64_decode
from encryptions.caesar import caesar_cipher


class Decryption(commands.GroupCog, name="decrypt"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(name="caesar", description="Decrypts a message using caesar cipher")
    @app_commands.describe(message="The message that should be decrypted")
    async def caesar_decrypt(self, interaction: discord.Interaction, message: str, shift: int):
        await interaction.response.send_message(f"Your message: {message}\nDecrypted Message: {caesar_cipher(message, -shift)}", ephemeral=True)

    @app_commands.command(name="base64", description="Decrypts a message using base 64")
    @app_commands.describe(message="The message that should be decrypted")
    async def base64_encrypt(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(f"Your message: {message}\nDecrypted Message: {base64_decode(message)}", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Decryption(bot), guilds=[discord.Object(id=1060144669482287124)])
