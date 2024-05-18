# Bot de Tarefas para Discord

Um bot de Discord simples para gerenciar uma lista de tarefas, incluindo funcionalidades para adicionar, listar e remover tarefas. 

## Descrição

Este projeto é um bot de Discord desenvolvido com `discord.py` que permite aos usuários gerenciar uma lista de tarefas diretamente em um canal do Discord. O bot salva as tarefas em um arquivo de texto (`tarefas.txt`) para que persistam entre reinicializações do bot.

## Funcionalidades

- Adicionar uma tarefa à lista.
- Listar todas as tarefas.
- Remover uma tarefa da lista por índice.
- Comando adicional para juntar strings fornecidas pelo usuário.

## Estrutura do Código

### Importações e Configuração Inicial

```python
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
```

- `discord` e `discord.ext.commands`: Importações da biblioteca `discord.py` para interagir com a API do Discord.

- `os`: Biblioteca padrão do Python para interagir com o sistema operacional.

- `intents`: Configurações de intenções do bot. Aqui, estamos ativando a intenção para ler o conteúdo das mensagens.

### Funções para Carregar e Salvar Tarefas

```python
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

```
- `FILENAME`: Nome do arquivo onde as tarefas serão salvas.
- `carregar_lista()`: Função que carrega as tarefas do arquivo `tarefas.txt`. Se o arquivo não existir, retorna uma lista vazia.
- `salvar_lista(lista)`: Função que salva a lista de tarefas no arquivo `tarefas.txt`.

### Configuração do Bot

```python
client = commands.Bot(command_prefix='!', intents=intents)
lista = carregar_lista()
```
- `client`: Instância do bot, configurada com o prefixo `!` para os comandos e as intenções definidas anteriormente.
- `lista`: Carrega a lista de tarefas do arquivo.

### Eventos do Bot

#### on_message
```python
@client.event
async def on_message(message):
    if message.channel.id != #id da sala de comandos:
        return  
    await client.process_commands(message)
```
- `on_message`: Evento que é chamado sempre que uma mensagem é enviada em um canal. Aqui, ele verifica se a mensagem foi enviada no canal de comandos específico (substitua `#id da sala de comandos` pelo ID real) e processa os comandos.

#### on_ready
```python
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
```
- `on_ready`: Evento que é chamado quando o bot é iniciado e está pronto para uso.

### Comandos de Gerenciamento de Tarefas

#### Grupo de Comandos: tarefas
```python
@client.group(name='tarefas')
async def tarefas(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Use os subcomandos: \nadicionar - Para adicionar uma tarefa à lista. \nlistar - Para listar todas as tarefas incluídas na lista. \nremover - Para remover uma tarefa da lista.")
```
- `tarefas`: Grupo de comandos para gerenciamento de tarefas. Exibe uma mensagem de ajuda se nenhum subcomando for fornecido.

#### Subcomando: adicionar
```python
@tarefas.command(name='adicionar')
async def adicionar_tarefa(ctx, *, tarefa: str = None):
    if tarefa:
        lista.append(tarefa)
        salvar_lista(lista)
        await ctx.send(f'Tarefa "{tarefa}" adicionada à lista.')
    else:
        await ctx.send("Por favor, forneça uma tarefa para adicionar.")
```
- `adicionar_tarefa`: Adiciona uma nova tarefa à lista e salva a lista atualizada no arquivo.

#### Subcomando: listar

```python
@tarefas.command(name='listar')
async def listar_tarefas(ctx):
    if lista:
        tarefas_listadas = "\n".join(f"- {i+1}: {tarefa}" for i, tarefa in enumerate(lista))
        await ctx.send(f"Tarefas na lista:\n{tarefas_listadas}")
    else:
        await ctx.send("A lista de tarefas está vazia.")
```
- `listar_tarefas`: Lista todas as tarefas atualmente na lista.

#### Subcomando: remover

```python
@tarefas.command(name='listar')
async def listar_tarefas(ctx):
    if lista:
        tarefas_listadas = "\n".join(f"- {i+1}: {tarefa}" for i, tarefa in enumerate(lista))
        await ctx.send(f"Tarefas na lista:\n{tarefas_listadas}")
    else:
        await ctx.send("A lista de tarefas está vazia.")
```
- `remover_tarefa`: Remove uma tarefa da lista com base no índice fornecido.

#### Subcomando: juntar
```python
@client.command(name='juntar')        
async def juntar_strings(ctx, *args):
    if args:
        string_args = [str(arg) for arg in args] 
        resultado = " ".join(string_args) 
        await ctx.send(resultado)
    else:
        await ctx.send("Forneça pelo menos uma string para juntar.")
```
- `juntar_strings`: Junta múltiplas strings fornecidas pelo usuário em uma única string e a exibe.

### Inicialização do Bot

```python
client.run('Token do seu bot')
```
- `client.run('Token do seu bot')`: Inicializa o bot com o token fornecido (substitua `'Token do seu bot'` pelo token real do seu bot do Discord).

## Como usar
#### 1. Adicionar Tarefa:
```diff
!tarefas adicionar <tarefa>
```

#### 2. Listar Tarefa:
```diff
!tarefas listar
```
#### 3. Remover Tarefa:
```diff
!tarefas remover <indice>
```

#### 4. Juntar Strings:
```diff
!juntar <strings>
```

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual (recomendado) e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install discord.py
    ```

4. Crie um arquivo `tarefas.txt` no mesmo diretório do script, se ele ainda não existir:
    ```bash
    touch tarefas.txt
    ```

5. Substitua `'Token do seu bot'` no código pelo token do seu bot do Discord.

6. Subistitua `#id da sala` no código pelo id da sala que deseja que ele receba comando.

## Uso

Execute o bot com o seguinte comando:
```bash
python seu-script.py
```
