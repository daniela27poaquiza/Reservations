import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.listen()
async def on_ready():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hi {ctx.author.display_name}")
    
@bot.command()
async def reservations(ctx):
    await ctx.send(while restart != ('N','NO','n','no'):
print("RESREVE")
answer = ("Y")

while answer != ('N','NO','n','no'):
    print("1.Check pnr status")
    print("2.Table and Game Reservation")
    option = int(input("\nEnter your option : "))
    
    if option == 1:
        print("Your pnr status is t2")
        exit(0)
  
    elif option == 2:
        people = int(input("\nEnter no. of people at table: "))
        name_l = []
        game_l = []
        table_l = []
        for p in range(people):2
        name = str(input("\nName : "))
        name_l.append(name)
        game = str(input("\nGame  : "))
        game_l.append(game)
        table  = str(input("\nTable number : "))
        table_l.append(table)

        answer = str(input("\nOops! Forget someone : "))
        if answer in ('y','YES','yes','Yes'):
                answer = ('Y')
        else:
                    x=0
        print("People : ",people)
        print("Name : ", name_l[x])
        print("Game  : ", game_l[x])
        print("Table : ", table_l[x])
        x += 1
bot.run(TOKEN)
