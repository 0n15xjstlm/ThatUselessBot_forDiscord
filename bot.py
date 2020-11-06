import discord
from discord.ext import commands
from config import settings
import json
import requests
import random
from vzlom_pentagon import Vzlom
bot = commands.Bot(command_prefix=settings['prefix'])
client = discord.Client()

bot.remove_command('help')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@bot.command()
async def light(ctx):
    await ctx.send("ВкЛюЧиТь СвЕтЛуЮ тЕмУ дЛя ДиСкОрДа!!! ВоТ сСыЛкА http://www.clickbait.pro/")

@bot.command()
async def who(ctx):
    await ctx.send(""">>> загадка от Фака Жреско
    
    КТО?

на размышление дается 30 секунд
    """)
    await ctx.send("https://yt3.ggpht.com/a/AATXAJxZQcl06uZvSpv6zkgOUveBOwfnpgeEYOz5gw-n-g=s900-c-k-c0xffffffff-no-rj-mo")
@bot.command()
async def chell(ctx):
    await ctx.send("Все ясно автор бота CHELL")


@bot.command()
async def cat(ctx):
    await ctx.send('а ты шаришь')
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
    await ctx.send("(кста это создатель бота в данное время)")

@bot.command()
async def joke(ctx):
    await ctx.send('колобок повесился :rofl: ')

@bot.command()
async def help(ctx):
    await ctx.send("""
>>> ***Список команд:***
   **Веселье**
    *:chell - узнать кто создатель бота*
    *:light - лигхт. лол че тут еще может быть*
    *:cat - а ты шаришь*
    *:who - сам узнай...*
    *:joke - расскажу шутку*
    *:auf - АУФ!*
    *:vzlom - взломай чето там...*
    *:pika - рандомный пика-пикачу)*
    *:meme - рандомный ОнГлЕсКиЙ мем*
    *:ideas - полезные идеи!*
   **Помощь**
    *:help - помощь (как неожиданно!)*
    *:prefix - показывает текущий префикс для команд бота.*
    *:v - версия бота*
   **Полезные (реально) функции**
    *:contact - связь с создателем бота*
    *:info - инфа про бота* 
    *:iqtest - тест на И_Ку*
    *:playlist (calm, dance, work, gaming, chilledcow)- скину плейлист с музыкой*
    *:motivate - нужна мотивация? Получай!*""")

@bot.command()
async def contact(ctx):
    await ctx.send(">>> Нашел баг? Пиши сюда! justlm228@ya.ru!!!")
@bot.command()
async def info(ctx):
    await ctx.send(""">>> Привет! Я бесполезный бот. 
    
Ты можешь добавить меня на свой сервер (а зачем) вот этой ссылкой: 
https://discord.com/api/oauth2/authorize?client_id=770657827256664124&permissions=8&scope=bot

Я являюсь творением justLM'а, тупого школьника который могет в программирование.

Для связи с создателем есть команда .contact!

Claimed by ThatUselessBot. 2020""")

@bot.command()
async def auf(ctx):
    await ctx.send(">>> Волк - это не работа. Работа - это ворк, а волк - это ходить. АУФ! :point_up_2:")
    await ctx.send("https://i.ytimg.com/vi/LxkQ8O6VMfA/maxresdefault.jpg")

@bot.command()
async def vzlom(ctx):
    Vzlom.vzlomat("да")
    Vzlom.codeVzloma("да")
    await ctx.send("``` Поздравляем! Вы взломали пентагон и свою жопу! Вам доступно: тюрьма, тюрьма2 ```")
    await ctx.send("https://i.gifer.com/7zog.gif")
    await ctx.send("я предупреждал...")
    await ctx.send("https://media1.tenor.com/images/a8dc67a6724059f2da5837c76ad38c72/tenor.gif")

@bot.command()
async def meme(ctx):
    response = requests.get("https://some-random-api.ml/meme")  # Get-запрос
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0x756D6D, title="МЕМЧЕГ (онглейский)",)  # Создание Embed'a
    embed.set_image(url=json_data['image'])  # Устанавливаем картинку Embed'a
    await ctx.send(embed=embed)  # Отправляем Embed
@bot.command()
async def pika(ctx):
    response = requests.get('https://some-random-api.ml/img/pikachu')  # Get-запрос
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0xff9900, title='рандомная гифка пикачу?')  # Создание Embed'a
    embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
    await ctx.send(embed=embed)  # Отправляем Embed

@bot.command()
async def prefix(ctx):
    await ctx.send("***ТЕКУЩИЙ ПРЕФИКС БОТА: [:]***")

@bot.command()
async def rules(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/736507272158511144/752928415761563749/kowalski-1-1-1-1.gif")

@bot.command()
async def iqtest(ctx):
    iq = random.randint(-5, 15)
    await ctx.send("Сканируется ваш аккаунт...")
    await ctx.send("Самый точный тест на АйКью: Ваш IQ равен "+str(iq)+". Вы кусок воды")
    await ctx.send("http://pm1.narvii.com/7269/528562cd06efc251bae2a3ad2941f1b81f677e28r1-1080-835v2_uhq.jpg")
@bot.command()
async def playlist(ctx, for_what):
    if for_what == "calm":
        await ctx.send("Расслабляйся! https://www.youtube.com/playlist?list=PLW_omwEM1aieD_VN_aEUucETFBpZsyFoZ")
    elif for_what == 'dance':
        await ctx.send("ТАНЦУЙ ПОД БУЗОВУ! (шутька) https://www.youtube.com/playlist?list=PL9Sagspadk-7CgjnUA5Y08kr-avk0mwqC")
    elif for_what == 'work':
        await ctx.send("Работаешь? Не беда! На плейлист: https://www.youtube.com/playlist?list=PLiZj-Ik9MmM1tG3_oAGuhSCqKLtLviLaI")
    elif for_what == 'gaming':
        await ctx.send("Геймер? Лови музон! Погнали на зону B! https://www.youtube.com/playlist?list=PLR7JWZAjVdyt484P_iMNVfjWuKceX5BFp")
    elif for_what == "chilledcow":
        await ctx.send("А ты шаришь! https://www.youtube.com/watch?v=5qap5aO4i9A")
@bot.command()
async def ideas(ctx):
    id_n = random.randint(0, 40)
    if id_n == 26:
        await ctx.send("Если вам нужен клей-карандаш, то капните клей на карандаш.")
    elif id_n == 1:
        await ctx.send("Если на вас напал медведь, то включите К-РОР, он от вас убежит.")
    elif id_n == 2:
        await ctx.send("Если у вас язва, то съешьте острый доширак.")
    elif id_n == 3:
        await ctx.send("Если вы порезались, нанесите свежий чеснок на рану.")
    elif id_n == 4:
        await ctx.send("Если вам надоело подтирать жопу деньгами, то сожгите свой НоВыЙ МеРиН.")
    elif id_n == 5:
        await ctx.send("Если к вам в школу врываются террористы, то скажите им, что без сменки нельзя.")
    elif id_n == 6:
        await ctx.send("Если вы не любите курицу - идите в KFC.")
    elif id_n == 7:
        await ctx.send("Если вы хотите, что бы ваша посылка быстро доехала, отправьте ее через 'Почту России'.")
    elif id_n == 8:
        await ctx.send("Если вы любите обниматься - идите в UFC.")
    elif id_n == 9:
        await ctx.send("Если вы не хотите что бы кисломолочные продукты испортились - вытащите их из холодильника.")
    elif id_n == 10:
        await ctx.send("Если вы не оплатили кредит и к вам стучится коллектор - откройте ему.")
    elif id_n == 11:
        await ctx.send("Если вы боитесь пауков и таковой завелся в вашем доме - сожгите его. И паука, и дом.")
    elif id_n == 12:
        await ctx.send("Если у вас закончилась туалетная бумага - используйте осенние листья.")
    elif id_n == 13:
        await ctx.send("Если вы хотите завести девушку - вставьте в нее ключи.")
    elif id_n == 14:
        await ctx.send("Если вы Артем - говорите, что вы есть Слава.")
    elif id_n == 15:
        await ctx.send("Очень умный идея - купить белые кроссы, когда ты живешь в России.")
    elif id_n == 16:
        await ctx.send("Если вам надоело общение - ударьте собеседника об стол пару-тройку раз.")
    elif id_n == 17:
        await ctx.send("Если вы чего то не понимаете, 'иди поспи, приляг и поспи'.")
    elif id_n == 18:
        await ctx.send("Если вы боитесь крови - станьте хирургом.")
    elif id_n == 19:
        await ctx.send("Если вы карлик - станьте баскетболистом.")
    elif id_n == 20:
        await ctx.send("Если вы немой - станьте телеведущим.")
    elif id_n == 21:
        await ctx.send("Если на заборе знак 'Осторожно! Злая собака' - обязательно перелезьте и погладьте ее.")
    elif id_n == 22:
        await ctx.send("Если у вас аллергия на шерсть - заведите кошку.")
    elif id_n == 23:
        await ctx.send("Если у вас прокисло молоко - добавьте его в кофе.")
    elif id_n == 24:
        await ctx.send("Если вы ударились о тумбочку, то ударьте тумбочку о себя (будет больно. тумбочке :]).")
    elif id_n == 25:
        await ctx.send("Если вы уронили кошелек с деньгами - не поднимйате его.")
    elif id_n == 27:
        await ctx.send("Закинь огромную петарду в унитаз.")
    elif id_n == 28:
        await ctx.send("Побрызгать спреем против запутанных волос на запутавшиеся наушники.")
    elif id_n == 29:
        await ctx.send("Быть модным, современным, соответствовать всем трендам.")
    elif id_n == 30:
        await ctx.send("Вместо сигнализации, повесьте дома попкорн. При пожаре он начнет лопаться, и скажет шо начался пожар.")
    elif id_n == 31:
        await ctx.send("Чтобы весы показали ваш настоящий вес и вы не расстроилиcь, станьте на пару весов. Пара весов покажет вес точнее.")
    elif id_n == 32:
        await ctx.send("Если ваш друг дальтоник - попросите его подать вам карандаш красного цвета.")
    elif id_n == 33:
        await ctx.send("Если вы хотите побриться налысо - идите в барбер-шоп.")
    elif id_n == 34:
        await ctx.send("У вас глубокая рана? Полейте ее лимонным соком.")
    elif id_n == 35:
        await ctx.send("Если у вас нет денег - продайте свои органы.")
    elif id_n == 36:
        await ctx.send("Если вы увидели шершня-убийцу - поймайте его.")
    elif id_n == 37:
        await ctx.send("Если вы хотите кого-то спасти - выстрелите в него из дробовика SPAS-12.")
    elif id_n == 38:
        await ctx.send("Если вам лень подыматься на лифте? Подымитесь по лестнице.")
    elif id_n == 39:
        await ctx.send("Если у вас разрядился ноут - выкиньте его.")
    elif id_n == 40:
        await ctx.send("Очень умный идея - делать ставки на спорт.")

@bot.command()
async def motivate(ctx):
    dems = [
        "ДА ЧО У ТЕБЯ ПОЛУЧИТСЯ, ЛОШОК!",
        "JUST! POSHEL NAFIG LOH!",
        "Get rekt lol. Ты даже инглишь не знаешь, ахахах.",
        "просто. лошок. И этот лошок - ты!))",
        "ДЭБИИИИЛ! 5 косарей на халяву не забрал!",
        "ТЫ ВАЩЕ КТО ТАКОЙ! ЛОХ МЕЛКИЙ!!!",
        "единственное сообщение которое смотивирует такого лоха как ты, это... его нет))))"
    ]
    variki = random.choices(dems, k=1)

    await ctx.send(variki)

@bot.command()
async def admin(ctx):
    await ctx.send("Вы стали админом (неть)")
@bot.command()
async def v(ctx):
    await ctx.send("***ТЕКУЩАЯ ВЕРСИЯ БОТА: beta 1.1***")

@bot.command()
async def magicball(ctx, question):
    await ctx.send()


bot.run(settings['token'])
