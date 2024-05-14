import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

FILENAME = "tarefas.txt"

def carregar_lista():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            linhas = f.readlines()  
            tarefas = [linha.strip() for linha in linhas]
            return tarefas
    else:
        return []


def salvar_lista(lista):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for tarefa in lista:
            f.write(f"{tarefa}\n")



client = commands.Bot(command_prefix='!', intents=intents) 


lista = carregar_lista()


@client.event
async def on_message(message):
    if message.channel.id != #id da sala de comandos:
        return  

    await client.process_commands(message)  


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.group(name='tarefas')
async def tarefas(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Use os subcomandos: \nadicionar - Para adicionar uma tarefa a lista. \nlistar - Para listar todas as tarefas incluidas na lista. \nremover - Para remover uma tarefa da lista ")

@tarefas.command(name='adicionar')
async def adicionar_tarefa(ctx, *, tarefa: str = None):
    if tarefa:
        lista.append(tarefa)
        salvar_lista(lista)
        await ctx.send(f'Tarefa "{tarefa}" adicionada à lista.')
    else:
        await ctx.send("Por favor, forneça uma tarefa para adicionar.")

@tarefas.command(name='listar')
async def listar_tarefas(ctx):
    if lista:
        tarefas_listadas = "\n".join(f"- {i+1}: {tarefa}" for i, tarefa in enumerate(lista))
        await ctx.send(f"Tarefas na lista:\n{tarefas_listadas}")
    else:
        await ctx.send("A lista de tarefas está vazia.")

@tarefas.command(name='remover')
async def remover_tarefa(ctx, indice: int):
    if 0 < indice <= len(lista):
        tarefa_removida = lista.pop(indice - 1)  
        salvar_lista(lista)
        await ctx.send(f'Tarefa "{tarefa_removida}" foi removida.')
    else:
        await ctx.send(f"Item da lista invalido. Forneça um número entre 1 e {len(lista)}.")

@client.command(name='juntar')        
async def juntar_strings(ctx, *args):
    if args:
        string_args = [str(arg) for arg in args] 
        resultado = " ".join(string_args) 
        await ctx.send(resultado)
    else:
        await ctx.send("Forneça pelo menos uma string para juntar.")

        

client.run('Token do seu bot')
