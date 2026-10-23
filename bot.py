import os
import discord
from discord.ext import commands

# إعداد الصلاحيات (Intents)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح باسم: {bot.user.name}")

# أمر إرسال رسالة باسم البوت
@bot.command(name="قول")
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

# أمر إنشاء روم نصي جديد
@bot.command(name="روم_جديد")
@commands.has_permissions(manage_channels=True)
async def create_channel(ctx, *, channel_name):
    guild = ctx.guild
    new_channel = await guild.create_text_channel(channel_name)
    await ctx.send(f"تم إنشاء الروم بنجاح: {new_channel.mention}")

# أمر حذف الروم الحالي
@bot.command(name="حذف_روم")
@commands.has_permissions(manage_channels=True)
async def delete_channel(ctx):
    await ctx.channel.delete()

# أمر مسح عدد معين من الرسائل
@bot.command(name="مسح")
@commands.has_permissions(manage_messages=True)
async def clear_messages(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount + 1)

# تشغيل البوت باستخدام الـ Token المسجل في البيئة
TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(TOKEN)
