import hashlib

text = input("Введите текст: ")

h = hashlib.md5(text.strip().encode("utf-8"))

file = open("password.txt", "a")
file.write("\nВаш хэш: " + str(h.hexdigest()) + " - " + str( text ))
file.close()

print("Ваш хэш: " + str(h.hexdigest()))
