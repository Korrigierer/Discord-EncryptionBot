import discord
from discord import app_commands
from discord.ext import commands

from encryptions.base64 import base64_encode
from encryptions.caesar import caesar_cipher


class Encryption(commands.GroupCog, name="encrypt"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(name="ceesar", description="Encrypts a message using caesar cipher")
    @app_commands.describe(message="The message that should be encrypted", shift="the shift that is used")
    async def caesar_encrypt(self, interaction: discord.Interaction, message: str, shift: int):
        await interaction.response.send_message(f"Your message: {message}\nShift: {shift}\nEncrypted Message: {caesar_cipher(message, shift)}", ephemeral=True)

    @app_commands.command(name="base64", description="Encrypts a message using base 64")
    @app_commands.describe(message="The message that should be encrypted")
    async def base64_encrypt(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(f"Your message: {message}\nEncrypted Message: {base64_encode(message)}", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Encryption(bot), guilds=[discord.Object(id=1060144669482287124)])
