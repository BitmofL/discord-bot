# Импортируем необходимые модули из библиотеки disnake.
import disnake
from disnake.ext import commands


# Определяем класс "ButtonView", который наследуется от disnake.ui.View.
class ButtonView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    # Создаем кнопку "button1" с соответствующей функцией-обработчиком.
    @disnake.ui.button(label="♂️", style=disnake.ButtonStyle.blurple, custom_id="button1")
    async def button1(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        # Получаем роль по ее ID (необходимо указать конкретный ID вместо ...).
        role = interaction.guild.get_role(1213849787955417191)

        # Проверяем, есть ли у пользователя эта роль, и добавляем/убираем ее соответственно.
        if role in interaction.author.roles:
            await interaction.author.remove_roles(role)
        else:
            await interaction.author.add_roles(role)

        # Отправляем ответ для показа, что бот обработал нажатие кнопки.
        await interaction.response.defer()

    # Создаем кнопку "button2" с соответствующей функцией-обработчиком.
    @disnake.ui.button(label="♀️", style=disnake.ButtonStyle.blurple, custom_id="button2")
    async def button2(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        # Получаем роль по ее ID (необходимо указать конкретный ID вместо ...).
        role = interaction.guild.get_role(1213851693435850823)

        # Проверяем, есть ли у пользователя эта роль, и добавляем/убираем ее соответственно.
        if role in interaction.author.roles:
            await interaction.author.remove_roles(role)
        else:
            await interaction.author.add_roles(role)

        # Отправляем ответ для показа, что бот обработал нажатие кнопки.
        await interaction.response.defer()

        # Создаем кнопку "button3" с соответствующей функцией-обработчиком.


       # @disnake.ui.button(label="Профиль", style=disnake.ButtonStyle.blurple, custom_id="button3", url="https://discord.com/channels/793901633703903284/839975686037962793")
                  #async def button3(self, button: disnake.ui.Button, interaction: disnake.Interaction):
                  #  await ctx.send("Профиль")




# Определяем класс "ButtonsRole", который является расширением (Cog) для бота.
class ButtonsRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False

    # Создаем команду "gender", которая будет выводить сообщение с кнопкой.
    @commands.command()
    async def gender(self, ctx):
        view = ButtonView()

        # Получаем роль по ее ID (необходимо указать конкретный ID вместо ...).
        role = ctx.guild.get_role(1213849787955417191)

        embed = disnake.Embed(color=0x2F3136)
        embed.set_author(name="Пол:")
       # embed.description = f"На сервере ежедневно проходят различные мероприятия. " \
         #                   "Для того чтобы быть в курсе предстоящих событий, нажми на кнопку ниже. " \
         #                   "Повторное нажатие убирает роль."
        #embed.set_image(url="https://i.imgur.com/QzB7q9J.png")
        await ctx.send(embed=embed, view=view)

    # Создаем слушателя события "on_ready", который добавляет персистентную кнопку.
    @commands.Cog.listener()
    async def on_ready(self):
        if self.persistent_views_added:
            return

        # Message ID сообщения, где будет кнопка, добавляется после отправки команды.
        # Нужно будет скопировать ID сообщения и вставить вместо "...", после выполнения данных действий
        # необходимо перезапустить бота.
        self.bot.add_view(ButtonView(), message_id=...)


# Функция setup, которая добавляет класс ButtonsRole как Cog (команду-расширение) в бота.
def setup(bot):
    bot.add_cog(ButtonsRole(bot))