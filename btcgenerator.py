import random
print("Created by Ugnikinn (t.me/ugnikinn) for Hackers Academy (t.me/academyofhackers)\n")
count = int(input("Сколько чеков надо?\n– "))
print("Окей, жди.\n")
f = open("BTChecks.txt", "w")
chars = "0123456789abcdef"
check2 = ""
for x in range(count):
    check = "https://t.me/BTC_CHANGE_BOT?start=c_"
    for i in range(1, 30):
        check = check + random.choice(chars)
    check2 = check2 + check + "\n\n\n"
f.write(check2)
print("Чеки записаны в файл BTChecks.txt. Принимай работу!")
