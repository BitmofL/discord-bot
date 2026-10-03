# Импортируем необходимые модули из библиотеки disnake.
import disnake
from disnake.ext import commands


# Определяем класс "SelectGames", который наследуется от disnake.ui.Select.
class SelectGames(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(
                label="Counter strike",
                value="839962260242694185",
                emoji="<:game_csgo:1221349512744796241>"
            ),
            disnake.SelectOption(
                label="Valorant",
                value="839978773074935879",
                emoji="<:game_valorant:1221349368637165578>"
            ),
            disnake.SelectOption(
                label="Dota 2",
                value="839962604927451156",
                emoji="<:game_dota:1221349510597316728>"
            ),
            disnake.SelectOption(
                label="League of legends",
                value="839962364786901003",
                emoji="<:game_lol:1221349508294905856>"
            ),
            disnake.SelectOption(
                label="Genshin Impact",
                value="988766970474270750",
                emoji="<:game_genshin_impact:1221349498174050304>"
            ),
            disnake.SelectOption(
                label="Honkai",
                value="840125902393311252",
                emoji="<:game_honkai:1221349366053470258>"
            ),
            disnake.SelectOption(
                label="Pubg",
                value="839962424789565520",
                emoji="<:GAMEPUBG:1221349503387308042>"
            ),
            disnake.SelectOption(
                label="Fortnite",
                value="839962882393374744",
                emoji="<:Fortnite_Logo:1221349505962606712>"
            ),
            disnake.SelectOption(
                label="Minecraft",
                value="839962471203602452",
                emoji="<:game_minecraft:1221349495686561822>"
            ),
            disnake.SelectOption(
                label="Terraria",
                value="840125146073268224",
                emoji="<:Game_Terraria:1221349493035761736>"
            ),
            disnake.SelectOption(
                label="Overwatch",
                value="840126506385801227",
                emoji="<:Game_Overwatch:1221349382746804274>"
            ),
            disnake.SelectOption(
                label="OSU!",
                value="839962641980194827",
                emoji="<:GAMEOsu:1221349501118316604>"
            ),
            disnake.SelectOption(
                label="GTA",
                value="839962681707855912",
                emoji="<:game_gtav:1221349373338845204>"
            ),
            disnake.SelectOption(
                label="Apex Legends",
                value="840125092982030358",
                emoji="<:game_ApexLegends:1221349377705115669>"
            ),
            disnake.SelectOption(
                label="Warframe",
                value="840125194516955136",
                emoji="<:Game_WarFrame:1221349489311354991>"
            ),
            disnake.SelectOption(
                label="The Finals",
                value="840126108400746497",
                emoji="<:game_finals:1221349363654201435>"
            ),
            disnake.SelectOption(
                label="Rainbow Six Siege",
                value="840126476467961896",
                emoji="<:game_Rainbow6:1221349379869249536>"
            ),
            disnake.SelectOption(
                label="Roblox",
                value="1137431925838057585",
                emoji="<:game_roblox:1221349486882721842>"
            ),
            disnake.SelectOption(
                label="Phasmophobia",
                value="1137431773702279200",
                emoji="<:game_phasmophobia:1221349375712821298>"
            ),
            disnake.SelectOption(
                label="Destiny 2",
                value="1137431704211038362",
                emoji="<:game_destiny2:1221349370633650197>"
            ),
            disnake.SelectOption(
                label="Backrooms",
                value="1137431752705573004",
                emoji="<:game_backrooms:1221353964038258780>"
            ),
            disnake.SelectOption(
                label="VR games",
                value="1137431416406286558",
            )

        ]
        super().__init__(placeholder="Укажите игру", options=options, custom_id="games", min_values=0, max_values=15)

    # Создаем метод callback для обработки взаимодействия пользователя с меню выбора ролей.
    async def callback(self, interaction: disnake.MessageInteraction):
        # Отправляем ответ, чтобы показать, что бот обрабатывает взаимодействие.
        await interaction.response.defer()

         # Задаем множество всех возможных ролей для выбора.
        all_roles = {839962260242694185, 839962604927451156, 839962364786901003, 839978773074935879, 988766970474270750,
         840125902393311252, 1137431752705573004, 839962882393374744, 839962424789565520, 839962641980194827,
         839962471203602452, 840125146073268224, 840125194516955136, 1137431925838057585, 840126506385801227,
         840126476467961896, 840125092982030358, 1137431773702279200, 839962681707855912, 1137431704211038362,
         840126108400746497, 1137431416406286558}

        # Инициализируем списки для ролей, которые нужно добавить и убрать у пользователя.
        to_remove = []
        to_add = []

        # Проверяем, выбрал ли пользователь какие-либо роли.
        if not interaction.values:
            # Если пользователь не выбрал ролей, то убираем все роли из множества all_roles.
            for role_id in all_roles:
                role = interaction.guild.get_role(role_id)
                to_remove.append(role)

            # Убираем все роли у пользователя и указываем причину.
            await interaction.author.remove_roles(*to_remove, reason="Удаление ролей")

        else:
            # Если пользователь выбрал роли, то сравниваем их с множеством all_roles.
            chosen_roles = {int(value) for value in interaction.values}

            # Определяем роли, которые нужно убрать (не выбраны пользователем).
            ids_to_remove = all_roles - chosen_roles

            for role_id in ids_to_remove:
                role = interaction.guild.get_role(role_id)
                to_remove.append(role)

            # Определяем роли, которые нужно добавить (выбраны пользователем).
            for role_id in chosen_roles:
                role = interaction.guild.get_role(role_id)
                to_add.append(role)

            # Убираем ненужные роли и добавляем выбранные роли у пользователя, указываем причину.
            await interaction.author.remove_roles(*to_remove, reason="Удаление ролей")
            await interaction.author.add_roles(*to_add, reason="Добавление ролей")


# Определяем класс "SelectRoles", который является расширением (Cog) для бота.
class SelectRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False

    # Создаем команду "games", которая будет выводить сообщение с вложенным меню выбора ролей.
    # ВНИМАНИЕ: Тут нет проверки на то, является ли пользователь администратором сервера или просто создателем.
    # Сделайте самостоятельно проверку на администратора или создателя бота.
    # Подсказка: Можно использовать декоратор @has_permissions() или if ctx.author.id == ...
    @commands.command()
    async def games(self, ctx):
        view = disnake.ui.View(timeout=None)
        view.add_item(SelectGames())
        embed = disnake.Embed(color=0x2F3136)
        embed.set_author(name="Игровые роли:")
        embed.description = "Выберите игры в которые играете и подождите " \
                            #"<:game_dota> - Dota 2\n" \
                           # "<:game_csgo> - cs 2\n" \
                           # "<:game_lol> - LoL"
        embed.set_image(url="https://i.imgur.com/QzB7q9J.png")
        await ctx.send(embed=embed, view=view)

    # Создаем слушателя события "on_ready", который добавляет персистентное меню выбора ролей.
    @commands.Cog.listener()
    async def on_ready(self):
        if self.persistent_views_added:
            return

        view = disnake.ui.View(timeout=None)
        view.add_item(SelectGames())
        # Message ID сообщения, где будет меню, добавляется после отправки команды.
        # Нужно будет скопировать ID сообщения и вставить вместо "...", после выполнения данных действий
        # необходимо перезапустить бота.
        self.bot.add_view(view, message_id=1221927612641841163)


# Функция setup, которая добавляет класс GameRoles как Cog (команду-расширение) в бота.
def setup(bot):
    bot.add_cog(SelectRoles(bot))
