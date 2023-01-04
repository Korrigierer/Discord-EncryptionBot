import discord
from discord.ext import commands
import os

import glob

# invite : https://discord.com/api/oauth2/authorize?client_id=1060142238551777300&permissions=414464855104&scope=bot%20applications.commands


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="?",
            intents=discord.Intents.all(),
            application_id=os.getenv("APP_ID"),
            strip_after_prefix=True,
        )

    async def setup_hook(self) -> None:
        print(f"{self.user} has connected to Discord!")

        # Load Jishaku extension.
        await self.load_extension("jishaku")

        # Load extensions that are inside your Cogs folder.
        for cog in glob.glob("cogs/**/*.py", recursive=True):
            await self.load_extension(
                cog.replace("\\", ".").replace("/", ".").removesuffix(".py")
            )

    # Close bot and connections.
    async def close(self) -> None:
        await super().close()


if __name__ == "__main__":
    bot = MyBot()
    bot.run(os.getenv("TOKEN"), reconnect=True)
