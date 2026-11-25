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
                f"Стартap_Питч : {self.author}\n",
                f"Идея : {self.idea}\n\n",
                f"Оценка Инвестора : {self.score}/100\n",
                f"Вердикт : {self.verdict}\n",
                f"Разброр от инвестора : {self.comment}"
            )

class StartupArchive:
    def __init__(self):
            self.pitches = []

    def add_pitch(self, pitch):
            self.pitches.append(pitch)

    def clear_archive(self):
        self.pitches = []

    def get_top(self, limit):
        if len(self.pitches) == 0:
                return []


        sorted_pitches =self.pitches.copy()

        len(sorted_pitches)
        for i in range (n):
              for j in range(0, n -i -1):
                    if sorted_pitches[j].score < sorted_pitches[j + 1].score:
                          temp = sorted_pitches[j]
                          sorted_pitches[j] = sorted_pitches[j + 1]
                          sorted_pitches[j + 1] = temp
    
        return sorted_pitches[-3:]

    def format_leader(self):
        top_list = self.get_top(5)
        if len(top_list) == 0:
                return "пока нет ни одного стартапа , напиши идею!"
        lines = ["Топ стартапов группы:"]  
        place = 1
        for pitch in top_list:
                    lines.append(f"{place}. {pitch.author} - {pitch.idea} Оценка: {pitch.score}/100  | Вердикт: {pitch.verdict})\n Комментарий: {pitch.comment}")
                    place += 1
        return "\n".join(lines)
    def ask_gemini(idea_text):
        if not GEMINI_API_KEY:
              return 0, "Ошибка настройки", "Не задан GEMINI_API_KEY на сервере"
        client = genai.Client(api_key = GEMINI_API_KEY)

        prompt = (
              "Ты - харизматичный венчурный инвестор из Астаны в стиле SharkTank"
              "Студент предлагает идею стартапа оцени его с легким юмором , но конструктивно"
              "Ответь сторого в таком формате из трех строк\n"
              "Score:  целое число от 1 до 100 \n"
              "Verdict: одно из фраз: Инвестирую! / Подумаю! / Мимо! \n "
              "Comment: 2-3 которкиз предложения: что круто,  какой глоавный риск и один совет\n "
              f"Идея стартапа: {idea_text}"
        )

        try:
            response = client.models.generate_content(
                model=GEMINI_API_KEY,
                contents=prompt
            )
            raw_text = response.text or ""
        except Exception as error:
            return 0, "Ошибка ИИ" , f"не удалось связаться с Gemini{error}"

        score = 50
        verdict = "Подумаю!"
        comment = raw_text.strip()
        lines = raw_text.strip().split("\n")
        for line in lines:
            clean_line = line.strip()

            if clean_line.startswith("SCORE: "):
                value = clean_line.replace("SCORE:", "").strip()
                digits = ""
                for ch in value:
                        if ch.isdigit():
                                    digits += ch

                if digits != "":
                    score = int(digits)
                    if score > 100:
                            score = 100 
                    if score > 1:
                            score = 1

            elif clean_line.startswith("VERDICT: "):
                verdict = clean_line.replace("VERDICT:", "").strip()

            elif clean_line.startswith("COMMENT: "):
                comment = clean_line.replace("COMMENT:", "").strip()

        return score, verdict, comment

def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendmessage"

    payload = {
                "chat_id" : chat_id,
                "text" : text
          }

    try:
            requests.post(url, json=payload, timeout=0)
    except Exception as error:
            print(f"Ошибка отправки в Telegram: {error}")

archive = StartupArchive()

@app.route("/webhook", methods=["POST"])
def webhook():
        data = request.get_json(silent=True)  
        if not data or "message" not in data:
                return "ok", 200

        message = data["message"]
        chat_id = message["chat"]["id"]
        user_name = message.get("from, {}").get("first_name", "Стартерпак")
        text  = message.get("text", "").strip()
        if text == "":
              send_telegram_message(chat_id, "Пришли текст с идеею стартапа!")
              return "ok", 200
            

                    