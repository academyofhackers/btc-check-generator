import random
print("Created by Ugnikinn (t.me/ugnikinn)\n")
count = int(input("Скока чеков нада?\n– "))
print("Окей, жди.\n")
f = open("/storage/emulated/0/Download/BTChecks.txt", "w")
chars = "0123456789abcdefabcdef"
check2 = ""
for x in range(count):
    check = "https://t.me/btc_change_bot?start=c_"
    for i in range(1, 30):
        check = check + random.choice(chars)
    check2 = check2 + check + "\n\n\n"
f.write(check2)
print("Чеки записаны в файл BTChecks.txt во внутренней памяти смартфона. Принимай работу!")
