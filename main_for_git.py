import os
import telebot
from telebot import types

# Отримайте токен бота від BotFather та підставте його тут
bot_token = ""

bot = telebot.TeleBot(bot_token)
# bot.enable_save_next_step_handlers()


# Головне меню бота
main_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_markup.add("👨‍🎓 ВСТУПНИКАМ", )
main_menu_markup.add("🌐 САЙТ", "📰 НОВИНИ")
main_menu_markup.add("🎓 КУРСИ ПІДГОТОВКИ АБІТУРІЄНТІВ ДО ВСТУПУ У ЗАКЛАДИ ВИЩОЇ ОСВІТИ УКРАЇНИ", )
main_menu_markup.add("🙋‍♂️💬 КОНСУЛЬТАЦІЯ ФАХІВЦЯ", )


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id,
                     "👋 Вітаємо тебе у світі знань та професійного зростання! Наш університет визначається високою якістю навчання, досвідченим викладацьким складом та широким спектром спеціальностей у сфері правопорядку. Яке саме питання Вас цікавить?",
                     reply_markup=main_menu_markup)


@bot.message_handler(func=lambda message: message.text == "🙋‍♂️💬 КОНСУЛЬТАЦІЯ ФАХІВЦЯ")
def handle_website_specialist(message):
    bot.send_message(message.chat.id, """Не впевнений у чомусь або маєш питання? Натискай на <a href="https://t.me/...">КОНСУЛЬТАЦІЯ ФАХІВЦЯ</a>, 
    щоб отримати професійну допомогу та відповіді від наших кваліфікованих експертів. Вони готові допомогти тобі з будь-якими аспектами навчання чи кар'єри. 
    Твій успіх - наш пріоритет! 🚀💼""", parse_mode='HTML')





@bot.message_handler(func=lambda message: message.text == "🌐 САЙТ")
def handle_website_address(message):
    # Створення кнопки "сайт" з посиланням на URL
    url_button = types.InlineKeyboardButton("САЙТ", url="https://...")

    # Створення клавіатури з цією кнопкою
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(url_button)

    # Відправка повідомлення з клавіатурою
    bot.send_message(message.chat.id, """Щоб миттєво потрапити на офіційний веб-сайт  університету. 
    Там тебе чекає вся необхідна інформація про навчання, події та новини. Зручно, швидко, ефективно — отримай потрібні дані вже зараз! 🖱️📰""", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "📰 НОВИНИ")
def handle_news_address(message):
    # Створення кнопки "сайт" з посиланням на URL
    url_button = types.InlineKeyboardButton("НОВИНИ", url="https://...")

    # Створення клавіатури з цією кнопкою
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(url_button)

    # Відправка повідомлення з клавіатурою
    bot.send_message(message.chat.id, """
    Бажаєш бути в курсі всіх останніх подій та оновлень університетського життя? Натискай на кнопку "НОВИНИ" і 
    дізнавайся першим про важливі події, анонси, та цікаві новини. Все, що стосується нашого університету та 
    студентського середовища, знаходиться тут. Будь в тренді з університетом! 📌🗞️
    """, reply_markup=keyboard)


@bot.message_handler(
    func=lambda message: message.text == "🎓 КУРСИ ПІДГОТОВКИ АБІТУРІЄНТІВ ДО ВСТУПУ У ЗАКЛАДИ ВИЩОЇ ОСВІТИ УКРАЇНИ")
def handle_curses_address(message):
    # Створення кнопки "сайт" з посиланням на URL
    url_button = types.InlineKeyboardButton("КУРСИ ПІДГОТОВКИ АБІТУРІЄНТІВ ДО ВСТУПУ У ЗАКЛАДИ ВИЩОЇ ОСВІТИ УКРАЇНИ",
                                            url="https://...")

    # Створення клавіатури з цією кнопкою
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(url_button)

    # Відправка повідомлення з клавіатурою
    bot.send_message(message.chat.id, """
    Мрієш про вступ до університету? Натискай на кнопку "КУРСИ ПІДГОТОВКИ", щоб дізнатися про спеціалізовані курси, 
    які допоможуть тобі підготуватися до вступу у вищий навчальний заклад. Отримуй важливі поради, вивчай тести та 
    матеріали, необхідні для успішного вступу до улюбленого університету. 
    Готуй себе до майбутньої освітньої подорожі вже зараз! 🎓📚
    """, reply_markup=keyboard)


# Обробка головного меню
@bot.message_handler(func=lambda message: message.text == "👨‍🎓 ВСТУПНИКАМ")
def handle_menu(message):
    category = message.text

    if category == "👨‍🎓 ВСТУПНИКАМ":
        # markup = types.ReplyKeyboardRemove()
        markup = types.ReplyKeyboardMarkup(row_width=2)
        markup.add("📋 ПРИЙМАЛЬНА КОМІСІЯ", "📚 ПЕРЕЛІК СПЕЦІАЛЬНОСТЕЙ")
        markup.add("📞 КОНТАКТИ", "💰 ВАРТІСТЬ НАВЧАННЯ")
        markup.add("↩️ Назад")
        # Додайте обробку інших категорій та пунктів меню

        bot.send_message(message.chat.id, """Щоб дізнатися про вступні вимоги, програми навчання, терміни прийому та усі нюанси процесу вступу. 
        Ми готові надати тобі всю необхідну інформацію та підтримку на шляху до успішного навчання. Обирай майбутнє з університетом ! 🌟📚""", reply_markup=markup)

        @bot.message_handler(func=lambda message: message.text in ["📋 ПРИЙМАЛЬНА КОМІСІЯ", "📚 ПЕРЕЛІК СПЕЦІАЛЬНОСТЕЙ",
                                                                   "📞 КОНТАКТИ", "💰 ВАРТІСТЬ НАВЧАННЯ", "↩️ Назад"])
        def handle_handle_menu_form(message):

            if message.text == "↩️ Назад":
                # Знову відправляємо головне меню
                bot.send_message(message.chat.id,
                                 "Спробуйте обрати знову",
                                 reply_markup=main_menu_markup)

            if message.text == "💰 ВАРТІСТЬ НАВЧАННЯ":
                # Створення кнопки "сайт" з посиланням на URL
                url_button = types.InlineKeyboardButton("ВАРТІСТЬ НАВЧАННЯ",
                                                        url="https://...")

                # Створення клавіатури з цією кнопкою
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(url_button)

                # Відправка повідомлення з клавіатурою
                bot.send_message(message.chat.id, """
                Цікавишся вартістю навчання в ...в? Клацай на кнопку 
                "ВАРТІСТЬ НАВЧАННЯ", щоб отримати детальну інформацію про вартість навчання на різних спеціальностях. 
                Ми готові надати тобі чітку та зрозумілу інформацію про витрати та можливості фінансування. 
                Зроби перший крок до своєї освітньої мети! 💰📊
                """, reply_markup=keyboard)

            if message.text == "📞 КОНТАКТИ":
                your_html_text = """
             ...
                """

                bot.send_message(message.chat.id, your_html_text, parse_mode='HTML')

            if message.text == "📋 ПРИЙМАЛЬНА КОМІСІЯ":
                # Створення кнопки "сайт" з посиланням на URL
                url_button = types.InlineKeyboardButton("ПРИЙМАЛЬНА КОМІСІЯ",
                                                        url="https://...")

                # Створення клавіатури з цією кнопкою
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(url_button)

                # Відправка повідомлення з клавіатурою
                bot.send_message(message.chat.id, """
                Готовий зробити перший крок до свого майбутнього? Клацай на кнопку "ПРИЙМАЛЬНА КОМІСІЯ", щоб отримати 
                вичерпну інформацію про вступні вимоги, процедури та контактні дані приймальної комісії. Наші фахівці 
                готові вас вислухати та надати всю необхідну підтримку на шляху до навчання у.... Відкрий двері до свого освітнього майбутнього! 🚪🎓
                """, reply_markup=keyboard)

            if message.text == "📚 ПЕРЕЛІК СПЕЦІАЛЬНОСТЕЙ":
                markup = types.ReplyKeyboardMarkup(row_width=1)
                markup.add("🏛️ ВСТУП ЗА ДЕРЖАВНИМ ЗАМОВЛЕННЯМ", "💳 ВСТУП ЗА КОШТИ ФІЗИЧНИХ ТА/АБО ЮРИДИЧНИХ ОСІБ",
                           "📖 АСПІРАНТУРА (АД’ЮНКТУРА) ТА ДОКТОРАНТУРА", "↩️ Назад")

                bot.send_message(message.chat.id, "Оберіть:", reply_markup=markup)

                # Обробка натискання кнопок "ПЕРЕЛІК СПЕЦІАЛЬНОСТЕЙ"
                @bot.message_handler(func=lambda message: message.text in ["🏛️ ВСТУП ЗА ДЕРЖАВНИМ ЗАМОВЛЕННЯМ",
                                                                           "💳 ВСТУП ЗА КОШТИ ФІЗИЧНИХ ТА/АБО ЮРИДИЧНИХ ОСІБ",
                                                                           "📖 АСПІРАНТУРА (АД’ЮНКТУРА) ТА ДОКТОРАНТУРА",
                                                                           "↩️ Назад"])
                def handle_budget_form_subcategory(message):
                    if message.text == "↩️ Назад":
                        # Знову відправляємо головне меню
                        bot.send_message(message.chat.id,
                                         "Спробуйте обрати знову",
                                         reply_markup=main_menu_markup)

                    if message.text == "🏛️ ВСТУП ЗА ДЕРЖАВНИМ ЗАМОВЛЕННЯМ":
                        markup = types.ReplyKeyboardMarkup(row_width=2)
                        markup.add("💡 📚 БАКАЛАВРАМ", "🧙‍♂️ МАГІСТРАМ", "↩️ Назад")

                        bot.send_message(message.chat.id, "Оберіть:", reply_markup=markup)

                        @bot.message_handler(
                            func=lambda message: message.text in ["💡 📚 БАКАЛАВРАМ", "🧙‍♂️ МАГІСТРАМ", "↩️ Назад"])
                        def handle_form_kontrakt_subcategory(message):
                            if message.text == "↩️ Назад":
                                # Знову відправляємо головне меню
                                bot.send_message(message.chat.id,
                                                 "Спробуйте обрати знову",
                                                 reply_markup=main_menu_markup)

                            if message.text == "💡 📚 БАКАЛАВРАМ":
                                # Створення кнопки "сайт" з посиланням на URL
                                url_button = types.InlineKeyboardButton("БАКАЛАВРАМ",
                                                                        url="https://....")

                                # Створення клавіатури з цією кнопкою
                                keyboard = types.InlineKeyboardMarkup()
                                keyboard.add(url_button)

                                # Відправка повідомлення з клавіатурою
                                bot.send_message(message.chat.id, "Натисніть кнопку для переходу на сайт:",
                                                 reply_markup=keyboard)

                            if message.text == "🧙‍♂️ МАГІСТРАМ":
                                # Створення кнопки "сайт" з посиланням на URL
                                url_button = types.InlineKeyboardButton("МАГІСТРАМ",
                                                                        url="https://...")

                                # Створення клавіатури з цією кнопкою
                                keyboard = types.InlineKeyboardMarkup()
                                keyboard.add(url_button)

                                # Відправка повідомлення з клавіатурою
                                bot.send_message(message.chat.id, "Натисніть кнопку для переходу на сайт:",
                                                 reply_markup=keyboard)

                    if message.text == "💳 ВСТУП ЗА КОШТИ ФІЗИЧНИХ ТА/АБО ЮРИДИЧНИХ ОСІБ":
                        markup = types.ReplyKeyboardMarkup(row_width=2)
                        markup.add("💡 📚 БАКАЛАВРАМ", "🧙‍♂️ МАГІСТРАМ", "↩️ Назад")

                        bot.send_message(message.chat.id, "Оберіть:", reply_markup=markup)

                        @bot.message_handler(
                            func=lambda message: message.text in ["💡 📚 БАКАЛАВРАМ", "🧙‍♂️ МАГІСТРАМ", "↩️ Назад"])
                        def handle_form_kontrakt_subcategory(message):
                            if message.text == "↩️ Назад":
                                # Знову відправляємо головне меню
                                bot.send_message(message.chat.id,
                                                 "Спробуйте обрати знову",
                                                 reply_markup=markup)

                            if message.text == "💡 📚 БАКАЛАВРАМ":
                                # Створення кнопки "сайт" з посиланням на URL
                                url_button = types.InlineKeyboardButton("БАКАЛАВРАМ",
                                                                        url="https://...")

                                # Створення клавіатури з цією кнопкою
                                keyboard = types.InlineKeyboardMarkup()
                                keyboard.add(url_button)

                                # Відправка повідомлення з клавіатурою
                                bot.send_message(message.chat.id, "Натисніть кнопку для переходу на сайт:",
                                                 reply_markup=keyboard)

                            if message.text == "🧙‍♂️ МАГІСТРАМ":
                                # Створення кнопки "сайт" з посиланням на URL
                                url_button = types.InlineKeyboardButton("МАГІСТРАМ",
                                                                        url="https://...")

                                # Створення клавіатури з цією кнопкою
                                keyboard = types.InlineKeyboardMarkup()
                                keyboard.add(url_button)

                                # Відправка повідомлення з клавіатурою
                                bot.send_message(message.chat.id, "Натисніть кнопку для переходу на сайт:",
                                                 reply_markup=keyboard)

                    if message.text == "📖 АСПІРАНТУРА (АД’ЮНКТУРА) ТА ДОКТОРАНТУРА":
                        # Створення кнопки "сайт" з посиланням на URL
                        url_button = types.InlineKeyboardButton("АСПІРАНТУРА (АД’ЮНКТУРА) ТА ДОКТОРАНТУРА",
                                                                url="https://...")

                        # Створення клавіатури з цією кнопкою
                        keyboard = types.InlineKeyboardMarkup()
                        keyboard.add(url_button)

                        # Відправка повідомлення з клавіатурою
                        bot.send_message(message.chat.id, "Натисніть кнопку для переходу на сайт:",
                                         reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
