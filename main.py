user_sentence = input("Введите предложение ")

counter_letters = 0
counter_digits = 0

for i in user_sentence.lower():
    if i.isalpha():
         counter_letters += 1
    elif i.isdigit():
        counter_digits += 1

print("Количество букв - ", counter_letters)
print("Количество цифр - ", counter_digits)

################

user_sentence_task_2 = input("Введите предложение ")
user_symbol = input("Выберите символ для поиска ")

counter_symbol = 0

for i in user_sentence_task_2:
    if i == user_symbol:
        counter_symbol += 1

print("выбраный символ повторяется - ", counter_symbol, "раз(a)")

##############

user_sentence_task_3 = input("Введите предложение ")
searching_word = input("слово для поиска ")
word_for_replace = input("слово для замены ")

print(user_sentence_task_3.replace(searching_word, word_for_replace))

#######

user_sentence_task_4 = input("Введите предложение ")

print(user_sentence_task_4[2])
print((user_sentence_task_4[-2]))
print(user_sentence_task_4[:5])
print(user_sentence_task_4[:-3])
print(user_sentence_task_4[::2])
print((user_sentence_task_4[1::2]))
print((user_sentence_task_4[::-1]))
print(user_sentence_task_4[-1::-2])
print(len(user_sentence_task_4))

####

user_text_task_5 = input("Введите текст ").split(". ")
new_text = ""

for i in user_text_task_5:
    new_text += i.capitalize() + ". "

print(new_text[:-2])


######


user_text_task_6 = input("Введите текст ")

digit_in_user_text = 0

for i in user_text_task_6:
    if i.isdigit():
        digit_in_user_text += 1

print("Amount of digits -", digit_in_user_text)

#####

user_text_task_7 = input("Введите текст ")

separates_symbols = 0

for i in user_text_task_7:
    if i == "." or i == ",":
        separates_symbols += 1

print("amount of separate symbols - ", separates_symbols)

######

user_text_task_8 = input("Введите уже наконец свой текст! ")
counter_of_exclamation_point = 0

for i in user_text_task_8:
    if i == "!":
        counter_of_exclamation_point += 1

print("amount of exclamation symbols -", counter_of_exclamation_point)





