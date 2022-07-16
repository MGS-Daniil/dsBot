import file.reload as rl
import time
import discord
from discord.ext import commands
from discord_components import Interaction, ActionRow, DiscordComponents, Button, ButtonStyle
from discord.utils import get
import datetime
import file.errors
import os
import sys
import json
#bot Daniil_85 Дата создания 30.09.2021 четверг

ffile = "file/"
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
voteIdTexts = {}
txt = "0"
with open(ffile+'daniil_85_ver.txt',"r") as file:
    txt = "daniil_85 v" + str(file.readlines(10))

def set(me):
    with open(ffile+"users.json", "r") as file:
        data = json.load(file)
        file.close()
    with open(ffile+"users.json", "w") as file:
        if me.name.lower() == "daniil6678":
            desk = "супер человек"
        desk = "Человек"
        data[str(me.id)] = {
            "N1": 0,
            "NAME": me.name,
            "WARNS": 0
        }
        json.dump(data, file, indent=6, )

@bot.event
async def on_ready():
    f = open(ffile + 'chlog.txt', 'r')
    console = bot.get_channel(int(f.readline(100)))
    DiscordComponents(bot)
    print("Bot connect")
    f.close()
    if not os.path.exists(ffile+'users.json'):
        with open(ffile+'users.json', 'w') as file:
            file.write("{}")
            file.close()
        for guild in bot.guilds:
            for member in guild.members:
                set(member)
    await console.send("bot connected")

@bot.command()
async def reload(ctx):
    try:
        rl.reload()
        await ctx.send(embed = discord.Embed(description="Успешно!", colour=discord.Color.green()))
    except:
        await ctx.send(embed=discord.Embed(description="Error! Сбой програмы", colour=discord.Color.red()))

@bot.command()
@commands.has_role("admin")
async def setreports(ctx, member: discord.Member, reason: str):
    if reason.lower() == "0" or reason.lower() == "1":
        set(member)

# @client.event
# async def on_member_join (member):
#     channel = client.get_channel ( 839807318162145290 )
#
#     role = discord.utils.get (member.guild.roles, id=839807022949335050)
#     print ('user join the servers')
#     await member.add_roles( role )
#     await channel.send( embed = discord.Embed( description = f'``{member.name}`` присоиединился', color = 0x0c0c0c))

@bot.event
async def on_member_join(member):
    await member.send(
        f"**Добро пожаловать на сервер _Main Test server_** \n"
        f"**Запрещено:**\n\n"
        f"**1.Эпилепсия**\n"
        f"Наказание: Мут\n\n"
        f"**2.18+**\n"
        f"Наказание: Мут\n\n"
        f"**3.Оскорбления**\n"
        f"Наказание: Мут\n\n"
        f"**4.Спам**\n"
        f"Наказание: Фриз\n\n"
        f"**5.Использование каналов не по назначению**\n"
        f"5.Использование каналов не по назначению\n\n"
        f"**6.Взлом учасника или бота**\n"
        f"Наказание: Бан\n\n"
        f"**7.Удаление чужих сообщений, не нарушающие правила**\n"
        f"Наказание: Фриз\n\n"
        f"**8.Упоминание без причины**\n"
        f"Наказание: Мут\n\n"
        f"**9.Отправка вредоносного ПО**\n"
        f"Наказание: Бан")

bot.remove_command('help')

@bot.command()
async def help(ctx):
    print(ctx.display_name)
    embed=discord.Embed(title = txt, color=0xCC0000)
    embed.set_author(name="помощь")
    embed.add_field(name="setreports", value="удаление жалоб с участника. Только admin'ам! !setreports @test 0", inline=True)
    embed.add_field(name="report", value="жалоба на участника !report @test", inline=True)
    embed.add_field(name="brush", value="сумма n+b", inline=True)
    embed.add_field(name="cat", value="giv", inline=True)
    embed.add_field(name="difference", value="вычетание n-b", inline=True)
    embed.add_field(name="divide", value="деление n/b", inline=True)
    embed.add_field(name="dog", value=" giv", inline=True)
    embed.add_field(name="hello", value="Здаровается", inline=True)
    embed.add_field(name="help ", value="Shows this message", inline=True)
    embed.add_field(name="multiply", value="умножение n*b", inline=True)
    embed.add_field(name="smile", value="эмодзи это-го сервера", inline=True)
    embed.add_field(name="perimeter", value="perimeter n*b", inline=True)
    embed.add_field(name="cube", value="3D cube n * b * c", inline=True)
    embed.add_field(name="vote", value="голосование (принять,отклонить)", inline=True)
    embed.add_field(name="date", value="выводит дату", inline=True)
    embed.add_field(name="reload", value="перезагружает данные", inline=True)
    embed.add_field(name="setlog", value="изменяет канал оповещения о включении бота. !Использовать сервер с ботом!", inline=True)
    embed.add_field(name="предупреждение", value="некоторые команды стоят с задержкой", inline=True)
    embed.add_field(name="test_command", value="новые команды (но тестовые)", inline=True)
    embed.set_footer(text="пока всё!")
    await ctx.send(embed=embed)

@bot.command()
async def report(ctx, member: discord.Member):

    with open(ffile+'users.json', 'r') as file:
        data = json.load(file)
        if data[str(member.id)]['WARNS'] >= 4:
            await ctx.send(embed = discord.Embed(title="❗❗📣ВНИМАНИЕ📣❗❗", description=f"У {member.name} уже {data[str(member.id)]['WARNS'] + 1} Жалоб!!!", colour=discord.Color.red()))
        file.close()

    with open(ffile+'users.json', 'w') as file:
        data[str(member.id)]['WARNS'] += 1
        json.dump(data, file, indent=6)
        file.close()
    await ctx.send(embed=discord.Embed(title="Жалоба отправлена.", colour=discord.Color.dark_gray))

@bot.command()
async def setlog(ctx, id):
    try:
        print("Новое Id: " + id)
        f = open(ffile+'chlog.txt', 'w')
        f.write("" + id)
        f.close()
        console = bot.get_channel(id)
        await ctx.send(embed = discord.Embed(description="Успешно! Оповещение о включении будет изменено после перезагрузки", colour=discord.Color.green()))
    except:
        await ctx.send(embed = discord.Embed(description="Error! неверное ID или сбой програмы", colour=discord.Color.red()))

@bot.command()
async def vote(ctx,*,title):
    try:
        msg= await ctx.send(
            embed=discord.Embed(title=title),
            components=[
                Button(style=ButtonStyle.green,label="Accept",emoji="✅"),
                Button(style=ButtonStyle.red, label="cancellation", emoji="❌")
            ]
        )
        voteIdTexts.update({msg.id:title})
    except:
        await ctx.send(embed = discord.Embed(description="используйте !vote [text]", colour=discord.Color.red()))

@bot.event
async def on_button_click(interaction):
    response = await bot.wait_for("button_click")
    name = voteIdTexts.get(response.message.id)
    if response.component.label == "Accept":
        await response.channel.send(response.author.mention + " принял,vote: " + name)
    else:
        await response.channel.send(response.author.mention + " не принял,vote: " + name)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(errors.MissingRequiredArgument)
    elif isinstance(error, commands.MissingRole) or isinstance(error, commands.MissingPermissions):
        await ctx.send(errors.MissingPerm)

@bot.command()
@commands.has_role('Python Developer')
async def unreport(ctx, mem: discord.Member, passw):
    if ctx.author.id == 849351619878715392:
        await ctx.delete()
        with open(ffile+"users.json", "r") as file:
            data = json.load(file)
            file.close()
        with open(ffile+'users.json', 'w') as file:
            data[str(member.id)]['WARNS'] -= 1
            json.dump(data, file, indent=6)
            file.close()
        await ctx.send('Успешно!')
    else:
        await ctx.send("Пользователь не вертифицырован!!")

#@bot.command() os._exit()
#async def bd(ctx, user):
#    enter = bd_enter(user)
#    await ctx.send(enter)
#
#def bd_enter(user):
#    for i in range(len(users)):
#        if user == usersId[i]:
#            enter = user + users[i]
#        else:
#            if user == botsId[i]:
#                enter = user + " обнаружен в базе... это - " + bots[i]
#            else:
#                enter = "Ошибка! User не найден. Использование !bd user#0000"
#            return enter

@bot.command()
async def hello(ctx, arg):
    await ctx.send("Добрый день, уважаемый " + arg + ", всего хорошего вам сегодня!)")

@bot.command()
async def date(ctx):
    with open(ffile+'time.txt', 'r') as file:
        d = file.readline(100)
        await ctx.send(d) \

@bot.command()
async def test_command(ctx):
    await ctx.send("тестовых команд пока нет😟😉 или вы о них не знаете🤐") \

@bot.command()
async def cat(ctx):
    await ctx.send("https://i.gifer.com/JtaW.gif")


@bot.command(name='dog', help='giv')
async def dog(ctx):
    await ctx.send("https://i.gifer.com/2g.gif")

@bot.command(help='perimeter')
async def perimeter(ctx,x,y):
    try:
        await ctx.send(int(x)*int(y))
    except:
        await ctx.send(embed=discord.Embed(description="Используйте цифры", colour=discord.Color.red()))

@bot.command(help='3D cube')
async def cube(ctx,x,y,z):
    try:
        await ctx.send(int(x)*int(y)*int(z))
    except:
        await ctx.send(embed=discord.Embed(description="Используйте цифры", colour=discord.Color.red()))

@bot.command(name='difference', help='вычетание')
async def difference(ctx, w, y):
    try: await ctx.send(int(w) - int(y))
    except: await ctx.send(embed=discord.Embed(description="Используйте цифры", colour=discord.Color.red()))

@bot.command(name='multiply', help='умножение')
async def multiply(ctx, w, y):
    try:
        await ctx.send(int(w) * int(y))
    except:
        await ctx.send(
            embed=discord.Embed(description="Используйте цифры", colour=discord.Color.red()))


@bot.command(name='divide', help='деление')
async def divide(ctx, w, y):
    if y=="0":
        await ctx.send("wes")
    else:
        await ctx.send(int(w) / int(y))


@bot.command(name='brush', help='сумма')
async def brush(ctx, w, y):
    await ctx.send(int(w) + int(y))



@bot.command(name='smile', help='эмодзи это-го сервера')
async def smile(ctx):
    await ctx.send("<:boteon:706935391852167208> ")


@bot.command(name='kick', help='КИКАЕТ ')
@commands.has_role('admin')
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


#@bot.event
#async def on_message(message):
#    if str(message.author)=="Daniii_85#0099" or str(message.author)=="bender#4678":
#        return
#    print(message.author)
#    if message.content=="hello":
#        await message.channel.send("hello")
#    await bot.process_commands(message)
fff = open(ffile+'danil_token.txt','r')
TOKEN = fff.readline(100)
fff.close()
bot.run(TOKEN)