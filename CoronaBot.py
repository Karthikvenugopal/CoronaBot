import requests
import discord

client = discord.Client()


@client.event
async def on_message(message):
    message.content.lower()
    mess = message.content
    if message.author == client.user:
        return
    if message.content.startswith("corona"):
        await message.channel.send("Hello, " + str(message.author) + " I am a bot which gives you CoViD-19 details of India")
        # if message.content == "corona":
        flag = mess[7:]
        if flag == "--help":
            await message.channel.send("To get CoViD-19 details type \"corona [name of the Indian state]\"")
        else:
            try:
                res = requests.get(
                    url="https://api.covid19india.org/state_district_wise.json")
                res = res.json()
                confirm, deceased, recovered, delcon, deldec, delrec = 0, 0, 0, 0, 0, 0
                for i in res[flag]["districtData"]:
                    confirm = confirm + \
                        res[flag]["districtData"][i]["confirmed"]
                    deceased = deceased + \
                        res[flag]["districtData"][i]["deceased"]
                    recovered = recovered + \
                        res[flag]["districtData"][i]["recovered"]
                    delrec = delrec + \
                        res[flag]["districtData"][i]["delta"]["recovered"]
                    delcon = delcon + \
                        res[flag]["districtData"][i]["delta"]["confirmed"]
                    deldec = deldec + \
                        res[flag]["districtData"][i]["delta"]["deceased"]

                await message.channel.send("**`"+flag + "`**\n\n:red_circle: `confirmed: " + str(confirm) + "` :red_circle:\n:muscle: `recovered: " + str(recovered) + "` :muscle:\n:blossom: `deceased: " + str(deceased) + "` :blossom:\n\n`Daily change:` \n\n:red_circle: `confirmed: " + (str(delcon) if delcon != 0 else "Not updated yet") + "`" + ":red_circle:\n:muscle: `recovered: " + (str(delrec) if delrec != 0 else "Not updated yet") + "`" + ":muscle:\n:blossom: `deceased: " + (str(deldec) if deldec != 0 else "Not updated yet")+"`:blossom:")
            except:
                await message.channel.send("Please enter the state name correctly")

client.run([Token])
