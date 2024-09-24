import os
import requests
import discord
import json
import random

from replit import db
import praw
from keep_alive import keep_alive

client = discord.Client()
sad_words = [
    'sad', 'hopeless', 'depressed', 'depression', 'unhappy', 'angry',
    'depressing'
]
retard_words = [
    'retard', 'sussy', 'retarded', 'retardation', 'society', 'samaj'
]
retard_spams = [
    'https://tenor.com/view/haha-gif-21635374',
    'https://cdn.discordapp.com/attachments/753629588365508618/854012211369738250/video0-1.mp4',
    ' \U0001F921',
    'https://cdn.discordapp.com/attachments/753629588365508618/854180637309534208/dank_bombay-15062021-0001.mp4',
    'https://tenor.com/view/npc-brainlet-gif-21897776',
    'https://tenor.com/view/dream-twerk-dream-smp-dream-team-dream-dream-minecraft-gif-20922736'
]

mute = ['?mute']
warining = ['?warn', 'warning']
Ban = ['?ban']
goodmorning = ['Good Morning', 'good morning', 'Good morning', 'gm', 'GM']
gm = [
    'https://cdn.discordapp.com/attachments/826140331158405183/853117211715436584/470_Ckish35y_6LRv.mp4',
    'https://cdn.discordapp.com/attachments/854870235207303218/874934830222147605/image0-184.jpg',
    'https://tenor.com/view/kanye-kanye-west-gamer-good-morning-good-morning-kanye-gif-16812565',
    'https://media.discordapp.net/attachments/830549560026988565/853476280087609384/b4eedb2ca2c88e25f68fe94b36f9efea.jpg?width=555&height=663',
    ' https://tenor.com/view/coffee-good-morning-smile-gif-13335988',
    'https://media.discordapp.net/attachments/803286365168730184/853852489832464384/image0-10.png',
    'https://cdn.discordapp.com/attachments/712722781988716567/854535092974387200/1623659367938.mp4'
]
goodnight = ['Good Night', 'good night', 'Good night']
SSR = ['ssr', 'SSR', 'Sushant Singh Rajput', 'sushant', 'Sushant']
slap = [
    'https://media.discordapp.net/attachments/714493202282971186/853054095770255370/taapri.gif',
    'https://tenor.com/view/slap-slapping-head-whack-gif-12667518',
    'https://tenor.com/view/robin-batman-slap-gif-10742154',
    'https://tenor.com/view/boy-punish-mad-pissed-off-slap-gif-14667643',
    'https://tenor.com/view/mm-emu-emu-anime-slap-strong-gif-7958720',
    'https://tenor.com/view/slap-gif-21553215',
    'https://tenor.com/view/no-angry-anime-slap-gif-7355956',
    'https://tenor.com/view/girl-slap-anime-mad-student-gif-17423278',
    'https://tenor.com/view/anime-slap-slap-in-the-face-smash-gif-17314633',
    'https://tenor.com/view/anime-slap-gif-7602649'
]
spank = [
    'https://tenor.com/view/spank-tomandjerry-gif-5196956',
    'https://tenor.com/view/hot-spank-butt-slap-butt-butt-grab-gif-12569697',
    'https://tenor.com/view/spank-bad-girl-lucy-deci-gif-4517367',
    'https://tenor.com/view/bad-beat-spank-punishment-gif-13569259',
    'https://tenor.com/view/bad-spank-cry-anime-gif-15905904',
    'https://tenor.com/view/anime-school-girl-smack-spanking-spank-gif-19349444',
    'https://tenor.com/view/spank-slap-butt-anime-gif-17784858',
    'https://tenor.com/view/anime-school-girl-spanking-spank-smack-gif-16313338',
    'https://tenor.com/view/free-iwatobi-swim-club-anime-swimming-spank-gif-3404502',
    'https://tenor.com/view/anime-school-girl-spanking-naughty-spank-gif-16224449',
    'https://tenor.com/view/spank-spank-prank-spanking-gif-17982331'
]
punch = [
    'https://tenor.com/view/anime-smash-lesbian-punch-wall-gif-4790446',
    'https://tenor.com/view/tgggg-anime-punch-gif-13142581',
    'https://tenor.com/view/anime-punch-mad-angry-gif-15580060',
    'https://tenor.com/view/pepe-smash-pepe-the-frog-punch-fight-gif-16459972',
    'https://tenor.com/view/punch-one-man-gif-14279695',
    'https://tenor.com/view/punch-in-the-face-surprise-girl-fight-gif-14906799',
    'https://tenor.com/view/7days-the-movie-punch-punch-in-the-face-movies-mew-gif-12061774',
    'https://tenor.com/view/onepunchman-saitama-anime-pokerface-gif-4604175',
    'https://tenor.com/view/stop-hibari-kun-anime-punch-gif-21782629',
    'https://tenor.com/view/anime-punch-anime-touma-accelerator-acertain-scientific-railgun-gif-20976942',
    'https://tenor.com/view/discord-anime-punch-sad-gif-19594595'
]
emoji = [
    '\U0001F600', '\U0001F601', '\U0001F602', '\U0001F603', '\U0001F604',
    '\U0001F605', '\U0001F606', '\U0001F607', '\U0001F608', '\U0001F623',
    '\U0001F469', '\U0001F971'
]

reddit = praw.Reddit(client_id=#redit client id,
                     client_secret=#redit client secret,
                     user_name=#redit user name,
                     password=#redit account password,
                     user_agent='prawproject',
                     check_for_async=False)

starter_encouragements = [
    'Cheer Up! Retard lol.', 'Get a life mate.', 'Hang in there.',
    'You are a great person! but throw those retarded thoughts.',
    'Give it a try.', 'What are you waiting for?', 'What do you have to lose?',
    'Stay strong.', 'Come on! You can do it!.', 'It’s totally up to you..',
    'Follow your dreams.', 'The sky is the limit.', 'Don’t give up.'
]

if "responding" not in db.keys():
    db['responding'] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db['encouragements'] = encouragements
    else:
        db['encouragements'] = [encouraging_message]


def delete_encouragement(index):
    encouragements = db['encouragements']
    if len(encouragements) > index:
        del encouragements[index]
    db['encouragements'] = encouragements


def meme():
    sub = [
        'Samaj', 'okbuddyretard', '2meirl42meirl4meirl', 'Animememes', 'ape',
        'blackhumor', 'EdgyMemestwo', 'okbhaibudbak', 'Offensivejokes',
        'PoliticalCompassMemes', 'atheistmemes', 'Dank', 'PCMIndia',
        'okaybuddyretard', '2Asia4u', 'comedyheaven', 'ComedyNecrophilia',
        'shitposting', 'whenthe', 'librandu'
    ]
    choose = random.choice(sub)
    subreddit = reddit.subreddit(choose)
    all_subs = []
    hot = subreddit.hot(limit=30)
    for submission in hot:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    embed = em
    return embed


def waifu():
    sub = [
        'waifuswithguns', 'cosplaygirls', 'animegifs', 'formalwaifus', 'Waifu'
    ]
    choose = random.choice(sub)
    subreddit = reddit.subreddit(choose)
    all_subs = []
    hot = subreddit.hot(limit=30)
    for submission in hot:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    embed = em
    return embed


def local():
    sub = ['IndianGoneWild', 'IndianBabes', 'desi', 'DesiBoners', 'DesiTeen']
    choose = random.choice(sub)
    subreddit = reddit.subreddit(choose)
    all_subs = []
    hot = subreddit.hot(limit=10)
    for submission in hot:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    embed = em
    return embed


def nsfw():
    sub = [
        'NSFWverifiedamateurs', 'HENTAI_GIF', 'thighdeology', 'thighhighs',
        'Lustdesii'
    ]
    choose = random.choice(sub)
    subreddit = reddit.subreddit(choose)
    all_subs = []
    hot = subreddit.hot(limit=30)
    for submission in hot:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    embed = em
    return embed


@client.event
async def on_ready():
    print('We have logged in as{0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.playing, name='with ur mom $help'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #for reddit memes
    if message.content.startswith('$meme'):
        memes = meme()
        await message.channel.send(embed=memes)

    if message.content.startswith('$waifu'):
        waifus = waifu()
        await message.channel.send(embed=waifus)
    if message.content.startswith('$nsfw'):
        nsfws = nsfw()
        await message.channel.send(embed=nsfws)
    if message.content.startswith('$local'):
        locals = local()
        await message.channel.send(embed=locals)
    #when $hello
    if message.content.startswith('$hello'):
        await message.channel.send(
            'Hello! how are you looks like u got no one to talk to sed ' +
            '\U0001F614')
    #for $sed
    if message.content.startswith('$sed'):
        quote = get_quote()
        await message.channel.send(quote + ' \U0001F618')

    if message.content.startswith('$redditpost'):
        sub = message.content.split('$redditpost ', 1)[1]
        if sub[0:2] == 'r/':
            await message.channel.send(
                'No need to enter r/. Please try again!!')
        else:
            choose = sub
            subreddit = reddit.subreddit(choose)
            all_subs = []
            hot = subreddit.hot(limit=30)
            for submission in hot:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)

            name = random_sub.title
            url = random_sub.url
            em = discord.Embed(title=name)
            em.set_image(url=url)
            embed = em
            await message.channel.send(embed=embed)

    if message.content.startswith('$slap'):
        SlAp = message.content.split('$slap ', 1)[1]
        await message.channel.send(
            f'{random.choice(slap)} {SlAp} you got slapped')
    if message.content.startswith('$spank'):
        SpAnK = message.content.split('$spank ', 1)[1]
        await message.channel.send(
            f'{random.choice(spank)} {SpAnK} you got spanked')
    if message.content.startswith('$punch'):
        pUnCh = message.content.split('$punch ', 1)[1]
        await message.channel.send(
            f'{random.choice(punch)} {pUnCh} you got punched')
    if message.content.startswith("$doge"):
        await message.channel.send(
            'https://cdn.discordapp.com/emojis/667431058576506892.png?v=1')

    #for $help

    if message.content.startswith('$help') or message.content.startswith(
            '$commands'):
        await message.channel.send(
            'Bot commands: '
            '\n'
            '$hello' + ' - to talk to me.'
            '\n'
            '$sed' + ' -get motivational quotes to get your ass running. '
            '\n'
            '$new' + ' -to add some good words for the bot to spam.'
            '\n'
            '$responding true' + ' - to turn on bot spams.'
            '\n'
            '$responding false' + ' - to turn off bot spams.'
            '\n'
            #$del + index number to delete any good words
            '$list' + ' - to see the words added.'
            '\n'
            '$punch' + '- to puch someone.'
            '\n'
            '$slap' + '- to slap someone.'
            '\n'
            '$meme' +
            '- get based meme that <@!270904126974590976> doesnt gives.'
            '\n'
            '$waifu' + ' - get some hot ass waifus.'
            '\n'
            '$redditpost (*enter correct subreddit name*)' +
            ' - to get trending post from the subreddit.'
            '\n'
            '$nsfw' + ' - nsfw content.'
            '\n'
            '$local' + ' - for indian local.'
            '\n'
            'For any bot related help DM  ' + '<@!514650429167239178>')
    #to turn on or off bot spams
    if db['responding']:

        options = starter_encouragements
        if "encouragements" in db.keys():
            options += db['encouragements']

        #SPAMS
        if any(word in message.content for word in retard_words):
            await message.channel.send(random.choice(retard_spams))

        if any(word in message.content for word in SSR):
            await message.channel.send(
                'https://media.discordapp.net/attachments/714493202282971186/852852648444821504/dumpy852852579918413854.gif'
            )

        if any(word in message.content for word in goodmorning):
            await message.channel.send(f'{random.choice(gm)}')

        if any(word in message.content for word in goodnight):
            await message.channel.send(
                'https://tenor.com/view/animu-anime-good-night-gif-14037284')

        if any(word in message.content for word in warining):
            await message.channel.send(
                'https://tenor.com/view/funne-warn-discord-tenor-meme-gif-21067897'
            )

        if any(word in message.content for word in mute):
            await message.channel.send(
                'https://tenor.com/view/mute-cat-hiding-kin-planet-gif-22304862'
            )

        if any(word in message.content for word in Ban):
            await message.channel.send(
                'https://tenor.com/view/ban-button-keyboard-press-the-ban-button-gif-16387934'
            )

        if any(word.lower() in message.content for word in sad_words):
            await message.channel.send(
                random.choice(options) + random.choice(emoji))
    #to add new good message
    if message.content.startswith('$new'):
        encouraging_message = message.content.split('$new ', 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send('Your words has been added. Thanks you!!!.')

    if message.content.startswith('$del'):
        encouragements = []
        if 'encouragements' in db.keys():
            index = int(message.content.split('$del', 1)[1])
            delete_encouragement(index)
            encouragements = db['encouragements']
        await message.channel.send(encouragements)
    if message.content.startswith('$list'):
        encouragements = []
        if 'encouragements' in db.keys():
            encouragements = db['encouragements']

        await message.channel.send(encouragements)

    if message.content.startswith("$responding"):
        value = message.content.split('$responding ', 1)[1]

        if value.lower() == 'true':
            db['responding'] = True
            await message.channel.send("Responding to messages is on.")

        else:
            db['responding'] = False
            await message.channel.send("Responding to messages is off.")


keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)