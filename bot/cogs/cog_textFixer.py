from discord.ext import commands
import re


class Fixer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.channel_id = 934586915796189215 
        self.regex = "(^\[).*(\]).*(\[H\]).{1,}(\[W\]).{1,}"
        self.regex2 = "(^\[).*(\]).*(\[W\]).{1,}(\[H\]).{1,}"

        with open("nonowords.txt", "r") as f:
            self.bad_words = f.read().splitlines()

    @commands.Cog.listener()
    async def on_message(self, message):
        rolly_exclude_ids = ["Admin", "Moderator", "Staff"]
        rolly_polly = message.author.roles

        admin_check = False
        for role in rolly_polly:
            if role.id in rolly_exclude_ids:
                admin_check = True

        # bad word checker upper
        gutted = False
        content_list = message.content.split()
        for word in content_list:
            if word in self.bad_words:
                gutted = True
                await message.delete()

        # format checker upper
        channel = message.channel.id
        valid_check = True if channel == self.channel_id else False

        if valid_check:
            if re.match(self.regex, message.content) or re.match(self.regex2, message.content) and not gutted:
                pass
            else:
                if not message.author.bot:
                    try:
                        await message.delete()
                        content = "Please use the following Format when posting:\n" \
                                  "[Location] [H] [W]\n" \
                                  "\nExample:\n" \
                                  "[USA-CA] Downtown SF [H] Vario, Infuser, DF64 in carbon. " \
                                  "[W] Local Cash preferably/venmo, could be open to shipping.\n"
                        await message.author.send(content=content)
                    except:
                        pass


def setup(client):
    client.add_cog(Fixer(client))
