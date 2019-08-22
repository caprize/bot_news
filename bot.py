import telebot
from telebot.types import Message
import requests
import json
from telebot import types

BASE_URL='https://api.telegram.org/bot825727999:AAGTZPK2TRRWZID-rxXicGpFeAbd8dbMyrk/'
TOKEN = '825727999:AAGTZPK2TRRWZID-rxXicGpFeAbd8dbMyrk'
tb = telebot.TeleBot(TOKEN)
user=tb.get_me()
import uuid
import json
import os


@tb.message_handler(commands=['start', 'help'])
def upper(message: Message):
    with open('admins.json', 'w') as f:
        r = tb.get_chat_administrators(-243828263)
        ad =[]
        for i in range (len(r)):
            ad.append(r[i].user.id)
        json.dump(ad, f)
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    h = types.InlineKeyboardButton(text="Добавить канал для администрации", callback_data="add_kanal")
    a = types.InlineKeyboardButton(text="Опубликовать объявление", callback_data="add")
    b = types.InlineKeyboardButton(text="Удалить объявление", callback_data="del")
    keyboard.add(a,b,h)
    tb.send_message(message.chat.id, "Здравствуй! Это бот для администрирования группы. Выберите что хотите сделать? ", reply_markup=keyboard)

@tb.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'add':
        kategories(call.message)
        delete_message(call.message)
    if call.data == 'add_kanal':
        tb.send_message(call.message.chat.id, 'Отправьте ID группы')
        delete_message(call.message)
        tb.register_next_step_handler(call.message, kanals)
    if call.data == 'del':
        delete(call.message)
        delete_message(call.message)
    if call.data == '1':
        new = {'kategoriya':'#Категория1','komba':'','text':'','user':'','id':'','photo':''}
        with open('news.json', 'w') as f:
            json.dump(new , f)
        with open('news.json', 'r') as f:
            new = json.load(f)
            new['user'] = call.from_user.username
        with open('news.json', 'w') as f:
            f.write(json.dumps(new))
        photo_or_next(call.message)
        delete_message(call.message)
    if call.data == '2':
        new = {'kategoriya':'#Категория2','komba':'','text':'','user':'','id':'','photo':''}
        with open('news.json', 'w') as f:
            json.dump(new , f)
        with open('news.json', 'r') as f:
            new = json.load(f)
            new['user'] = call.from_user.username
        with open('news.json', 'w') as f:
            f.write(json.dumps(new))
        photo_or_next(call.message)
        delete_message( call.message)
    if call.data == '3':
        new = {'kategoriya':'#Категория3','komba':'','text':'','user':'','id':'','photo':''}
        with open('news.json', 'w') as f:
            json.dump(new , f)
        with open('news.json', 'r') as f:
            new = json.load(f)
            new['user'] = call.from_user.username
        with open('news.json', 'w') as f:
            f.write(json.dumps(new))
        photo_or_next(call.message)
        delete_message(call.message)
    if call.data == '4':
        new = {'kategoriya':'#Категория4','komba':'','text':'','user':'','id':'','photo':''}
        with open('news.json', 'w') as f:
            json.dump(new , f)
        with open('news.json', 'r') as f:
            new = json.load(f)
            new['user'] = call.from_user.username
        with open('news.json', 'w') as f:
            f.write(json.dumps(new))
        photo_or_next(call.message)
        delete_message(call.message)
    if call.data == '5':
        new = {'kategoriya':'#Категория5','komba':'','text':'','user':'','id':'','photo':''}
        with open('news.json', 'w') as f:
            json.dump(new , f)
        with open('news.json', 'r') as f:
            new = json.load(f)
            new['user'] = call.from_user.username
        with open('news.json', 'w') as f:
            f.write(json.dumps(new))
        photo_or_next(call.message)
        delete_message(call.message)
    if call.data == 'photo':
        with open('news.json', 'r') as f:
            new = json.load(f)
            new['photo'] = '1'
        with open('news.json', 'w') as f:
            f.write(json.dumps(new))
        tb.send_message(call.message.chat.id, 'Отправьте фотографию')
        tb.register_next_step_handler(call.message, add_photo)
        delete_message(call.message)
    if call.data == 'next':
        with open('news.json', 'r') as f:
            new = json.load(f)
            new['photo'] = '0'
        with open('news.json', 'w') as f:
            f.write(json.dumps(new))
        tb.send_message(call.message.chat.id, "Отправьте число  (Только цифры и символы))")
        tb.register_next_step_handler(call.message, add_number)
        delete_message(call.message)
    if call.data == 'back':
        with open('news.json', 'r') as jfr:
            new = json.load(jfr)
            g = new['photo']
        with open('id.json', 'r') as jft:
            file1 = json.load(jft)
            b = file1[0]['sms'][-1]['code']
        if g == '1':
            src = '/home/iskander/mafia/photos/' + str(b) + '.jpg'
            os.remove(src)
        with open('id.json', 'r') as jf:
            file = json.load(jf)
        with open('id.json', 'w') as f:
            del file[0]['sms'][-1]
            json.dump(file, f, indent=4)
        kategories(call.message)
        delete_message(call.message)
    if call.data == 'publicate':
        public(call.message)
        delete_message(call.message)
def kanals(message):
    try:
        a = int(message.text)
        with open('kanal.json', 'w') as f:
            f.write(json.dumps(a))
        upper(message)
    except Exception:
        tb.send_message(message.chat.id, text='Введите ID корректно')
        tb.register_next_step_handler(message, kanals)

def kategories(message):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    a = types.InlineKeyboardButton(text="Категория 1", callback_data="1")
    b = types.InlineKeyboardButton(text="Категория 2", callback_data="2")
    c = types.InlineKeyboardButton(text="Категория 3", callback_data="3")
    d = types.InlineKeyboardButton(text="Категория 4", callback_data="4")
    e = types.InlineKeyboardButton(text="Категория 5", callback_data="5")

    keyboard.add(a,b,c,d,e,)
    tb.send_message(message.chat.id, 'Выберите категорию',reply_markup=keyboard)
    # tb.register_next_step_handler(message, get_id)
    # group_list.append('f')
    # print(group_list)
# def get_id(message: Message):
#     group_list.append(message.text)
#     print(group_list)
def photo_or_next(message):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    a = types.InlineKeyboardButton(text="Прикрепить фото", callback_data="photo")
    b = types.InlineKeyboardButton(text="Пропустить этот шаг", callback_data="next")
    keyboard.add(a, b )
    tb.send_message(message.chat.id, 'Хотите объявление с фотографией? ', reply_markup=keyboard)

def add_photo(message):
    ff = uuid.uuid4()
    id = str(ff)
    with open('news.json', 'r') as f:
        new = json.load(f)
        new['id'] = id
    with open('news.json', 'w') as f:
        f.write(json.dumps(new))
    a = str(id)+'.jpg'
    if message.content_type=='photo':
        file_info = tb.get_file(message.photo[0].file_id)
        downloaded_file = tb.download_file(file_info.file_path)

        src = '/home/iskander/mafia/photos/' + a
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        tb.reply_to(message, "Пожалуй, я сохраню это")
        tb.send_message(message.chat.id, "Отправьте число (Только цифры и символы))")
        tb.register_next_step_handler(message, add_number)
    else:
        tb.send_message(message.chat.id, 'Извините, это не фотография( Попробуйте отправить ещё раз')
        tb.register_next_step_handler(message, add_photo)
    return id

def add_number(message):
    ff = uuid.uuid4()
    id = str(ff)
    with open('news.json', 'r') as f:
        new = json.load(f)
        if new['id'] == '':
            new['id'] = id
    with open('news.json', 'w') as f:
        f.write(json.dumps(new))
    with open('news.json', 'r') as f:
        new = json.load(f)
        a = new['user']
        new['user'] = '@'+new['user']
    with open('news.json', 'w') as f:
        f.write(json.dumps(new))
    try:
        number = str(message.text)
        with open('news.json', 'r') as f:
            new = json.load(f)
            new['komba'] = number
        with open('news.json', 'w') as f:
            f.write(json.dumps(new))
        tb.send_message(message.chat.id, text='Введите текст объявления')
        tb.register_next_step_handler(message, add_text)
        return number
    except Exception:
        tb.send_message(message.chat.id, text='Введите число корректно')
        tb.register_next_step_handler(message, add_number)
def add_text(message):
    text=message.text
    with open('news.json', 'r') as f:
        new = json.load(f)
        new['text'] = text
    with open('news.json', 'w') as f:
        f.write(json.dumps(new))
    ending(message)

def ending(message):
    with open('news.json', 'r') as jfr:
        new = json.load(jfr)
        a = new['id']
        b = new['photo']
    with open('id.json', 'r') as jf:
        file = json.load(jf)
    with open('number.json', 'r') as fgr:
        num = int(json.load(fgr))
        if num >=1000:
            num = 1
        num+=1
    with open('id.json', 'w') as f:
        target = file[0]['sms']
        user_info = {'id': '','code':a,'number':num}
        target.append(user_info)
        json.dump(file, f, indent=4)
    with open('number.json', 'w') as fer:
        json.dump(num,fer)
    dop= '[Нажмите сюда,](https://t.me/Mytoserbot) '
    smska = new['kategoriya'] + '\n'
    smska += str(new['komba'])  + '\n'
    smska += new['text'] + '\n'
    smska += 'ID обьявления :' + str(num) + '\n'
    smska += 'Сообщение от пользователя ' + new['user']  + '\n'
    smska += dop + "чтобы дать объявление "
    if b =='1':
        tb.send_photo(message.chat.id, open( '/home/iskander/mafia/photos/' + a + '.jpg', 'rb'),smska, parse_mode='markdown')
    else:
        tb.send_message(message.chat.id, smska,parse_mode='markdown')


    keyboard = types.InlineKeyboardMarkup(row_width=3)
    a = types.InlineKeyboardButton(text="Опубликовать", callback_data="publicate")
    b = types.InlineKeyboardButton(text="Написать заново", callback_data="back")
    keyboard.add(a, b)
    tb.send_message(message.chat.id, 'Хотите опубликовать новость? ', reply_markup=keyboard)

def public(message):
    with open('news.json', 'r') as jfr:
        new = json.load(jfr)
        a = new['id']
        b = new['photo']
    with open('kanal.json', 'r') as f:
        chat_id = json.load(f)
    with open('id.json', 'r') as jf:
        file = json.load(jf)
    with open('number.json', 'r') as fgr:
        num = int(json.load(fgr))
    dop = '[Нажмите сюда,](https://t.me/Mytoserbot) ' #Рандомный текст
    smska = new['kategoriya'] + '\n'
    smska += str(new['komba']) + '\n'
    smska += new['text'] + '\n'
    smska += 'ID Новости ' + str(num) + '\n'
    smska += 'Сообщение от пользователя: ' + new['user']  + '\n'
    smska += dop + "чтобы дать объявление "
    succes = 'Новость успешно опубликована!' + '\n'
    succes += 'Пожалуйста сохраните данный код, чтобы в будущем удалить данное обьявление:' + '\n'
    succes += a + '\n'
    try:
        if b == '1':
            sph = tb.send_photo(chat_id, open('/home/iskander/mafia/photos/' + a + '.jpg', 'rb'), smska,parse_mode='markdown')
            with open('id.json', 'r') as jf:
                file = json.load(jf)
            with open('id.json', 'w') as f:
                file[0]['sms'][-1]['id']=sph.message_id
                json.dump(file, f, indent=4)
            with open('admins.json', 'r') as fj:
                admin = json.load(fj)
        else:
            st = tb.send_message(chat_id, smska,parse_mode='markdown')
            with open('id.json', 'r') as jf:
                file = json.load(jf)
            with open('id.json', 'w') as f:
                file[0]['sms'][-1]['id']=st.message_id
                json.dump(file, f, indent=4)
            with open('admins.json', 'r') as fj:
                admin = json.load(fj)
        tb.send_message(message.chat.id, succes)
        upper(message)
    except Exception:
        tb.send_message(message.chat.id, 'Что-то пошло не так ;( Попробуйте ещё раз')
        upper(message)

def delete(message):
    with open('admins.json', 'r') as fj:
        admin = json.load(fj)

    if message.chat.id in admin:
        tb.send_message(message.chat.id, 'Введите id обьявления, которое хотите удалить')
        tb.register_next_step_handler(message, delete_message2)
    else:
        tb.send_message(message.chat.id, 'Введите секретный код обьявления, которое хотите удалить')
        tb.register_next_step_handler(message, delete_message3)

def delete_message(message):

    return tb.delete_message(message.chat.id, message.message_id)
def delete_message2(message):
    with open('kanal.json', 'r') as f:
        chat_id = json.load(f)
    with open('id.json', 'r') as jf:
        file = json.load(jf)
        a = file[0]['sms'][-1]['number']
        b = file[0]['sms'][-1]['code']
        v = file[0]['sms'][-1]['id']
    v = str(v)
    smska =  '🆔 :' + str(a) + '  ❎ Объявление удалено'
    sms ='🆔 :' + str(a) + '  ❎ Объявление успешно удалено'
    with open('news.json', 'r') as jfr:
        new = json.load(jfr)
        g = new['photo']
    try:
        if str(message.text) == str(a) and g=='1':
            src = '/home/iskander/mafia/photos/' + str(b) + '.jpg'
            os.remove(src)
            with open('id.json', 'r') as jf:
                file = json.load(jf)
            with open('id.json', 'w') as f:
                del file[0]['sms'][-1]
                json.dump(file, f, indent=4)
            tb.send_message(message.chat.id, sms)
            upper(message)

            tb.send_message(chat_id, smska)
            return tb.delete_message(chat_id, int(v))
        elif str(message.text) == str(a) and g == '0':
            with open('id.json', 'r') as jf:
                file = json.load(jf)
            with open('id.json', 'w') as f:
                del file[0]['sms'][-1]
                json.dump(file, f, indent=4)
            tb.send_message(message.chat.id, sms)
            upper(message)

            tb.send_message(chat_id, smska)
            return tb.delete_message(chat_id, int(v))
    except Exception:
        tb.send_message(message.chat.id, 'К сожалению это неверный ID(')
        delete(message)

def delete_message3(message):

    with open('kanal.json', 'r') as f:
        chat_id = json.load(f)
    with open('id.json', 'r') as jf:
        file = json.load(jf)
        a = file[0]['sms'][-1]['code']
        b = file[0]['sms'][-1]['id']
        h = file[0]['sms'][-1]['number']
    b = str(b)
    with open('news.json', 'r') as jfr:
        new = json.load(jfr)
        g = new['photo']
    smska = '🆔 : ' + str(h) + '  ❎ Объявление удалено'
    sms = '🆔 : ' + str(h) + '  ❎ Объявление успешно удалено'
    try:
        if str(message.text) == str(a) and g == '1' :
            src = '/home/iskander/mafia/photos/' + str(a) + '.jpg'
            os.remove(src)
            with open('id.json', 'r') as jf:
                file = json.load(jf)
            with open('id.json', 'w') as f:
                del file[0]['sms'][-1]
                json.dump(file, f, indent=4)
            tb.send_message(message.chat.id, sms)
            upper(message)

            tb.send_message(chat_id, smska)
            return tb.delete_message(chat_id, int(b))
        elif str(message.text) == str(a) and g == '0':
            with open('id.json', 'r') as jf:
                file = json.load(jf)
            with open('id.json', 'w') as f:
                del file[0]['sms'][-1]
                json.dump(file, f, indent=4)
            tb.send_message(message.chat.id, sms)
            upper(message)

            tb.send_message(chat_id, smska)
            return tb.delete_message(chat_id, int(b))
    except Exception:
        tb.send_message(message.chat.id, 'К сожалению это неверный код(')
        delete(message)
# @tb.message_handler(func=lambda message:True)
# def get_id(message: Message):
# 	tb.send_message(message.chat.id,message.chat.id)
# 	print(message.chat.id)
tb.polling(True)
