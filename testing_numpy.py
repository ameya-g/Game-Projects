from discord import emoji
import numpy as np
import discord
from discord import channel 
import time
import json

op = open('config.json',)
token_data = json.load(op)

TOKEN = token_data.get('token')

from discord.channel import CategoryChannel, TextChannel

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

## ~~ENDING OF DISCORD IMPLEMENTATIONS~~ ##

# height = int(input("Height of the board: "))
# length = int(input("Length of the board: "))

def display(list):
    list = np.array(list)
    print (list)

# Generates the board using 1's and 0's
def board_gen(height,length):
    basic_board = np.zeros((height,length), dtype=int)
    basic_board = basic_board.tolist()

    for y in (range(height)):
        if y == 0 or y == height-1:
            basic_board[y] = np.ones(length, dtype=int).tolist()

        for x in (range(length)):
            if x == 0 or x == length-1:
                basic_board[y][x] = 1
    
    return basic_board

# Converts 1's and 0's into emojis
def emojifier(board_list):
    for y in range(len(board_list)):
        for x in range(len(board_list[y])):
            if board_list[y][x] == 1:
                board_list[y][x] = ":white_large_square:"
            elif board_list[y][x] == 0:
                board_list[y][x] = ":black_large_square:"
    return board_list

def into_one_message(emogified):
    sing_msg = ""
    for wow in emogified:
        for lol in wow:
            sing_msg += lol
        sing_msg += "\n"
    return sing_msg

## ~~DISCORD MESSAGE SENDER~~##
@client.event
async def on_message(message):
    msg = message.content

    if msg.startswith("!rect"):
        msg = msg[6:]
        dim_list = msg.split()
        l = int(dim_list[0])
        h = int(dim_list[1])

        completed = into_one_message(emojifier(board_gen(h,l)))

        await message.channel.send(completed)

client.run(TOKEN)