from discord.ext import commands
import discord
import datetime
import json



TOKEN = ''

bot = commands.AutoShardedBot(command_prefix="!")

class EmptyMemberError(Exception):
    pass
class NotMemberError(Exception):
    pass

def terror_checker(member: discord.Member=None):
    if member is None:
        raise EmptyMemberError("member 인자가 None 값일 수 없습니다.")
    elif type(member) != discord.Member:
        raise NotMemberError("member 인자는 반드시 discord.Member 타입이어야 합니다.")
    #a = member.joined_at - datetime.date.today()
    elif round((datetime.datetime.utcnow() - member.created_at).total_seconds()) < 600: #만약 계정을 만든지 10분이 지나지 않았다면
        return "위험"
    elif round((datetime.datetime.utcnow() - member.created_at).total_seconds()) > 600: #아니라면
        return "통과"
    else: #ㅅㅂ 모르겠다면
        return "에러"
        


@bot.event
async def on_member_join(member):
    embed = discord.Embed(
        title = f"{member} 님이 들어오셨습니다."
    )
    danger = terror_checker(member)
    if danger == "위험":
        embed.colour = discord.Colour.red()
    if danger == "통과":
        embed.colour = discord.Colour.green()
    if danger == "에러":
        embed.colour = discord.Colour.gold()
    embed.add_field(
        name="안전 여부",
        value=danger
    )
    await bot.get_channel(690925568744620054).send(embed=embed)
@bot.command()
async def test(ctx, member: discord.Member):
    await ctx.send(str((datetime.datetime.utcnow() - member.created_at).total_seconds()))

bot.run(TOKEN)
