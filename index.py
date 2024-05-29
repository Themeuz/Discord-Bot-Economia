import discord
from discord.ext import commands
import time

perm  = discord.Intents.default()
perm.message_content = True
perm.members = True
bot = commands.Bot(command_prefix="/", intents=perm)


@bot.command()
async def comandos(ctx:commands.Context):
    user = ctx.author
    await ctx.reply(f"Olá, {user.display_name}!\nAqui estão todos os meus comandos.\n")

@bot.command()
async def enviarembed(ctx:commands.Context):
    meu_embed = discord.Embed(title='Hello World', description='Me livrei da maldição!')
    await ctx.reply(embed=meu_embed)

@bot.command()
async def resgatar(ctx:commands.Context):
    async def resposta_botao(interact:discord.Interaction):
        await interact.response.send_message("Verificando se você tem direito a moedas, aguarde...")
        time.sleep(1)
        await interact.followup.send('Você recebeu X em moedas diárias!')
    view = discord.ui.View()
    botao = discord.ui.Button(label='Abrir Baú')
    botao.callback = resposta_botao

    botao_jogo = discord.ui.Button(label='Tarefas')
    botao_nuuvem = discord.ui.Button(label='Acesse ao site da Nuuvem', url='https://www.nuuvem.com/br-pt/')


    view.add_item(botao)
    view.add_item(botao_jogo)
    view.add_item(botao_nuuvem)
    await ctx.reply(view=view)


@bot.event
async def on_member_join(user:discord.Member):
    channel = bot.get_channel(CHANNEL_ID_TROQUE)
    meu_embed = discord.Embed(title=f"Bem vindo, {user.name}!")
    meu_embed.description= "Você recebeu 100 moedas de boas vindas!"
    await channel.send(embed=meu_embed)


@bot.event
async def on_ready():
    print("Você me acordou!")
bot.run('bot_token')
