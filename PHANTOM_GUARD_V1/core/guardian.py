# pyright: reportMissingImports=false
import pyautogui
import os
from datetime import datetime
import time
import msvcrt
from src_phantom.config import CAPTURES_DIR, LOG_FILE

# print(CAPTURES_DIR)

console_input = []


def log_event(note_taker = None, message = None):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}: {note_taker}\n")

    if message is not None:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}: подозрительный пользователь ввел в консоль '{message}'\n")

def screenshot_loop():
    # Создаем папку для скринов, если её нет
    os.makedirs(CAPTURES_DIR, exist_ok=True)


    while True:
        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
        full_path = os.path.join(CAPTURES_DIR, filename)

        try:
            pyautogui.screenshot().save(full_path)
            log_event(f"Скриншот: {filename} сохранен!")
        except Exception as e:
            log_event("Во время сохранения скриншота произошла ошибка!")

        time.sleep(15)

def monitor_typing(target_password):
    log_event(f"Начат мониторинг ввода для пароля: {target_password}")
    verification = None
    __for_loop = 0
    while __for_loop <= 6:
        password = ""
        timings = []
        print(f"\n[ПОПЫТКА {__for_loop + 1}/6] Введите пароль: ", end='', flush=True)
        while True:
            start_time = time.perf_counter()
            char = msvcrt.getch()
            end_time = time.perf_counter()

            if char == b'\r':
                print() # Переход на новую строку
                break

            if char == b'\x08': # Если нажали Backspace
                if len(password) > 0:
                    # 1. Удаляем последнюю букву из переменной
                    password = password[:-1]

                    # 2. Удаляем букву с экрана
                    # \b - сдвигает курсор назад
                    # пробел - затирает букву
                    # \b - еще раз сдвигает курсор назад, чтобы мы были на пустом месте
                    print('\b \b', end='', flush=True)
                    if len(timings) > 0:
                        timings.pop() 
                continue

            try:
                char_decoded = char.decode('utf-8')
                print(char_decoded, end='', flush=True) # flush=True для того чтобы буквы печатались сразу а не только после enter
                password += char_decoded
            except UnicodeDecodeError:
                print("Нажата системная или некорректная клавиша")
                continue

            if len(password) > 1:
                delay = end_time - start_time
                timings.append(round(delay, 4))
        
        if password == target_password:
            is_bot = False
            for delay in timings:
                if delay <= 0.01:
                    is_bot = True
                    log_event("Хакер просто вставил пароль, начинаем поток дизинформации!")
                    break
            if is_bot == True:
                verification = False
            elif is_bot == False:
                verification = True
                print(f"Вы успешно ввели пароль!\nДобро пожаловать в систему!")
                break
        else:
            print("\nНеверный пароль!")
            __for_loop += 1
    else:
        verification = False
        log_event("Подозрительный пользователь ввел неправильно пароль 6 раз, начинаем поток дизинформации!")
        print(f"Вы успешно ввели пароль!\nДобро пожаловать в систему!")

    return verification
