import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()

# إنشاء البوت
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

# حدث عند تشغيل البوت
@bot.event
async def on_ready():
    print(f'✅ البوت {bot.user} جاهز الآن!')

# أمر ping بسيط
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'🏓 Pong! {round(bot.latency * 1000)}ms')

# أمر مرحبا
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'👋 مرحباً {ctx.author.mention}!')

# أمر معلومات المستخدم
@bot.command(name='info')
async def info(ctx):
    embed = discord.Embed(
        title=f"معلومات {ctx.author.name}",
        color=discord.Color.blue()
    )
    embed.add_field(name="الاسم", value=ctx.author.mention, inline=False)
    embed.add_field(name="الـ ID", value=ctx.author.id, inline=False)
    embed.add_field(name="تاريخ الإنشاء", value=ctx.author.created_at.strftime("%d/%m/%Y"), inline=False)
    await ctx.send(embed=embed)

# تشغيل البوت
token = os.getenv('DISCORD_TOKEN')
bot.run(token)
