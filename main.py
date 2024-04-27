# This example requires the 'message_content' intent.

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

lista= []

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id != 1233778618187120761:
        return
    if message.author == client.user:
        return
    if messase.content.startswith('!tarefa adicinonar')
        async def adicionar_tarefas(ctx, *, tarefa)
            lista.append(tarefa)
           await ctx.send(f'Tarefa"{tarefa}"adicionada a lista')
        



#id da sala = 1233778618187120761

client.run('MTIzMzc2OTAyNTA2MzA5MjMxNg.GNhFlk.i3IS6wJmuhMecX7wR4mc3m58_vO8-lEoYelsxg')