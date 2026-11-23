import os
import requests
from flask import Flask, request
from google import genai



TELEGRAM_TOKEN  = os.environ.get("TELEGRAM_TOKEN", "")
GEMINI_API_KEY  = os.environ.get("GEMINI_API_KEY", "")

GEMINI_MODEL = "gemini-3.5-flash-lite"

app = Flask(__name__)

@app.route ("/", methods=["GET"])
def home():
    return "Stertup Shark Bot is running!", 200
    #tcp/ip
    #udp
    #1xx - информационные
    #100  continue - сервер поучил начала запроса и ждет осталную часть данных 
    #101 - Switch Protocols - Сервер готов сменить протокол
    #200 - OK -- Успешный результат
    #201 - Сreated  запрос выполнен , создан новый ресурс
    #202 - Accepted -- запрос принят в обработку но не зваершен
    #204 - Not Content -- запрос выполнен но тело ответа отсутствует
    #3xx -- Перенаправление 
    #302 - Found -- Временный перенос ресурса
    #4хх - Ошибки клиента
    #400 - Bad Request -- некоректный запрос
    #401 - 
    #404 - Not Found -- запрошенный ресурс не найден
    #408 - Request Timeout -- сервер не дождался полного запроса от клиента за отведенное время
    #429 - Too Many Request --  перевышен лимит запросов за единицу время
    #5xx - Ошиька сервера
    #500 - Internal Server Error -- внутренная ошибка сервера
    #502 - Bad Gateway -- шлюз получил некотектный ответ от вышестоящего сервера
    #503 - Service Unavaillable -- сервис временно недоступен (техработы, перезагрузка сервера) 


class StartupPitch: 
        def __init__(self, author, idea, score, verdict, comment ):
            self.author = author
            self.idea = idea
            self.score = score
            self.verdict = verdict
            self.comment = comment

    def format_card(self):
        return (
              f"Ствртап_Питч : {self.aurhor}\n",
              f"Идея : {self.idea}\n\n",
              f"Оценка Инвестора : {self.score}/100\n",
              f"Вердикт : {self.verdict}\n",
              f"Разброр от инвестора : {self.comment}
              
        )  
            