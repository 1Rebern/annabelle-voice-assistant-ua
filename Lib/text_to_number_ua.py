def text_to_number_ua(text):
    units = {
        'нуль': 0, 'один': 1, 'два': 2, 'три': 3, 'чотири': 4, 'п\'ять': 5, 'шість': 6, 
        'сім': 7, 'вісім': 8, 'дев\'ять': 9
    }
    
    teens = {
        'десять': 10, 'одинадцять': 11, 'дванадцять': 12, 'тринадцять': 13, 
        'чотирнадцять': 14, 'п\'ятнадцять': 15, 'шістнадцять': 16, 'сімнадцять': 17, 
        'вісімнадцять': 18, 'дев\'ятнадцять': 19
    }
    
    tens = {
        'двадцять': 20, 'тридцять': 30, 'сорок': 40, 'п\'ятдесят': 50, 
        'шістдесят': 60, 'сімдесят': 70, 'вісімдесят': 80, 'дев\'яносто': 90
    }
    
    hundreds = {
        'сто': 100, 'двісті': 200, 'триста': 300, 'чотириста': 400, 
        'п\'ятсот': 500, 'шістсот': 600, 'сімсот': 700, 'вісімсот': 800, 'дев\'ятсот': 900
    }
    
    scales = {
        'тисяча': 1000, 'тисячі': 1000, 'тисяч': 1000,
        'мільйон': 1000000, 'мільйони': 1000000, 'мільйонів': 1000000,
        'мільярд': 1000000000, 'мільярди': 1000000000, 'мільярдів': 1000000000
    }
    
    fractions = {
        'десятих': 0.1, 'сотих': 0.01, 'тисячних': 0.001
    }

    numwords = {}
    numwords.update(units)
    numwords.update(teens)
    numwords.update(tens)
    numwords.update(hundreds)
    numwords.update(scales)
    
    integer_part = 0
    fraction_part = 0
    current_fraction_value = 0
    fraction_divider = 1
    is_fraction = False

    words = text.split()
    for i, word in enumerate(words):
        if word == "цілих":
            integer_part += current_fraction_value
            current_fraction_value = 0
            is_fraction = True
            continue
        
        if word in numwords:
            increment = numwords[word]
            if is_fraction:
                current_fraction_value += increment
            else:
                integer_part += increment
        elif word in scales:
            scale = scales[word]
            if is_fraction:
                fraction_part += current_fraction_value * fraction_divider
                current_fraction_value = 0
                fraction_divider = 1
            else:
                integer_part *= scale
        elif word in fractions:
            fraction_divider = fractions[word]
            if len(words) > i + 1 and words[i + 1] in numwords:
                fraction_part += numwords[words[i + 1]] * fraction_divider
                fraction_divider *= 0.1

    if is_fraction and current_fraction_value:
        fraction_part += current_fraction_value * fraction_divider

    result = integer_part + fraction_part
    return round(result, 3)  # Обмеження плаваючої точки

# Приклади використання:
#print(text_to_number_ua("десять цілих тринадцять сотих"))  # Виведе: 10.13
#print(text_to_number_ua("одна тисяча п'ятдесят шість цілих сорок п'ять тисячних"))  # Виведе: 1056.045
#print(text_to_number_ua("дванадцять цілих три тисячних"))  # Виведе: 12.003
#print(text_to_number_ua("одна тисяча п'ятдесят шість"))  # Виведе: 1056