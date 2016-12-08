import datetime
import vk
import weather
import time

#Лазченко Влад. ВИС 22. Лабораторная работа #3 "Разработка и внедрение VK-бота"
session = 

vk.Session('9197d4d5223bd3ec10fa9ba8f5593431d7dc42bca8b3a233972ef72f9204d8d13b5bef9cbbabea4c46019')

api = vk.API(session)

while (True):
    try:
       
messages = api.messages.get()
    except:
        continue
   
for m in messages[1:]:
        
        if m['read_state'] == 0:

           
uid = m['uid']

           
            user_name = 

api.users.get(user_ids=uid)[0]['first_name']
            try:
                
                chat_id = m['chat_id']
            except:
                chat_id = 0
            if chat_id > 0:
                uid = 0

            text = m['body']
            text = text.lower()
            text = text.replace(' ', '')

            
            date_time = 

datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

            if text == 'info':
                api.messages.send(uid=uid, chat_id=chat_id, 

message=date_time +
                                                                  

  '\n\n Information:'
                                                                  

  '\n>VKBot v.0.01, build on November 02 2016 '
                                                                  

  '\n>Developer: Lazchenko Vlad')

            if text == 'commands':
                list_city = 'Список поддерживаемых городов: 

Ростов-на-Дону, Каменск, Миллерово, Таганрог, Азов '
                api.messages.send(uid=uid, chat_id=chat_id, 

message=date_time + '\n\nCommands:\n1. info\n2. commands'
                                                                  

              '\n3. Привет'
                                                                  

              '\n4. Погода в [название города]\n' +
                                                                  

  list_city)
          
            if text == 'Привет':
                api.messages.send(uid=uid, chat_id=chat_id, 

message=date_time + '\n\nЗдравствуй, ' + user_name +
                                                                  

      '!?')
            
            if text[0:7:1] == "Погода":
                api.messages.send(uid=uid, chat_id=chat_id, 

message=str(date_time + '\n\n' +
                                                                  

      weather.weather_now(text)))
            
            api.messages.markAsRead(message_ids=m['mid'])
  
    time.sleep(3)
