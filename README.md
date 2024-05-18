# Bot de Tarefas para Discord

Um bot de Discord simples para gerenciar uma lista de tarefas, incluindo funcionalidades para adicionar, listar e remover tarefas. 

## Descrição

Este projeto é um bot de Discord desenvolvido com `discord.py` que permite aos usuários gerenciar uma lista de tarefas diretamente em um canal do Discord. O bot salva as tarefas em um arquivo de texto (`tarefas.txt`) para que persistam entre reinicializações do bot.

## Funcionalidades

- Adicionar uma tarefa à lista.
- Listar todas as tarefas.
- Remover uma tarefa da lista por índice.
- Comando adicional para juntar strings fornecidas pelo usuário.

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
