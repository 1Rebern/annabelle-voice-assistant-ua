import time

variable_endings = ["нуль", "одна", "дві", "три", "чотири", "п'ять", "шість", "сім", "вісім", "дев'ять", "десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", "п'ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять", "дев'ятнадцять"]
tens = ["", "", "двадцять", "тридцять", "сорок", "п'ятдесят"]

def is_one_or_teens(n):
    return n % 10 == 1 or (n % 10 == 1 and 10 < n < 20)

def number_to_text(n, context):
    if n < 20:
        base = variable_endings[n]
    else:
        base = tens[n // 10]
        if n % 10 != 0:
            base += " " + variable_endings[n % 10]

    if context == "година":
        if is_one_or_teens(n):
            return base + " година"
        elif 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
            return base + " години"
        else:
            return base + " годин"
    elif context == "хвилина":
        if is_one_or_teens(n):
            return base + " хвилина"
        elif 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
            return base + " хвилини"
        else:
            return base + " хвилин"
    elif context == "секунда":
        if is_one_or_teens(n):
            return base + " секунда"
        elif 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
            return base + " секунди"
        else:
            return base + " секунд"

def get_current_time_in_text():
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    hours_text = number_to_text(hours, "година")
    minutes_text = number_to_text(minutes, "хвилина")
    seconds_text = number_to_text(seconds, "секунда")

    return f"Зараз {hours_text} {minutes_text} {seconds_text}"

#print(get_current_time_in_text())