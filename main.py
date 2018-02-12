import discord
from discord import Webhook, AsyncWebhookAdapter
import random
import KEYS
import sqlite3
import aiohttp
import time
import asyncio

conn = sqlite3.connect("daten.db")
cur = conn.cursor()

global version
version = "2.0 ALPHA"
DEINE_USER_ID = "HIER DEINE USER ID"

global gamestatus
# gamestatus = "!help @Logit | TheBotDev"
gamestatus = "!help - V 2.0 ALPHA"



class MyClient(discord.Client):
    async def on_ready(self):
        game = discord.Game(name=gamestatus)
        await client.change_presence(status=discord.Status.online, game=game)
        global clientname
        clientname = "test-bot"
        cur.execute("CREATE TABLE IF NOT EXISTS server_settings (gid INTEGER, prefix TEXT)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS premium_user (username TEXT, userid INTEGER, key INTEGER, server INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS premium (servername TEXT, serverid INTEGER, key INTEGER, status TEXT)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS server_logs(gid INTEGER, a1 INTEGER, a2 INTEGER, a3 INTEGER, a4 INTEGER, a5 INTEGER, a6 INTEGER, a7 INTEGER, a8 INTEGER, a9 INTEGER, a10 INTEGER, a11 INTEGER, a12 INTEGER, a13 INTEGER, a14 INTEGER, a15 INTEGER, a16 INTEGER, a17 INTEGER, a18 INTEGER, a19 INTEGER, a31 INTEGER, a32 INTEGER, a33 INTEGER, a34 INTEGER, activated TEXT, channelid INTEGER, owner INTEGER)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS server_game_settings (activated INTEGER, channel INTEGER, guildid INTEGER)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS server_game_accounts (userid INTEGER, money INTEGER, banned INTEGER, serverid INTEGER)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS support (channel INTEGER, messageUser TEXT, message TEXT, server INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS webhook (server INTEGER, url TEXT)")

        print("Login succesfully!\n")
        print("""================\n""")
	#Emojis für die Setup's der Game's (wenn du auch diese Emojis haben möchtest schreibe mir und ich mache das dann für dich)
        emojilist = client.get_guild(394139572260438020)
        emojilist2 = client.get_guild(398121407847989248)
        admin_name = client.get_user(DEINE_USER_ID)
        counter = 0
        counter2 = 0
        for emojis in emojilist2.emojis:
            if counter2 == 0:
                global moneyicon
                moneyicon = client.get_emoji(emojis.id)
            if counter2 == 1:
                global n1
                n1 = client.get_emoji(emojis.id)
            elif counter2 == 2:
                global n2
                n2 = client.get_emoji(emojis.id)
            elif counter2 == 3:
                global n3
                n3 = client.get_emoji(emojis.id)
            elif counter2 == 4:
                global n4
                n4 = client.get_emoji(emojis.id)
            elif counter2 == 5:
                global n5
                n5 = client.get_emoji(emojis.id)
            elif counter2 == 6:
                global premium
                premium = client.get_emoji(emojis.id)
            elif counter2 == 7:
                global horse
                horse = client.get_emoji(emojis.id)
            counter2 = counter2 + 1
        for emoji in emojilist.emojis:
            if counter == 0:
                global z10
                z10 = client.get_emoji(emoji.id)
            elif counter == 1:
                global z11
                z11 = client.get_emoji(emoji.id)
            elif counter == 2:
                global z12
                z12 = client.get_emoji(emoji.id)
            elif counter == 3:
                global z13
                z13 = client.get_emoji(emoji.id)
            elif counter == 4:
                global z14
                z14 = client.get_emoji(emoji.id)
            elif counter == 5:
                global z15
                z15 = client.get_emoji(emoji.id)
            elif counter == 6:
                global z16
                z16 = client.get_emoji(emoji.id)
            elif counter == 7:
                global z17
                z17 = client.get_emoji(emoji.id)
            elif counter == 8:
                global z18
                z18 = client.get_emoji(emoji.id)
            elif counter == 9:
                global z19
                z19 = client.get_emoji(emoji.id)
            elif counter == 10:
                global z1
                z1 = client.get_emoji(emoji.id)
            elif counter == 11:
                global z2
                z2 = client.get_emoji(emoji.id)
            elif counter == 12:
                global z3
                z3 = client.get_emoji(emoji.id)
            elif counter == 13:
                global z4
                z4 = client.get_emoji(emoji.id)
            elif counter == 14:
                global z5
                z5 = client.get_emoji(emoji.id)
            elif counter == 15:
                global z6
                z6 = client.get_emoji(emoji.id)
            elif counter == 16:
                global z7
                z7 = client.get_emoji(emoji.id)
            elif counter == 17:
                global z8
                z8 = client.get_emoji(emoji.id)
            elif counter == 18:
                global z9
                z9 = client.get_emoji(emoji.id)
            elif counter == 19:
                global hype
                hype = client.get_emoji(emoji.id)
            elif counter == 20:
                global off
                off = client.get_emoji
            elif counter == 21:
                global on
                on = client.get_emoji

            elif counter == 22:
                global z210
                z210 = client.get_emoji
            elif counter == 23:
                global z215
                z215 = client.get_emoji
            elif counter == 24:
                global z20
                z20 = client.get_emoji
            elif counter == 25:
                global z25
                z25 = client.get_emoji
            elif counter == 26:
                global z30
                z30 = client.get_emoji
            elif counter == 27:
                global z50
                z50 = client.get_emoji

            counter = counter + 1

    async def on_message(self, message):
        guild = message.guild.id
        cur.execute("SELECT prefix FROM server_settings WHERE gid=?", (guild,))
        global prefix
        prefix = cur.fetchone()[0]
        inleng = len(prefix)
        cur.execute("SELECT status FROM premium WHERE serverid=?", (message.guild.id,))
        global statuspremium
        statuspremium = cur.fetchall()
        if message.content.startswith(prefix):
            invoke = message.content[inleng:].split(" ")[0]
            if invoke == "ping":
                await message.channel.send(content="Pong!")
            if invoke == "update":
                cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (message.guild.id,))
                loexi = cur.fetchall()
                print(loexi)
                if str(loexi) != "[(None,)]":
                    cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (message.guild.id,))
                    log = cur.fetchone()[0]
                    print(log)
                    cur.execute("SELECT server FROM webhook WHERE server=?", (message.guild.id,))
                    webhshex = cur.fetchall()
                    if str(webhshex) == "[]":
                        try:
                            webh = await log.create_webhook(name="Logit")
                            cur.execute("INSERT INTO webhook (server, url) VALUES (?,?)", (message.guild.id, webh.url))
                            conn.commit()
                            async with aiohttp.ClientSession() as session:
                                webhook = Webhook.from_url(webh.url, adapter=AsyncWebhookAdapter(session))
                                await webhook.send(username='Logit',
                                                   avatar_url="https://cdn.discordapp.com/app-icons/398933329862328330/e33eff5bb64f94c2d013bc9e6de01393.png",
                                                   embed=discord.Embed(color=discord.Color.green(),
                                                                       description="Es funktioniert"))

                        except discord.errors.Forbidden:
                            await message.channel.send(
                                content="Das Setup wurde abgebrochen! Leider habe ich nicht die Permission um einen WebHook zu erstellen (WebHooks verwalten), aber das ist sehr wichtig für diese Funktion!")

            if invoke == "replace":
                def c(m):
                    if m.author.id == message.author.id and m.channel.id == message.channel.id:
                        return m

                await message.channel.send(content="Sende mir den Text")
                temp = await client.wait_for("message", check=c, timeout=None)
                message1 = (temp.content).replace("n11", str(z11))
                message2 = (message1).replace("n12", str(z12))
                message3 = (message2).replace("n13", str(z13))
                message4 = (message3).replace("n14", str(z14))
                message5 = (message4).replace("n15", str(z15))
                message6 = (message5).replace("n16", str(z16))
                message7 = (message6).replace("n17", str(z17))
                message8 = (message7).replace("n18", str(z18))
                message9 = (message8).replace("n19", str(z19))
                message10 = message9
                await message.channel.send(content=message10)



            if invoke == "activate" or invoke == "premiumactivate" or invoke == "activatepremium" or invoke == "activatePremium" or invoke == "pa" or invoke == "ap":
                if message.author.guild_permissions.administrator == True or message.author.id == DEINE_USER_ID:
                    def c(m):
                        if m.author.id == message.author.id and m.channel.id == message.channel.id:
                            return m

                    await message.channel.send(
                        content="Oh cool du möchtest Premium aktivieren? Bitte sei dir sicher das nur du und ich diesen Channel sehen können. Nun sende bitte deinen 'Key' direckt unter dieser Nachricht. Dein 'Key' sollte folgendermaßen aussehen: `xxxxxxxxxxxxxxxx`")
                    ke = await client.wait_for("message", check=c, timeout=None)
                    key = ke.content
                    try:
                        int(key)
                        if len(key) == 16 or len(key) == 15:
                            cur.execute("SELECT server FROM premium_user WHERE key=?", (int(key),))
                            exists = cur.fetchall()
                            cur.execute("SELECT userid FROM premium_user WHERE key=?", (int(key),))
                            user = cur.fetchone()[0]
                            if user == 0 or user == message.author.id:
                                print(exists)
                                if str(exists) == "[(88,)]":
                                    cur.execute("SELECT status FROM premium WHERE key=? AND serverid=?",
                                                (int(key), message.guild.id))
                                    date = cur.fetchall()
                                    if str(date) == "[]":
                                        cur.execute(
                                            "INSERT INTO premium (key, serverid, servername, status) VALUES(?, ?, ?, ?)",
                                            (int(key), message.guild.id, message.author.guild.name, "activated"))

                                         conn.commit()
                                        await message.channel.send(
                                            content="Sehr Gut Premium wurde erfolgreich für diesen Server aktiviert :tada:, wenn du irgendwelche Vorschläge oder so hast kontaktiere mich bitte. Dann noch viel Spaß mit dem Bot.")
                                    else:
                                        await message.channel.send(
                                            content="Cool dass du an einer Premium Version meines Bot's interressiert bist, und dass du deinen Key gleich 2 mal einlösen willst aber ich denke 1 mal reicht aus^^")
                                elif str(exists) == "[(1,)]":
                                    cur.execute("UPDATE premium_user SET server=0 WHERE key=?", (int(key),))
                                    conn.commit()
                                    cur.execute("SELECT status FROM premium WHERE key=? AND serverid=?",
                                                (int(key), message.guild.id))
                                    date = cur.fetchall()
                                    if str(date) == "[]":
                                        cur.execute(
                                            "INSERT INTO premium (key, serverid, servername, status) VALUES(?, ?, ?, ?)",
                                            (int(key), message.guild.id, message.author.guild.name, "activated"))
                                        conn.commit()
                                        await message.channel.send(
                                            content="Sehr Gut Premium wurde erfolgreich für diesen Server aktiviert :tada:, wenn du irgendwelche Vorschläge oder so hast kontaktiere mich bitte. Dann noch viel Spaß mit dem Bot..")
                                    else:
                                        await message.channel.send(
                                            content="Cool dass du an einer Premium Version meines Bot's interressiert bist, und dass du deinen Key gleich 2 mal einlösen willst aber ich denke 1 mal reicht aus^^")
                                elif str(exists) == "[(0,)]":
                                    await message.channel.send(
                                        content="Es tut mir wirklich leid aber der Key ist berreits auf einem anderen Server aktiviert.")
                            else:
                                await message.channel.send(
                                    content="Das ist nicht dein Key! Bitte kaufe dir deinen eigenen auf [Patrreon](https://patreon.com/TheBotDev)")
                        else:
                            await message.channel.send(content="Die Länge von deinem Key ist falsch!")

                    except:
                        await message.channel.send(content="Kein gültiger Key eingegeben")
                else:
                    sorry = await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Diesen Command können leider nur Administartoren ausführen").set_thumbnail(
                        url="https://thebotdev.de/assets/img/alert.png"))
                    await asyncio.sleep(20)
                    await sorry.delete()
           if invoke == "premium":
                cur.execute("SELECT status FROM premium WHERE serverid=?", (message.guild.id,))
                stat = cur.fetchall()
                status = "error to read database"
                if str(stat) == "[]":
                    status = "Premium is not activated for this server"
                else:
                    status = "Bot is premium here"
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Premium Dashboard")
                embed.add_field(name="status:", value=status, inline=False)
                embed.add_field(name="Info:",
                                value="Du kannst sehen das wenn das Icon: %s vor einer Einstellung ist dass es dann nur Premium Nutzer benutzen können. Um Premium zu kaufen gebe bitte **!buypremium** ein" % (
                                    str(premium)), inline=False)
                embed.add_field(name="Wieso Premium?",
                                value="Ich verkaufe Premium für meine Bots nicht um Geld abzu ziehen sondern weil ich auch Ausgaben für meine Bots habe und ich mit Premium und co. probiere diese Ausgaben wieder zurück zu bekommen indem ich den Premium Rang verkaufe (1 $ für einen Server | 3 $ für unendlich Server)",
                                inline=False)
                embed.add_field(name="Was bekomme ich wenn ich Premium kaufe?",
                                value="Wenn du Premium kaufst dann bekommst du die Premium Rolle auf meinem Server mit der du mehr Channel sehen kannst und exklusiven Zugriff auf Premium Funktionen des Bot's.")
                await message.channel.send(embed=embed)

            if invoke == "buypremium":
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Premium kaufen <3", url="https://patreon.com/TheBotDev")
                embed.add_field(name="Wie kaufe ich Premium?",
                                value="Um den Premium Rang zu bekommen musst du auf dem TheBotDev Server sein dann wirst du eine Private Nachricht meines Bot's erhalten in der dein Key steht. Diesen Key kannst du mit dem Befehl %sactivatePremium auf deinem Server einlösen." % (
                                    prefix))
                embed.add_field(name="Wo könnte ich Premium kaufen?",
                                value="Premium für diesen Bot kaufst du auf [Patreon](https://patreon.com/TheBotDev), aber du musst auf dem [TheBotDev Support Server](https://discord.gg/HD7x2vx) sein.")
                embed.add_field(name="Wie aktiviere ich Premium?",
                                value="Nachdem dir Patreon die Premium Rolle gegeben hat wird dir mein Bot eine Nachricht mit einem 16 stelligen Key senden. Diesen Key lößt du mit dem  %sactivatePremium Command auf deinem Server ein." % (
                                    str(prefix)))
                await message.channel.send(embed=embed)



            # Es tut mir leid das ich leider nicht alle Games veröffentlicht habe weil ich sie auf Patreon anbiete.

            if invoke == "acc":
                ban = "unknown"
                cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                            (message.author.id, message.guild.id))
                existiertacc = cur.fetchall()
                if str(existiertacc) == "[]":
                    cur.execute("INSERT INTO server_game_accounts (userid, money, banned, serverid) VALUES(?,?,?,?)",
                                (message.author.id, 2500, 0, message.guild.id))
                    conn.commit()
                    await message.channel.send(
                        content="Dein Account wurde erfolgreich erstellt! Für weitere Informationen gebe bitte %sacc oder %sgames um eine Liste mit allen Games zu bekommen" % (
                        prefix, prefix))
                else:
                    cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                                (message.author.id, message.guild.id))
                    money = cur.fetchone()[0]
                    cur.execute("SELECT banned FROM server_game_accounts WHERE userid=? AND serverid=?",
                                (message.author.id, message.guild.id))
                    banned = cur.fetchall()
                    if str(banned) != "[]":
                        cur.execute("SELECT banned FROM server_game_accounts WHERE userid=? AND serverid=?",
                                    (message.author.id, message.guild.id))
                        userban = cur.fetchone()[0]
                        if userban == 1:
                            ban = "banned for games by the server admin"
                        elif userban == 0:
                            ban = "Du bist nicht für Games gebannt"
                    else:
                        ban = "Du bist nicht für Games gebannt"
                    embed = discord.Embed(color=0x64efff)
                    embed.set_author(name="Account")
                    embed.add_field(name="money:", value=str(money) + str(moneyicon), inline=True)
                    embed.add_field(name="ban status:", value=ban, inline=True)
                    embed.add_field(name="Games", value=prefix + "games", inline=False)
                    await message.channel.send(embed=embed)

            if invoke == "number":
                cur.execute("SELECT channel FROM server_game_settings WHERE guildid=?", (message.guild.id,))
                channel = cur.fetchone()[0]
                if channel == message.channel.id:
                    abfrage = await message.channel.send(
                        content=":one: 1-10 kosten: 10%s win: 100%s\n:two: 1-20 kosten: 10%s win: 200%s\n:three: 1-30 kosten: 10%s win: 3000%s\n:four: 1-40 kosten: 10%s win: 4000%s\n:five: 1-50 kosten: 10%s win: 5555%s" % (
                        str(moneyicon), str(moneyicon), str(moneyicon), str(moneyicon), str(moneyicon), str(moneyicon),
                        str(moneyicon), str(moneyicon), str(moneyicon), str(moneyicon)))
                    try:
                        await abfrage.add_reaction(n1)
                        await abfrage.add_reaction(n2)
                        await abfrage.add_reaction(n3)
                        await abfrage.add_reaction(n4)
                        await abfrage.add_reaction(n5)
                    except discord.errors.Forbidden:
                        await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                       description="Ich konnte das Game leider nicht starten! Bitte gebe mir die Berrechtigung Reactions hinzu zufügen"))
                else:
                    information = await message.channel.send(
                        content="Dies ist kein Game Channel oder Game's sind auf diesem Server nicht erlaubt, wenn du der Admin bist du es eintichten möchtest mache bitte !setupG")
                    await asyncio.sleep(20)
                    await information.delete()


            # PREFIX
            elif invoke == "PREFIX":
                chapre = prefix + "pchange"
                hel = prefix + "Hilfe"
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Prefix")
                embed.add_field(name="aktueller Prefix:", value=prefix, inline=False)
                embed.add_field(name="ändere Prefix:", value=chapre, inline=False)
                embed.add_field(name="mehr Hilfe:", value=hel, inline=True)
                await message.channel.send(embed=embed)
            elif invoke == "pchange":
                if message.author.guild_permissions.administrator == True or message.author.id == DEINE_USER_ID:
                    gid = message.guild.id
                    await message.channel.send(embed=discord.Embed(color=0x64efff,
                                                                   description="Dein aktueller Prefix ist %s Nun sende mir bitte den neuen Prefix" % prefix))

                    def c(m):
                        if m.author.id == message.author.id and m.channel.id == message.channel.id:
                            return m

                    waitfor = await client.wait_for("message", check=c, timeout=None)
                    newprefix = waitfor.content
                    cur.execute("UPDATE server_settings SET prefix=? WHERE gid=?", (newprefix, gid))
                    conn.commit()
                    await message.channel.send(content="Der neue prefix ist nun " + str(newprefix))
                else:
                    await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                   description="Diese Command ist nur für Administratoren Sorry!").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))
            elif invoke == "changelog":
                await message.channel.send(content=msgChangeLog)
            elif invoke == "info":
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Botinfo",
                                 icon_url="https://thebotdev.de/assets/img/Fragezeichen.png")
                embed.add_field(name="Bot von:", value="BaseChip#2390", inline=False)
                embed.add_field(name="Projekt:", value="TheBotDev", inline=False)
                embed.add_field(name="Lade mich auf deinen Server ein:",
                                value="[invite](https://discordapp.com/oauth2/authorize?client_id=398933329862328330&permissions=1342663878&scope=bot)",
                                inline=False)
                embed.add_field(name="Mein Support Server:", value="https://discord.gg/HD7x2vx", inline=False)
                embed.add_field(name="Bot Liste:", value="[DiscordBots](https://discordbots.org/bot/398933329862328330)", inline=False)
                embed.add_field(name="Version:", value=version, inline=False)
		embed.add_field(name="GitHub", value="[BaseChip](https://github.com/BaseChip)", inline=False)
                embed.add_field(name="Libary", value="discord.py rewrite api", inline=False)
                embed.set_footer(text="Vielen Dank für die Benutzung!")
                await message.channel.send(embed=embed)

            elif invoke == "replaceinfo":
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Replace Info",
                                 icon_url="https://thebotdev.de/assets/img/Fragezeichen.png")
                embed.add_field(name="Ferfügbare Emojis",
                                value=" n11 -> %s\nn12 -> %s\nn13 -> %s\nn14 -> %s\nn15 -> %s\nn16 -> %s\nn17 -> %s\nn18 -> %s\nn19 -> %s" % (
                                str(z11), str(z12), str(z13), str(z14), str(z15), str(z16), str(z17), str(z18),
                                str(z19)))
                await message.channel.send(embed=embed)

            elif invoke == "rules" and message.channel.id != 404911854112997377:
                embed = discord.Embed(title="Regeln ",
                                      description="Eine Funktion um Regeln zu aktzeptieren ist der Rules Bot und dann gibt es da auch noch so nen komisch Blitz Bot",
                                      color=0x00ff00)
                embed.add_field(name="Rules Bot (von mir)", value="https://discord.gg/HD7x2vx", inline=False)
                embed.add_field(name="Flash aka. Blitz", value="https://flashbot.de", inline=True)
                await message.channel.send(embed=embed)

            elif invoke == "help" or invoke == "Help" or invoke == "Support" or invoke == "Hilfe":
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Hilfe", icon_url="https://thebotdev.de/assets/img/Fragezeichen.png")
                embed.add_field(name="Prefix",
                                value="➥" + prefix + "**PREFIX** -> zeigt Informationen über diesen Command\n➥" + prefix + "**pchange** -> ändert den Prefix (serverweit)",
                                inline=False)
                embed.add_field(name="Logs",
                                value="➥" + prefix + "**log** -> zeigt Informationen übern den Log auf deinem Server\n➥" + prefix + "**setupL** -> Ist das Setup für den Server Log",
                                inline=False)
                embed.add_field(name="Admin Commands",
                                value="➥" + prefix + "**ban** -> Bannt einen User\n➥" + prefix + "**kick** -> Kickt einen User\n➥" + prefix + "**ping** -> Zeigt ob der Bot online ist.",
                                inline=False)
                embed.add_field(name="Messages",
                                value="➥" + prefix + "**send** [Die Nachricht] -> sendet eine Nacheicht\n" + "➥" + prefix + "**message** -> Generiert eine Nachricht mit einem bunten Rand\n➥" + prefix + "**replaceinfo** -> Infos für den 'replace' Command\n➥" + prefix + "**replace** -> Ersetzt nutzvolle Emojis.")
                embed.add_field(name="Games",
                                value="➥%ssetupG\n➥%sgames\n➥%snumber\n➥%s%sdon\n➥%s%srace\n➥%s%saddmoney\n➥%s%sremovemoney" % (
                                prefix, prefix, prefix, str(premium), prefix, str(premium), prefix, str(premium),
                                prefix, str(premium), prefix), inline=False)
                embed.add_field(name="Normale Sachen",
                                value="➥%s**info**\n➥%s**send** [Die nacheicht]\n➥%s**rules**" % (prefix, prefix, prefix),
                                inline=False)
                embed.add_field(name="Premium",
                                value="➥%s**ap**\n➥%s**premium**\n➥%s**buypremium**" % (prefix, prefix, prefix))
                await message.channel.send(embed=embed)
		
            # Admin stuff
            elif invoke == "leave":
                if message.author.id == DEINE_USER_ID:
                    await message.guild.leave()

                else:
                    await message.channel.send(
                        content="WOW eine geheime Funktion aber es tut mir Leid diese Funktion ist nur für BaseChip :shrug:")
            elif invoke == "ban":
                if message.author.guild_permissions.administrator == True or message.author.id == DEINE_USER_ID:
                    await message.channel.send(content="Bitte mentione den User den ich bannen soll")

                    def c(m):
                        if m.author.id == message.author.id and m.channel.id == message.channel.id:
                            return m

                    usr = await client.wait_for("message", check=c, timeout=None)
                    usertoban = usr.mentions[0]
                    await message.channel.send(content="Ich werde den User " + str(
                        usertoban.mention) + "bannen. Bitte sende mir nun den ban Grund oder wenn du keinen grund angeben möchtest antworte mit `n`")
                    reas = await client.wait_for("message", check=c, timeout=None)
                    if reas.content != "n":
                        try:
                            await message.author.guild.ban(usertoban,
                                                           reason=reas.content + "  | Wurde gebannt von: " + reas.author.name,
                                                           delete_message_days=7)
                        except discord.errors.Forbidden:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Error ich habe keine Rechte zum bannen!"))
                else:
                    sorry = await message.channel.send(content="Sorry diesen Command können nur Admins benutzen")
                    await asyncio.sleep(20)
                    await sorry.delete()

            elif invoke == "kick":
                if message.author.guild_permissions.administrator == True or message.author.id == DEINE_USER_ID:
                    await message.channel.send(content="Bitte mentione den User den ich kicken soll")

                    def c(m):
                        if m.author.id == message.author.id and m.channel.id == message.channel.id:
                            return m

                    usr = await client.wait_for("message", check=c, timeout=None)
                    usertoban = usr.mentions[0]
                    await message.channel.send(content="Ich werde den User " + str(
                        usertoban.mention) + "kicken. Bitte sende mir nun den ban Grund oder wenn du keinen grund angeben möchtest antworte mit `n`")
                    reas = await client.wait_for("message", check=c, timeout=None)
                    if reas.content != "n":
                        try:
                            await message.author.guild.kick(usertoban,
                                                            reason=reas.content + "  | Wurde gekickt von: " + reas.author.name)
                        except discord.errors.Forbidden:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Error ich habe keine Rechte zum kicken!"))
                else:
                    sorry = await message.channel.send(content="Sorry diesen Command können nur Admins benutzen")
                    await asyncio.sleep(20)
                    await sorry.delete()

            # logs
            elif invoke == "log":
                gid = message.guild.id
                cur.execute("SELECT activated FROM server_logs WHERE gid=?", (gid,))
                status = cur.fetchone()[0]
                if status == "yes":
                    act = "Logs sind aktiviert auf diesem Server"
                else:
                    act = "Logs sind nicht aktiviert hier "
                hel = prefix + "help"
                change = prefix + "setupL"
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Logs")
                embed.add_field(name="Status:", value=act, inline=False)
                embed.add_field(name="Set up logs:", value=change, inline=False)
                embed.add_field(name="more help:", value=hel, inline=True)
                await message.channel.send(embed=embed)
            elif invoke == "setupL":
                if message.author.guild_permissions.administrator == True or message.author.id == DEINE_USER_ID:
                    def c(m):
                        if m.author.id == message.author.id and m.channel.id == message.channel.id:
                            return m

                    await message.channel.send(embed=discord.Embed(color=0x64efff,
                                                                   description="Okay also als erstes sende mit bitte den Channel in dem der Log geschickt werden soll also zum Beispiel #LogChannel"))
                    waitforchannel = await client.wait_for("message", check=c, timeout=None)
                    log = waitforchannel.channel_mentions[0]
                    logchannel = log.id
                    cur.execute("SELECT server FROM webhook WHERE server=?", (message.guild.id,))
                    webhshex = cur.fetchall()
                    if str(webhshex) == "[]":
                        print(webhshex)
                        try:
                            webh = await log.create_webhook(name="Logit")
                            cur.execute("INSERT INTO webhook (server, url) VALUES (?,?)", (message.guild.id, webh.url))
                            conn.commit()
                            async with aiohttp.ClientSession() as session:
                                webhook = Webhook.from_url(webh.url, adapter=AsyncWebhookAdapter(session))
                                await webhook.send(username='Logit',
                                                   avatar_url="https://cdn.discordapp.com/app-icons/398933329862328330/e33eff5bb64f94c2d013bc9e6de01393.png",
                                                   embed=discord.Embed(color=discord.Color.green(),
                                                                       description="Es funktioniert"))

                        except discord.errors.Forbidden:
                            await message.channel.send(
                                content="Setup wurde abgebrochen! Möglicher Weise habe ich nicht alle berechtigungen dafür (WebHooks verwalten)")
                    else:
                        cur.execute("SELECT url FROM webhook WHERE server=?", (message.guild.id,))
                        url = cur.fetchone()[0]
                        try:
                            async with aiohttp.ClientSession() as session:
                                webhook = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
                                await webhook.send(username='Logit',
                                                   avatar_url="https://cdn.discordapp.com/app-icons/398933329862328330/e33eff5bb64f94c2d013bc9e6de01393.png",
                                                   embed=discord.Embed(color=discord.Color.green(),
                                                                       description="Webhook existiert bereits"))
                        except discord.errors.NotFound:
                            await message.channel.send("Bitte kicke den bot und invite ihn erneut - DANKE")
                    print(logchannel)
                    if logchannel != None:
                        gid = message.guild.id
                        auth = message.author.id
                        embed = discord.Embed(
                            description="Um die Funktion zu aktivieren reagiere bitte mit der passenden Nummer",
                            color=0x64efff)
                        embed.set_author(name="Setup | Logs")
                        embed.add_field(name="member join", value="1", inline=False)
                        embed.add_field(name="member leave", value="2", inline=False)
                        embed.add_field(name="member update (e.g Nickname Änderung...)", value="3", inline=False)
                        embed.add_field(name="member ban", value="4", inline=False)
                        embed.add_field(name="member unban", value="5", inline=False)
                        embed.add_field(name="message delete", value="6", inline=False)
                        embed.add_field(name="bulk message delete", value="7", inline=False)
                        embed.add_field(name="message edit", value="8", inline=False)
                        embed.add_field(name="channel create", value="9", inline=False)
                        embed.add_field(name="channel update", value="10", inline=False)
                        embed.add_field(name="channel delete", value="11", inline=False)
                        embed.add_field(name="member joins a voice channel", value="12", inline=False)
                        embed.add_field(name="emoji add/update/remove to the server", value="13", inline=False)
                        embed.add_field(name="reaction add", value="14", inline=False)
                        embed.add_field(name="reaction remove", value="15", inline=False)
                        embed.add_field(name="reaction clear", value="16", inline=False)
                        embed.add_field(name="role create", value="17", inline=False)
                        embed.add_field(name="role delete", value="18", inline=False)
                        embed.add_field(name="role update", value="19", inline=False)
                        embed.set_footer(text="Du kannst auf so viele Nummern zu klicken wie du willst")

                        cur.execute("UPDATE server_logs SET owner=?, activated='yes', channelid=? WHERE gid=?",
                                    (auth, logchannel, gid))
                        conn.commit()

                        msg = await message.channel.send(embed=embed)
                        try:
                            await msg.add_reaction(z1)
                            await msg.add_reaction(z2)
                            await msg.add_reaction(z3)
                            await msg.add_reaction(z4)
                            await msg.add_reaction(z5)
                            await msg.add_reaction(z6)
                            await msg.add_reaction(z7)
                            await msg.add_reaction(z8)
                            await msg.add_reaction(z9)
                            await msg.add_reaction(z10)
                            await msg.add_reaction(z11)
                            await msg.add_reaction(z12)
                            await msg.add_reaction(z13)
                            await msg.add_reaction(z14)
                            await msg.add_reaction(z15)
                            await msg.add_reaction(z16)
                            await msg.add_reaction(z17)
                            await msg.add_reaction(z18)
                            await msg.add_reaction(z19)
                        except discord.errors.Forbidden:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Error! Setup wurde abgebrochen da ich nicht die Berrechtigung habe Reaktionen hinzuzu fügen!"))
                        except discord.errors.NotFound:
                            await message.channel.send(
                                content="Sorry! Irgendwas ist falch gelaufen. Bitt joine https://discord.gg/HD7x2vx um Hilfe von mir zu bekommen.")
                        except discord.errors.HTTPException:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Error! I habe einen unbekannten Fehler bitte probiere es erneut oder joine meinem Support Server https://discord.gg/HD7x2vx "))
                    else:
                        await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                       description="Error! Setup wurde abgebrochen es muss z.B. so aus sehen: **386425937748819978**"))
                else:
                    sorry = await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Diesen Command können leider nur Administratoren nutzen. Sorry").set_thumbnail(
                        url="https://thebotdev.de/assets/img/alert.png"))
                    await asyncio.sleep(20)
                    await sorry.delete()

            elif invoke == "send":
                if message.author.guild_permissions.administrator == True or message.author.id == DEINE_USER_ID:
                    me = (message.content).replace("send", "")
                    mes = (me).replace(str(prefix), "")
                    try:
                        await message.channel.send(content=mes)
                    except discord.errors.HTTPException:
                        await message.channel.send(embed=discord.Embed(color=0x64efff,
                                                                       description=prefix + "send [Die nachricht die ich senden soll]"))
                else:
                    sorry = await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Diesen Command können leider nur Administratoren nutzen. Sorry").set_thumbnail(
                        url="https://thebotdev.de/assets/img/alert.png"))
                    await asyncio.sleep(20)
                    await sorry.delete()
            elif invoke == "message":
                setup = await message.channel.send(embed=discord.Embed(color=discord.Color.magenta(),
                                                                       description="OK! Das Setup um die nacheicht zu erstellen wurde gestartet. Bitte sende nun die Farbe die der Rand haben soll (grün/rot/magenta/blau/gold) und wundere dich nicht über diese Nachricht ich werde sie nach dem Setup löschen :) "))

                # time.sleep(4)

                def checkmsg(m):
                    if m.author.id == message.author.id and m.channel.id == message.channel.id:
                        return m

                msgwaitfor = await client.wait_for("message", check=checkmsg, timeout=None)
                if msgwaitfor != None:

                    if msgwaitfor.content == "grün":
                        print("Farbe: Grün")
                        cg = await message.channel.send(embed=discord.Embed(color=discord.Color.green(),
                                                                            description="Du hast die farbe grün gewählt. Als Beispiel wie die nachricht später aussehen wird habe ich den Rand dieser Nacheicht auch grün gefärbt. Also sende mit bitte jetzt den text der in der Nachricht stehen soll."))

                        def checkg(m):
                            if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
                                return m

                        msg2 = await client.wait_for("message", check=checkg, timeout=None)
                        text = await message.channel.send(
                            embed=discord.Embed(color=discord.Color.green(), description=msg2.content))
                        try:
                            await message.delete()
                            await setup.delete()
                            await msgwaitfor.delete()
                            await cg.delete()
                        except:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Oh es sieht so aus als müsste ich mich selbs korrigieren. Ich habe gesagt das ich alle nachrichten des Setup's löschen werde aber wie es aussieht habe ich nicht die Permission's dazu die Permission heisst (Nachrichten verwalten)").set_thumbnail(
                                url="https://thebotdev.de/assets/img/alert.png"))

                    elif msgwaitfor.content == "rot":
                        print("Color: Rot")
                        cg = await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                            description="Du hast die farbe rot gewählt. Als Beispiel wie die nachricht später aussehen wird habe ich den Rand dieser Nacheicht auch rot gefärbt. Also sende mit bitte jetzt den text der in der Nachricht stehen soll."))

                        def checkr(m):
                            if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
                                return m

                        msg2 = await client.wait_for("message", check=None, timeout=None)
                        text = await message.channel.send(
                            embed=discord.Embed(color=discord.Color.red(), description=msg2.content))
                        try:
                            await message.delete()
                            await setup.delete()
                            await msgwaitfor.delete()
                            await cg.delete()
                        except:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Oh es sieht so aus als müsste ich mich selbs korrigieren. Ich habe gesagt das ich alle nachrichten des Setup's löschen werde aber wie es aussieht habe ich nicht die Permission's dazu die Permission heisst (Nachrichten verwalten)").set_thumbnail(
                                url="https://thebotdev.de/assets/img/alert.png"))




                    elif msgwaitfor.content == "blau":
                        print("Color: Blau")
                        cg = await message.channel.send(embed=discord.Embed(color=discord.Color.blue(),
                                                                            description="Du hast die farbe blau gewählt. Als Beispiel wie die nachricht später aussehen wird habe ich den Rand dieser Nacheicht auch blau gefärbt. Also sende mit bitte jetzt den text der in der Nachricht stehen soll."))

                        def checkb(m):
                            if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
                                return m

                        msg2 = await client.wait_for("message", check=checkb, timeout=None)
                        text = await message.channel.send(
                            embed=discord.Embed(color=discord.Color.blue(), description=msg2.content))
                        try:
                            await message.delete()
                            await setup.delete()
                            await msgwaitfor.delete()
                            await cg.delete()
                        except:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Oh es sieht so aus als müsste ich mich selbs korrigieren. Ich habe gesagt das ich alle nachrichten des Setup's löschen werde aber wie es aussieht habe ich nicht die Permission's dazu die Permission heisst (Nachrichten verwalten)").set_thumbnail(
                                url="https://thebotdev.de/assets/img/alert.png"))



                    elif msgwaitfor.content == "magenta":
                        print("Color: Magenta")
                        cg = await message.channel.send(embed=discord.Embed(color=discord.Color.magenta(),
                                                                            description="Du hast die farbe magenta gewählt. Als Beispiel wie die nachricht später aussehen wird habe ich den Rand dieser Nacheicht auch magenta gefärbt. Also sende mit bitte jetzt den text der in der Nachricht stehen soll."))

                        def checkm(m):
                            if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
                                return m

                        msg2 = await client.wait_for("message", check=checkm, timeout=None)
                        text = await message.channel.send(
                            embed=discord.Embed(color=discord.Color.magenta(), description=msg2.content))
                        try:
                            await message.delete()
                            await setup.delete()
                            await msgwaitfor.delete()
                            await cg.delete()
                        except:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Oh es sieht so aus als müsste ich mich selbs korrigieren. Ich habe gesagt das ich alle nachrichten des Setup's löschen werde aber wie es aussieht habe ich nicht die Permission's dazu die Permission heisst (Nachrichten verwalten)").set_thumbnail(
                                url="https://thebotdev.de/assets/img/alert.png"))


                    elif msgwaitfor.content == "gold":
                        print("Color: Gold")
                        cg = await message.channel.send(embed=discord.Embed(color=discord.Color.gold(),
                                                                            description="Du hast die farbe gold gewählt. Als Beispiel wie die nachricht später aussehen wird habe ich den Rand dieser Nacheicht auch gold gefärbt. Also sende mit bitte jetzt den text der in der Nachricht stehen soll."))

                        def checkgold(m):
                            if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
                                return m

                        msg2 = await client.wait_for("message", check=checkgold, timeout=None)
                        text = await message.channel.send(
                            embed=discord.Embed(color=discord.Color.gold(), description=msg2.content))
                        try:
                            await message.delete()
                            await setup.delete()
                            await msgwaitfor.delete()
                            await cg.delete()
                        except:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Oh es sieht so aus als müsste ich mich selbs korrigieren. Ich habe gesagt das ich alle nachrichten des Setup's löschen werde aber wie es aussieht habe ich nicht die Permission's dazu die Permission heisst (Nachrichten verwalten)").set_thumbnail(
                                url="https://thebotdev.de/assets/img/alert.png"))

                    else:
                        print("Farbe nicht erkannt")
        elif message.mentions != None:
            for mentionsn in message.mentions:
                if mentionsn == client.user:
                    await message.channel.send(
                        content="Oh hallo! Hier sind die meist benutzten Commands: " + prefix + "help und " + prefix + "info\n Danke für die Benutzung!")

    async def on_raw_reaction_add(self, emoji, message_id, channel_id, user_id):
        gu = client.get_channel(channel_id)
        guild = gu.guild.id
        gugui = client.get_guild(guild)
        usr = gugui.get_member(user_id)
        gid = gugui.id
        cur.execute("SELECT owner FROM server_logs WHERE gid=?", (gid,))
        owner = cur.fetchone()[0]
        cur.execute("SELECT channel FROM server_game_settings WHERE guildid=?", (gid,))
        chan = cur.fetchall()
        # cur.execute("SELECT channelid FROM server_logs WHERE gid=?")
        # chann = cur.fetchone()[0]	
        if str(chan) != "[]" and user_id != client.user.id:
            print(channel_id)
            cur.execute("SELECT channel FROM server_game_settings WHERE guildid=?", (gid,))
            chan = cur.fetchone()[0]
            print(chan)

            def c(m):
                if m.author.id == user_id:
                    return m

            if chan == channel_id:
                if emoji.id == n1.id:
                    cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?", (user_id, gid))
                    Usersmoney = cur.fetchall()
                    if str(Usersmoney) == "[]":
                        msg = await gu.send(
                            content="Sorry aber du kannst keine Games spielen da du keinen Account hast. Um einen Account zu erstellen mache %sacc und erhalte 2500 Gratis!" % (
                                prefix) + str(moneyicon))
                        await asyncio.sleep(60)
                        await msg.delete()
                    else:
                        cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                                    (user_id, gid))
                        money = cur.fetchone()[0]
                        if money >= 10:
                            newmoney = money - 10
                            cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                        (newmoney, user_id, gid))
                            conn.commit()
                            await gu.send(
                                content="Nun wähle bitte eine Nummer zwischen 1 und 10, und nun sende mit die Zahl.")
                            gedacht = await client.wait_for("message", check=c, timeout=None)
                            botsgedacht = random.randint(1, 10)
                            if botsgedacht == int(gedacht.content):
                                await gu.send(content="Oh das ist richtig meine Nummer war " + str(botsgedacht))
                                newmoney = money + 100
                                cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                            (newmoney, user_id, gid))
                                conn.commit()
                            else:
                                await gu.send(
                                    content="Sorry das war leider nicht die Zahl die ich mir gedacht habe meine war " + str(botsgedacht))
                        else:
                            await gu.send(
                                content="Oh, du kannst dieses Game nicht spielen da du nicht genug Geld hast;( Dein Geld: " + str(
                                    money))
                elif emoji.id == n2.id:
                    cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?", (user_id, gid))
                    Usersmoney = cur.fetchall()
                    if str(Usersmoney) == "[]":
                        msg = await gu.send(
                            content="Sorry aber du kannst keine Games spielen da du keinen Account hast. Um einen Account zu erstellen mache %sacc und erhalte 2500 Gratis!" % (
                                prefix) + str(moneyicon))
                        await asyncio.sleep(60)
                        await msg.delete()
                    else:
                        cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                                    (user_id, gid))
                        money = cur.fetchone()[0]
                        if money >= 10:
                            newmoney = money - 10
                            cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                        (newmoney, user_id, gid))
                            conn.commit()
                            await gu.send(
                                content="So ich habe mir nun eine Nummer zwischen 1 und 20 gedacht, nun sende mir bitte eine Nummer zwischen 1 und 20.")
                            gedacht = await client.wait_for("message", check=c, timeout=None)
                            botsgedacht = random.randint(1, 20)
                            if botsgedacht == int(gedacht.content):
                                await gu.send(content="Wow das ist richtig! My Nummer war " + str(botsgedacht))
                                newmoney = money + 200
                                cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                            (newmoney, user_id, gid))
                                conn.commit()
                            else:
                                await gu.send(
                                    content="Sorry das war leider nicht die Zahl die ich mir gedacht habe meine war " + str(botsgedacht))
                        else:
                            await gu.send(
                                content="Oh, du kannst dieses Game nicht spielen da du nicht genug Geld hast;( Dein Geld: " + str(
                                    money))

                elif emoji.id == n3.id:
                    cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?", (user_id, gid))
                    Usersmoney = cur.fetchall()
                    if str(Usersmoney) == "[]":
                        msg = await gu.send(
                            content="Sorry aber du kannst keine Games spielen da du keinen Account hast. Um einen Account zu erstellen mache %sacc und erhalte 2500 Gratis!" % (
                                prefix) + str(moneyicon))
                        await asyncio.sleep(60)
                        await msg.delete()
                    else:
                        cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                                    (user_id, gid))
                        money = cur.fetchone()[0]
                        if money >= 10:
                            newmoney = money - 10
                            cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                        (newmoney, user_id, gid))
                            conn.commit()
                            await gu.send(
                                content="So ich habe mir nun eine Nummer zwischen 1 und 30 gedacht, nun sende mir bitte eine Nummer zwischen 1 und 30.")
                            gedacht = await client.wait_for("message", check=c, timeout=None)
                            botsgedacht = random.randint(1, 30)
                            if botsgedacht == int(gedacht.content):
                                await gu.send(content="Wow das ist richtig! Meine Nummer war " + str(botsgedacht))
                                newmoney = money + 3000
                                cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                            (newmoney, user_id, gid))
                                conn.commit()
                            else:
                                await gu.send(
                                    content="Sorry aber das war nicht die Nummer die ich mir gedacht habe meine Nummer war " + str(botsgedacht))
                        else:
                            await gu.send(
                                content="Oh, du kannst dieses Game nicht spielen da du nicht genug Geld hast;( Dein Geld: " + str(
                                    money))

                elif emoji.id == n4.id:
                    cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?", (user_id, gid))
                    Usersmoney = cur.fetchall()
                    if str(Usersmoney) == "[]":
                        msg = await gu.send(
                            content="Oh, du kannst dieses Game nicht spielen da du nicht genug Geld hast;( Dein Geld: " + str(
                                prefix) + str(moneyicon))
                        await asyncio.sleep(60)
                        await msg.delete()
                    else:
                        cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                                    (user_id, gid))
                        money = cur.fetchone()[0]
                        if money >= 10:
                            newmoney = money - 10
                            cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                        (newmoney, user_id, gid))
                            conn.commit()
                            await gu.send(
                                content="So ich habe mir nun eine Nummer zwischen 1 und 40 gedacht, nun sende mir bitte eine Nummer zwischen 1 und 40.")
                            gedacht = await client.wait_for("message", check=c, timeout=None)
                            botsgedacht = random.randint(1, 40)
                            if botsgedacht == int(gedacht.content):
                                await gu.send(content="Wow das ist richtig! Meine Nummer war " + str(botsgedacht))
                                newmoney = money + 40000
                                cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                            (newmoney, user_id, gid))
                                conn.commit()
                            else:
                                await gu.send(
                                    content="Sorry das ist nicht die Nummer die ich mir gedacht habe. ich habe mir die Zahl " + str(botsgedacht) + " gedacht")
                        else:
                            await gu.send(
                                content="Oh, du kannst dieses Game nicht spielen da du nicht genug Geld hast;( Dein Geld: " + str(
                                    money))

                elif emoji.id == n5.id:
                    cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?", (user_id, gid))
                    Usersmoney = cur.fetchall()
                    if str(Usersmoney) == "[]":
                        msg = await gu.send(
                            content="Sorry aber du kannst keine Games spielen da du keinen Account hast. Um einen Account zu erstellen mache %sacc und erhalte 2500 Gratis!" % (
                                prefix) + str(moneyicon))
                        await asyncio.sleep(60)
                        await msg.delete()
                    else:
                        cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                                    (user_id, gid))
                        money = cur.fetchone()[0]
                        if money >= 10:
                            newmoney = money - 10
                            cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                        (newmoney, user_id, gid))
                            conn.commit()
                            await gu.send(
                                content="So ich habe mir nun eine Nummer zwischen 1 und 50 gedacht, nun sende mir bitte eine Nummer zwischen 1 und 50.")
                            gedacht = await client.wait_for("message", check=c, timeout=None)
                            botsgedacht = random.randint(1, 50)
                            if botsgedacht == int(gedacht.content):
                                await gu.send(content="Wow das ist richtig! Meine Nummer war " + str(botsgedacht))
                                newmoney = money + 5555
                                cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                            (newmoney, user_id, gid))
                                conn.commit()
                            else:
                                await gu.send(
                                    content="Sorry das ist nicht die Nummer die ich mir gedacht habe. ich habe mir die Zahl " + str(botsgedacht) + " gedacht")
                        else:
                            await gu.send(
                                content="Oh, du kannst dieses Game nicht spielen da du nicht genug Geld hast;( Dein Geld: " + str(
                                    money))
        if owner == user_id:
            if emoji.id == z1.id:
                cur.execute("UPDATE server_logs SET a1=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z2.id:
                cur.execute("UPDATE server_logs SET a2=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z3.id:
                cur.execute("UPDATE server_logs SET a3=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z4.id:
                cur.execute("UPDATE server_logs SET a4=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z5.id:
                cur.execute("UPDATE server_logs SET a5=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z6.id:
                cur.execute("UPDATE server_logs SET a6=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z7.id:
                cur.execute("UPDATE server_logs SET a7=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z8.id:
                cur.execute("UPDATE server_logs SET a8=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z9.id:
                cur.execute("UPDATE server_logs SET a9=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z10.id:
                cur.execute("UPDATE server_logs SET a10=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z11.id:
                cur.execute("UPDATE server_logs SET a11=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z12.id:
                cur.execute("UPDATE server_logs SET a12=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z13.id:
                cur.execute("UPDATE server_logs SET a13=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z14.id:
                cur.execute("UPDATE server_logs SET a14=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z15.id:
                cur.execute("UPDATE server_logs SET a15=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z16.id:
                cur.execute("UPDATE server_logs SET a16=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z17.id:
                cur.execute("UPDATE server_logs SET a17=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z18.id:
                cur.execute("UPDATE server_logs SET a18=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z19.id:
                cur.execute("UPDATE server_logs SET a19=1 WHERE gid=?", (gid,))
                conn.commit()
            else:
                cur.execute("SELECT a14 FROM server_logs WHERE gid=?", (gid,))
                data = cur.fetchone()[0]
                if data == 0 or data == None:
                    pass
                if data == 1:
                    cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
                    ch = cur.fetchone()[0]
                    channel = client.get_channel(ch)
                    await channel.send(embed=discord.Embed(color=discord.Color.green(), description="Der User " + str(
                        usr.mention) + " reagierte mit " + str(emoji)).set_author(name=usr.name + " hat reagiert",
                                                                                 icon_url=usr.avatar_url))

        else:
            cur.execute("SELECT a14 FROM server_logs WHERE gid=?", (gid,))
            data = cur.fetchone()[0]
            if data == 0 or data == None:
                pass
                if data == 1:
                    cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
                    ch = cur.fetchone()[0]
                    channel = client.get_channel(ch)
                    await channel.send(embed=discord.Embed(color=discord.Color.green(), description="Der User " + str(
                        usr.mention) + " reagierte mit " + str(emoji)).set_author(name=usr.name + " hat reagiert",
                                                                                 icon_url=usr.avatar_url))

    async def on_raw_reaction_remove(self, emoji, message_id, channel_id, user_id):
        gu = client.get_channel(channel_id)
        guild = gu.guild.id
        gugui = client.get_guild(guild)
        usr = gugui.get_member(user_id)
        gid = gugui.id
        cur.execute("SELECT owner FROM server_logs WHERE gid=?", (gid,))
        owner = cur.fetchone()[0]
        if owner == user_id:
            if emoji.id == z1.id:
                cur.execute("UPDATE server_logs SET a1=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z2.id:
                cur.execute("UPDATE server_logs SET a2=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z3.id:
                cur.execute("UPDATE server_logs SET a3=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z4.id:
                cur.execute("UPDATE server_logs SET a4=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z5.id:
                cur.execute("UPDATE server_logs SET a5=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z6.id:
                cur.execute("UPDATE server_logs SET a6=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z7.id:
                cur.execute("UPDATE server_logs SET a7=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z8.id:
                cur.execute("UPDATE server_logs SET a8=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z9.id:
                cur.execute("UPDATE server_logs SET a9=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z10.id:
                cur.execute("UPDATE server_logs SET a10=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z11.id:
                cur.execute("UPDATE server_logs SET a11=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z12.id:
                cur.execute("UPDATE server_logs SET a12=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z13.id:
                cur.execute("UPDATE server_logs SET a13=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z14.id:
                cur.execute("UPDATE server_logs SET a14=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z15.id:
                cur.execute("UPDATE server_logs SET a15=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z16.id:
                cur.execute("UPDATE server_logs SET a16=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z17.id:
                cur.execute("UPDATE server_logs SET a17=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z18.id:
                cur.execute("UPDATE server_logs SET a18=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z19.id:
                cur.execute("UPDATE server_logs SET a19=0 WHERE gid=?", (gid,))
                conn.commit()
            else:
                cur.execute("SELECT a15 FROM server_logs WHERE gid=?", (gid,))
                data = cur.fetchone()[0]
                if data == 0 or data == None:
                    pass
                if data == 1:
                    cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
                    ch = cur.fetchone()[0]
                    channel = client.get_channel(ch)
                    await channel.send(embed=discord.Embed(color=discord.Color.green(), description="Der User " + str(
                        usr.mention) + " entfernte die Reaktion " + str(emoji)).set_author(name=usr.name + " hat reagiert",
                                                                                 icon_url=usr.avatar_url))

        else:
            cur.execute("SELECT a15 FROM server_logs WHERE gid=?", (gid,))
            data = cur.fetchone()[0]
            if data == 0 or data == None:
                pass
                if data == 1:
                    cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
                    ch = cur.fetchone()[0]
                    channel = client.get_channel(ch)
                    await channel.send(embed=discord.Embed(color=discord.Color.green(), description="Der User " + str(
                        usr.mention) + " entfernte die Reaktion " + str(emoji)).set_author(name=usr.name + " hat reagiert",
                                                                                 icon_url=usr.avatar_url))

    async def on_raw_reaction_clear(self, message_id, channel_id):
        chan = client.get_channel(channel_id)
        gid = chan.guild.id
        cur.execute("SELECT a16 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=discord.Color.blue(),
                                                   description="Reaktionen einer Nachricht im Channel " + str(
                                                       chan.mention) + "wurden gelöscht").set_author(
                name=chan.guild.name, icon=chan.guild.icon_url))

    async def on_member_join(self, member):
        gid = member.guild.id
        cur.execute("SELECT a1 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            usr = client.get_user(member.id)

            embed = discord.Embed(title="User jointe dem Server", color=0x00ff00)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Username:", value=member.name, inline=True)
            embed.add_field(name="Discriminator:", value=member.discriminator, inline=True)
            embed.add_field(name="User ID:", value=member.id, inline=True)
            embed.add_field(name="Erstellt am:", value=member.created_at, inline=True)
            await channel.send(embed=embed)

    async def on_member_remove(self, member):
        gid = member.guild.id
        cur.execute("SELECT a2 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            usr = client.get_user(member.id)

            embed = discord.Embed(title="User hat den Server verlassen", color=discord.Color.red())
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Username:", value=member.name, inline=True)
            embed.add_field(name="Discriminator:", value=member.discriminator, inline=True)
            embed.add_field(name="User ID:", value=member.id, inline=True)
            embed.add_field(name="Erstellt am:", value=member.created_at, inline=True)
            await channel.send(embed=embed)

    async def on_member_update(self, before, after):

        gid = before.guild.id
        cur.execute("SELECT a3 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            if before.nick != after.nick:
                await channel.send(embed=discord.Embed(color=0x64efff, description="Der User " + str(
                    before.name) + " änderte seinen Nickname von " + str(before.nick) + " zu " + str(after.nick)).set_author(
                    name=before.name, icon_url=before.avatar_url))
            elif before.status != after.status:
                await channel.send(embed=discord.Embed(color=0x64efff, description="Der User " + str(
                    before.name) + " änderte seinen Status von " + str(before.status) + " zu " + str(
                    after.status)).set_author(name=before.name, icon_url=before.avatar_url))
            elif before.game != after.game:
                await channel.send(embed=discord.Embed(color=0x64efff, description="Der User " + str(
                    before.name) + " änderte sein Game von " + str(before.game) + " zu " + str(after.game)).set_author(
                    name=before.name, icon_url=before.avatar_url))
            elif before.avatar_url != after.avatar_url:
                await channel.send(embed=discord.Embed(color=0x64efff, description="Der User " + str(
                    before.name) + " änderte seinen Avatar zu ->").set_thumbnail(url=after.avatar_url))

            elif before.roles != after.roles:
                if len(before.roles) < len(after.roles):
                    await channel.send(embed=discord.Embed(color=0x64efff, description="Der User " + str(
                        before.name) + " wurde folgende Rolle geaddet").set_author(name=before.name, icon_url=before.avatar_url))
                elif len(before.roles) > len(after.roles):
                    await channel.send(embed=discord.Embed(color=0x64efff, description="Der User " + str(
                        before.name) + " wurde folgende Rolle entfernt").set_author(name=before.name,
                                                                              icon_url=before.avatar_url))

    async def on_member_ban(self, guild, user):
        gid = guild.id
        cur.execute("SELECT a4 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=discord.Color.red(), description="Der User " + str(
                user.name) + " wurde gebannt vom Server ").set_author(name=user.name, icon_url=user.avatar_url))

    async def on_member_unban(self, guild, user):
        gid = guild.id
        cur.execute("SELECT a5 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=discord.Color.green(), description="Der User " + str(
                user.name) + " wurde vom Server entbannt ").set_author(name=user.name, icon_url=user.avatar_url))

    async def on_raw_message_delete(self, message_id, channel_id):
        channelmessage = client.get_channel(channel_id)
        print(channelmessage.name)
        # message = channel.get_message(message_id)
        gid = channelmessage.guild.id
        guild = channelmessage.guild
        cur.execute("SELECT a6 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            print(message_id)
            await channel.send(embed=discord.Embed(color=discord.Color.red(), description="Message im Channel " + str(
                channelmessage.mention) + " wurde gelöscht.").set_author(name=guild.name + "| Log gelöschte Nachricht",
                                                                      icon_url=guild.icon_url))

    async def on_raw_bulk_message_delete(self, message_ids, channel_id):
        channel = client.get_channel(channel_id)
        anzahl = len(message_ids)
        gid = channel.guild.id
        guild = channel.guild
        cur.execute("SELECT a7 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            print(message_id)
            await channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                   description=anzahl + "x Nachrichten im Channel " + str(
                                                       channel.mention) + " wurden gelöscht.").set_author(
                name=guild.name + "| Log gelöschte Nachrichten", icon_url=guild.icon_url))

    async def on_message_edit(self, before, after):
        gid = before.author.guild.id
        cur.execute("SELECT a8 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            if before.content != after.content:
                cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
                ch = cur.fetchone()[0]
                channel = client.get_channel(ch)
                if before.content != "":
                    await channel.send(embed=discord.Embed(color=0x64efff, description="Die Nachricht:\n`" + str(
                        before.content) + "`\n wurde geändert zu:\n`" + str(after.content) + "`").set_author(
                        name=before.author, icon_url=before.author.avatar_url))
                else:
                    pass

    async def on_guild_channel_create(self, neuerchannel):
        gid = neuerchannel.guild.id
        cur.execute("SELECT a9 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=0x64efff, description="Der Channel " + str(
                neuerchannel.mention) + " wurde erstellt"))

    async def on_guild_channel_delete(self, neuerchannel):
        gid = neuerchannel.guild.id
        cur.execute("SELECT a11 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=0x64efff, description="Der Channel " + str(
                neuerchannel.name) + " wurde gelöscht"))

    async def on_guild_channel_update(self, before, after):
        gid = before.guild.id
        cur.execute("SELECT a10 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            if before.name != after.name:
                await channel.send(embed=discord.Embed(color=0x64efff, description="Der Channel Name wurde von " + str(
                    after.mention) + " geändert von `" + str(before.name) + "` zu `" + str(after.name) + "`"))
            elif before.topic != after.topic:
                await channel.send(embed=discord.Embed(color=0x64efff, description="Der Topic vom Channel " + str(
                    after.mention) + " wurde geändert zu:\n `" + str(after.topic) + "`"))
            else:
                await channel.send(embed=discord.Embed(color=0x64efff, description="Der Channel " + str(
                    after.mention) + " wurde geupdatet."))

    async def on_voice_state_update(self, member, before, after):
        memberid = member.id
        memb = member.guild.get_member(memberid)
        gid = member.guild.id
        cur.execute("SELECT a12 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            counterbefore = 0
            counterafter = 0
            if before.channel != None:
                counterbefore = counterbefore + 1
            elif after.channel != None:
                counterafter = counterafter + 1
            if counterbefore < counterafter:
                await channel.send(embed=discord.Embed(color=0x64efff, description="-> Der User " + str(
                    member.name) + " jointe " + str(after.channel.name)).set_author(name=member.name,
                                                                                     icon_url=member.avatar_url))
            elif counterbefore > counterafter + 1000000:
                await channel.send(embed=discord.Embed(color=0x64efff,
                                                       description="-> Der User " + str(memb.name) + " leavte " + str(
                                                           after.channel.name)).set_author(name=memb.name,
                                                                                           icon_url=memb.avatar_url))

    async def on_guild_emojis_update(self, guild, before, after):
        gid = guild.id
        cur.execute("SELECT a13 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            if len(before) < len(after):
                await channel.send(embed=discord.Embed(color=discord.Color.green(),
                                                       description="-> Ein Emoji wurde zum Server geaddet ").set_author(
                    name=guild.name, icon_url=guild.icon_url))
            elif len(before) > len(after):
                await channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                       description="<- Ein Emoji wurde vom Server gelöscht ").set_author(
                    name=guild.name, icon_url=guild.icon_url))

    async def on_guild_role_create(self, role):
        gid = role.guild.id
        cur.execute("SELECT a17 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=discord.Color.green(), description="Die Rolle `" + str(
                role.name) + "` wurde erstellt").set_author(name=role.guild.name, icon_url=role.guild.icon_url))

    async def on_guild_role_delete(self, role):
        gid = role.guild.id
        cur.execute("SELECT a18 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=discord.Color.green(), description="Die Rolle `" + str(
                role.name) + "` wurde gelöscht").set_author(name=role.guild.name, icon_url=role.guild.icon_url))

    async def on_guild_role_update(self, before, after):
        gid = after.guild.id
        cur.execute("SELECT a19 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            if before.name == after.name:
                await channel.send(embed=discord.Embed(color=discord.Color.green(), description="Die Rolle `" + str(
                    after.name) + "` wurde geupdatet").set_author(name=after.guild.name, icon_url=after.guild.icon_url))
            elif before.name != after.name:
                await channel.send(embed=discord.Embed(color=discord.Color.green(),
                                                       description="Der Rollen Name wurde geändert von `" + str(
                                                           before.name) + "` zu `" + str(after.name) + "`").set_author(
                    name=after.guild.name, icon_url=after.guild.icon_url))

    async def on_guild_join(self, guild):

        gid = guild.id
        gnm = guild.name
        prefixnormalsetting = "!"
        cur.execute("INSERT INTO server_settings(gid, prefix) VALUES(?, ?)", (gid, prefixnormalsetting))
        cur.execute("INSERT INTO server_logs(gid) VALUES(?)", (gid,))
        conn.commit()

    async def on_guild_remove(self, guild):
        gid = guild.id
        cur.execute("DELETE FROM server_settings WHERE gid=?", (gid,))
        cur.execute("DELETE FROM server_logs WHERE gid=?", (gid,))
        conn.commit()


client = MyClient()
client.run(KEYS.TOKEN)
