# import asyncio
# import logging
# import sys
# import random  # Savollarni aralashtirish uchun kerak bo'ladi
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.filters import Command
# from aiogram.types import BotCommand
#
# # TOKEN
# TOKEN = "8422699263:AAG9MDvHxqz23D8bhg8FpPNhePzYdu9vx9Y"
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# # MA'LUMOTLARNI SAQLASH (Dastur yopilsa o'chib ketadi)
# user_data = {}  # {user_id: {'step': 0, 'score': 0}}
# all_users = set()  # Obunachilar soni uchun
#
# questions = [
#     # --- HTML (1-20) ---
#     {"q": "HTML-da 'Hyperlink' yaratish uchun qaysi teg ishlatiladi?", "options": ["<link>", "<a>", "<href>"],
#      "correct": 1},
#     {"q": "Qaysi teg matnni qalin (bold) qiladi?", "options": ["<style>", "<b>", "<i>"], "correct": 1},
#     {"q": "Tartiblangan ro'yxat qaysi teg bilan boshlanadi?", "options": ["<ul>", "<li>", "<ol>"], "correct": 2},
#     {"q": "Rasmni sahifaga qo'shish uchun qaysi atribut majburiy?", "options": ["src", "alt", "href"], "correct": 0},
#     {"q": "HTML5-da video qo'shish uchun qaysi teg ishlatiladi?", "options": ["<media>", "<video>", "<source>"],
#      "correct": 1},
#     {"q": "Formada foydalanuvchi ma'lumot kiritishi uchun qaysi teg kerak?",
#      "options": ["<input>", "<label>", "<form>"], "correct": 0},
#     {"q": "Sahifa sarlavhasi (tabda) qaysi teg ichida yoziladi?", "options": ["<body>", "<head>", "<title>"],
#      "correct": 2},
#     {"q": "HTML-da eng kichik sarlavha darajasi qaysi?", "options": ["<h1>", "<h6>", "<h3>"], "correct": 1},
#     {"q": "Yangi qatorga o'tish tegi qaysi?", "options": ["<break>", "<lb>", "<br>"], "correct": 2},
#     {"q": "Jadvalda qator yaratish tegi qaysi?", "options": ["<td>", "<tr>", "<th>"], "correct": 1},
#     {"q": "HTML-da 'id' va 'class' farqi nimada?",
#      "options": ["Farqi yo'q", "ID faqat bitta, Class ko'p elementga", "Class faqat bitta bo'ladi"], "correct": 1},
#     {"q": "Sayt ikonkasi (favicon) qayerda ko'rsatiladi?", "options": ["Body ichida", "Brauzer tabida", "Faqat pastda"],
#      "correct": 1},
#     {"q": "Meta charset='UTF-8' nima uchun kerak?",
#      "options": ["Rang uchun", "Simvollarni to'g'ri ko'rsatish uchun", "Tezlik uchun"], "correct": 1},
#     {"q": "HTML-da tugma yaratish tegi?", "options": ["<button>", "<input type='btn'>", "<press>"], "correct": 0},
#     {"q": "Qaysi teg matnni kursiv (italic) qiladi?", "options": ["<em>", "<i>", "Ikkalasi ham"], "correct": 2},
#     {"q": "HTML5-ning yangi semantic tegi qaysi?", "options": ["<div>", "<section>", "<span>"], "correct": 1},
#     {"q": "Qaysi atribut inputni to'ldirish majburiy ekanini bildiradi?", "options": ["important", "required", "must"],
#      "correct": 1},
#     {"q": "Radio button nima uchun ishlatiladi?",
#      "options": ["Ko'p javobdan birini tanlash", "Matn kiritish", "Fayl yuklash"], "correct": 0},
#     {"q": "HTML-da eng katta sarlavha tegi?", "options": ["<hmax>", "<h1>", "<h6>"], "correct": 1},
#     {"q": "Kodlarni sahifada ko'rsatish uchun qaysi teg ishlatiladi?", "options": ["<code>", "<script>", "<pre>"],
#      "correct": 0},
#
#     # --- CSS (21-40) ---
#     {"q": "CSS nima degani?", "options": ["Creative Style Sheets", "Cascading Style Sheets", "Computer Style Sheets"],
#      "correct": 1},
#     {"q": "Elementning ichki masofasini qaysi xususiyat boshqaradi?", "options": ["margin", "border", "padding"],
#      "correct": 2},
#     {"q": "ID selektori qaysi belgi bilan yoziladi?", "options": [".", "#", "*"], "correct": 1},
#     {"q": "Matn rangini o'zgartirish uchun qaysi xususiyat ishlatiladi?",
#      "options": ["text-color", "font-style", "color"], "correct": 2},
#     {"q": "Flexbox-da asosiy o'q bo'ylab tekislash?", "options": ["align-items", "justify-content", "flex-direction"],
#      "correct": 1},
#     {"q": "Elementning tashqi masofasini qaysi xususiyat boshqaradi?", "options": ["padding", "margin", "spacing"],
#      "correct": 1},
#     {"q": "Z-index nima vazifani bajaradi?", "options": ["Kenglik", "Qatlamlar tartibi", "Shaffoflik"], "correct": 1},
#     {"q": "CSS-da rangni shaffof qilish formati?", "options": ["HEX", "RGB", "RGBA"], "correct": 2},
#     {"q": "Position: sticky nima qiladi?",
#      "options": ["Elementni yopishtiradi", "Elementni yashiradi", "Doim o'rtada saqlaydi"], "correct": 0},
#     {"q": "Matnni o'rtaga keltirish xususiyati?", "options": ["align: center", "text-align: center", "font-center"],
#      "correct": 1},
#     {"q": "CSS grid-da qatorlar orasidagi masofa?", "options": ["gap", "margin", "padding"], "correct": 0},
#     {"q": "Media query nima uchun kerak?", "options": ["Rang uchun", "Responsive dizayn uchun", "Rasm uchun"],
#      "correct": 1},
#     {"q": "Elementni butunlay yashirish (joyini ham olmaydi)?",
#      "options": ["visibility: hidden", "display: none", "opacity: 0"], "correct": 1},
#     {"q": "Font-family nima?", "options": ["Shrift o'lchami", "Shrift turi", "Shrift rangi"], "correct": 1},
#     {"q": "Border-radius: 50% nima qiladi?", "options": ["Kvadrat qiladi", "Doira qiladi", "Uchburchak qiladi"],
#      "correct": 1},
#     {"q": "Hover nima?",
#      "options": ["Sichqoncha ustiga kelgandagi holat", "Tugma bosilgandagi holat", "Sahifa yuklangandagi holat"],
#      "correct": 0},
#     {"q": "Background-repeat: no-repeat nima qiladi?",
#      "options": ["Fonni takrorlamaydi", "Fonni kattalashtiradi", "Fonni o'chiradi"], "correct": 0},
#     {"q": "CSS-da !important nima?", "options": ["Xatolik", "Eng yuqori ustunlik beradi", "Kod yozishni to'xtatadi"],
#      "correct": 1},
#     {"q": "vh va vw nima?", "options": ["Vaqt birligi", "Ekran o'lchamiga nisbatan birliklar", "Rang kodi"],
#      "correct": 1},
#     {"q": "CSS-da o'zgaruvchi qanday boshlanadi?", "options": ["$", "@", "--"], "correct": 2},
#
#     # --- JAVASCRIPT (41-65) ---
#     {"q": "JS-da o'zgarmas qiymat qanday e'lon qilinadi?", "options": ["let", "var", "const"], "correct": 2},
#     {"q": "Brauzerda ogohlantirish oynasini chiqarish?", "options": ["alert()", "msg()", "console.log()"],
#      "correct": 0},
#     {"q": "JS qayerda ishlaydi?", "options": ["Server", "Brauzer", "Ikkalasida ham"], "correct": 2},
#     {"q": "Massivga yangi element qo'shish metodi?", "options": ["pop()", "push()", "shift()"], "correct": 1},
#     {"q": "Qiymat va turni baravar tekshirish?", "options": ["==", "=", "==="], "correct": 2},
#     {"q": "Async/Await nima uchun?", "options": ["Asinxron kodni boshqarish", "Dizayn", "Loop"], "correct": 0},
#     {"q": "JavaScript-da 'undefined' nima?",
#      "options": ["Qiymat berilmagan o'zgaruvchi", "Xatolik", "Null bilan bir xil"], "correct": 0},
#     {"q": "DOM elementini ID orqali olish?", "options": ["getElementByClass", "getElementById", "queryID"],
#      "correct": 1},
#     {"q": "Array length nima beradi?",
#      "options": ["Massiv elementlari sonini", "Massiv birinchi elementini", "Xatolikni"], "correct": 0},
#     {"q": "Sichqoncha bosilgandagi event?", "options": ["onchange", "onclick", "onhover"], "correct": 1},
#     {"q": "JavaScript kutubxonasi qaysi?", "options": ["Django", "React", "Laravel"], "correct": 1},
#     {"q": "Template literal qanday belgilanadi?", "options": ["' '", '" "', "` `"], "correct": 2},
#     {"q": "SetTimeout nima qiladi?",
#      "options": ["Kodni ma'lum vaqtdan keyin yurgizadi", "Kodni to'xtatadi", "Loopni boshlaydi"], "correct": 0},
#     {"q": "Arrow function qanday yoziladi?", "options": ["function()", "() => {}", "=> func"], "correct": 1},
#     {"q": "Object-dan kalitlarni olish metodi?", "options": ["Object.keys()", "Object.values()", "Object.get()"],
#      "correct": 0},
#     {"q": "Typeof [] natijasi nima?", "options": ["array", "object", "null"], "correct": 1},
#     {"q": "Map() metodi nima qaytaradi?", "options": ["Yangi massiv", "Bitta qiymat", "Hech narsa"], "correct": 0},
#     {"q": "Strict mode nima?", "options": ["Xavfsiz va qat'iy kod yozish rejimi", "O'yin rejimi", "Tezkor rejim"],
#      "correct": 0},
#     {"q": "Promises-da xatoni tutish uchun qaysi metod ishlatiladi?", "options": ["then()", "catch()", "finally()"],
#      "correct": 1},
#     {"q": "JSON nima?", "options": ["JavaScript Object Notation", "Java Serial Object", "Just Simple Object"],
#      "correct": 0},
#     {"q": "Spread operator qanday yoziladi?", "options": ["...", "---", "***"], "correct": 0},
#     {"q": "NaN nima?", "options": ["Not a Number", "Now and Next", "New and Null"], "correct": 0},
#     {"q": "Math.random() nima qaytaradi?", "options": ["0 va 1 oralig'ida son", "1 va 10 oralig'ida", "Butun son"],
#      "correct": 0},
#     {"q": "Event delegation nima?",
#      "options": ["Parent orqali child eventlarini ushlash", "Eventni o'chirish", "Delegat tayinlash"], "correct": 0},
#     {"q": "JS-da 'this' nimaga ishora qiladi?",
#      "options": ["Global obyektga", "Kontekstga", "Ikkalasi ham vaziyatga qarab"], "correct": 2},
#
#     # --- VUE.JS (66-85) ---
#     {"q": "Vue-da ikki tomonlama bog'lash (two-way binding)?", "options": ["v-bind", "v-model", "v-on"], "correct": 1},
#     {"q": "Vue-da 'props' nima uchun?", "options": ["Parentdan childga ma'lumot uzatish", "Dizayn", "Loop"],
#      "correct": 0},
#     {"q": "Vue 3-da asosiy API turi?", "options": ["Options API", "Composition API", "Ikkalasi ham"], "correct": 2},
#     {"q": "Vue-da elementni shartli render qilish?", "options": ["v-show", "v-if", "Ikkalasi ham"], "correct": 2},
#     {"q": "Vue-da reactive o'zgaruvchi yaratish (Composition API)?", "options": ["ref()", "reactive()", "Ikkalasi ham"],
#      "correct": 2},
#     {"q": "Vue-da computed o'zgaruvchi nima bilan farq qiladi?", "options": ["Keshlanadi", "Tezroq", "Xotira olmaydi"],
#      "correct": 0},
#     {"q": "Vue Router nima uchun?", "options": ["Sahifalararo o'tish", "Baza", "Stil"], "correct": 0},
#     {"q": "Pinia nima?", "options": ["State management", "CSS framework", "Router"], "correct": 0},
#     {"q": "Vue-da life cycle hook qaysi?", "options": ["onMounted", "onStarted", "onFinished"], "correct": 0},
#     {"q": "Vue-da 'v-on' o'rniga qisqartma?", "options": [":", "@", "#"], "correct": 1},
#     {"q": "Vue-da 'v-bind' o'rniga qisqartma?", "options": [":", "@", "#"], "correct": 0},
#     {"q": "Vue-da 'slot' nima?", "options": ["Komponent ichiga kontent joylash joyi", "Xotira", "Funksiya"],
#      "correct": 0},
#     {"q": "Vue-da 'watchEffect' nima?", "options": ["Avtomatik kuzatuvchi funksiya", "Dizayn effekti", "Loop"],
#      "correct": 0},
#     {"q": "Vue-da 'teleport' nima?",
#      "options": ["Elementni boshqa joyga ko'chirish", "Sahifani yangilash", "API chaqiruv"], "correct": 0},
#     {"q": "Vue 3-da 'setup' funksiyasi qayerda?", "options": ["Script ichida", "Template ichida", "Style ichida"],
#      "correct": 0},
#     {"q": "Vue-da 'provide/inject' nima uchun?",
#      "options": ["Chuqur komponentlarga ma'lumot uzatish", "Rasmlar uchun", "Xavfsizlik"], "correct": 0},
#     {"q": "Vue-da 'key' atributi nima uchun v-for-da kerak?",
#      "options": ["Elementlarni tanib olish (re-render optimallash)", "Rang uchun", "ID berish uchun"], "correct": 0},
#     {"q": "Vue DevTools nima?", "options": ["Brauzer kengaytmasi (debug uchun)", "Dasturlash tili", "Hosting"],
#      "correct": 0},
#     {"q": "Vue-da 'transition' tegi nima qiladi?",
#      "options": ["Kirish/chiqish animatsiyalari", "Sahifani boshqasiga o'tkazadi", "HTTP so'rov"], "correct": 0},
#     {"q": "Vite nima?", "options": ["Tezkor loyiha yig'uvchi (build tool)", "CSS framework", "Baza"], "correct": 0},
#
#     # --- NUXT.JS (86-100) ---
#     {"q": "Nuxt.js asosi nima?", "options": ["React", "Vue.js", "Angular"], "correct": 1},
#     {"q": "Nuxt-da avtomatik routing qaysi papkada?", "options": ["assets", "pages", "components"], "correct": 1},
#     {"q": "SSR nima?", "options": ["Server Side Rendering", "Static Site", "Client Side"], "correct": 0},
#     {"q": "Nuxt-da SEO uchun head qismini boshqarish?", "options": ["useHead", "useMeta", "useSEO"], "correct": 0},
#     {"q": "Nuxt 3 da server API-lar qayerda?", "options": ["api/", "server/api", "backend/"], "correct": 1},
#     {"q": "Nuxt-da 'useFetch' va 'useAsyncData' farqi?",
#      "options": ["Farqi yo'q", "useFetch - qisqartma, useAsyncData - kengaytirilgan", "useFetch faqat CSS uchun"],
#      "correct": 1},
#     {"q": "Nuxt-da layoutlar qaysi papkada?", "options": ["layouts/", "styles/", "views/"], "correct": 0},
#     {"q": "Nuxt-da 'middleware' nima uchun?", "options": ["Sahifaga kirishdan oldin tekshiruvlar", "Rasmlar", "Baza"],
#      "correct": 0},
#     {"q": "Nuxt static site generation (SSG) uchun buyruq?", "options": ["nuxt build", "nuxt generate", "nuxt start"],
#      "correct": 1},
#     {"q": "Nuxt-da komponentlar qanday yuklanadi?",
#      "options": ["Import qilish shart emas (Auto-import)", "Har doim import qilish kerak", "Faqat Nuxt configda"],
#      "correct": 0},
#     {"q": "Nuxt 3 da composables papkasi nima uchun?",
#      "options": ["Reactive funksiyalarni global qilish", "Stillar uchun", "Rasmlar uchun"], "correct": 0},
#     {"q": "Nuxt-da 'Nitro' nima?", "options": ["Server dvigateli", "Animatsiya kutubxonasi", "Dizayn"], "correct": 0},
#     {"q": "Nuxt-da 'public' papkasi nima uchun?", "options": ["Statik fayllar uchun", "Kod uchun", "Modullar uchun"],
#      "correct": 0},
#     {"q": "Nuxt-da 'plugins' papkasi qachon ishga tushadi?",
#      "options": ["Vue app yaratilganda", "Sahifa yopilganda", "Faqat serverda"], "correct": 0},
#     {"q": "Nuxt 3 TypeScript-ni qo'llab-quvvatlaydimi?", "options": ["Ha, to'liq", "Yo'q", "Faqat pullik versiyada"],
#      "correct": 0}
# ]
#
#
# async def set_main_menu(bot: Bot):
#     main_menu_commands = [
#         BotCommand(command='/start', description='Botni yangilash'),
#         BotCommand(command='/quiz', description='Quizni boshlash'),
#         BotCommand(command='/stat', description='Statistika'),
#         BotCommand(command='/help', description='Yordam')
#     ]
#     await bot.set_my_commands(main_menu_commands)
#
#
# async def send_next_question(user_id: int):
#     data = user_data.get(user_id)
#     if not data:
#         return
#
#     step = data['step']
#
#     if step < len(questions):
#         item = questions[step]
#         await bot.send_poll(
#             chat_id=user_id,
#             question=f"{step + 1}/{len(questions)}: {item['q']}",
#             options=item['options'],
#             type='quiz',
#             correct_option_id=item['correct'],
#             is_anonymous=False
#         )
#     else:
#         score = data['score']
#         total = len(questions)
#         await bot.send_message(
#             user_id,
#             f"O'yin tugadi! 🎉\n\nNatijangiz: {total} tadan {score} ta to'g'ri javob berdingiz.\n\nQayta boshlash uchun /quiz buyrug'ini yozing."
#         )
#         user_data[user_id] = {'step': 0, 'score': 0}
#
#
# @dp.message(Command("start"))
# async def start_handler(message: types.Message):
#     all_users.add(message.from_user.id)  # Obunachini saqlash
#     await message.answer(
#         "Frontend Quiz botiga xush kelibsiz! 🚀\nMenuda 'Quizni boshlash' tugmasini bosing yoki /quiz deb yozing.")
#
#
# @dp.message(Command("stat"))
# async def stat_handler(message: types.Message):
#     count = len(all_users)
#     await message.answer(f"📊 Botingizdan foydalanuvchilar soni: {count} ta")
#
#
# @dp.message(Command("quiz"))
# async def quiz_handler(message: types.Message):
#     # Har safar yangi quiz boshlaganda ma'lumotlarni nolga tushirish
#     user_data[message.from_user.id] = {'step': 0, 'score': 0}
#     await send_next_question(message.from_user.id)
#
#
# @dp.poll_answer()
# async def handle_poll_answer(poll_answer: types.PollAnswer):
#     user_id = poll_answer.user.id
#     if user_id not in user_data:
#         return
#
#     data = user_data[user_id]
#     current_step = data['step']
#
#     # Ballni tekshirish
#     if poll_answer.option_ids[0] == questions[current_step]['correct']:
#         data['score'] += 1
#
#     # Qadamni oshirish
#     data['step'] += 1
#
#     await asyncio.sleep(0.5)
#     await send_next_question(user_id)
#
#
# @dp.message(Command("help"))
# async def help_handler(message: types.Message):
#     await message.answer(
#         "Ushbu bot orqali Frontend bilimingizni 100 ta savol orqali sinab ko'rishingiz mumkin.\n\nBuyruqlar:\n/quiz - Testni boshlash\n/stat - Foydalanuvchilar soni")
#
#
# async def main():
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     await set_main_menu(bot)
#     print("Bot ishga tushdi...")
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     try:
#         asyncio.run(main())
#     except (KeyboardInterrupt, SystemExit):
#         print("Bot to'xtatildi")