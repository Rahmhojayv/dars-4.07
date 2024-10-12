# 1 masala
# import json
# json1 = {
#     "last_name":  "Abdurahmonov",
#     "first_name":  "Abdunabi",
#     "age": 16,
#     "year": 2008
# }
# with open('data.json', 'w')as fayl:
#     json.dump(json1, fayl, indent=4)
#
# with open("data.json", "r")as fayl:
#     json1 = json.load(fayl)
# for kalitlar, qiymatlar in json1.items():
#     print(f"{kalitlar}: {qiymatlar}")

# 2 masala
# import json
# oquvchi = {
#     "Fast_name": "Azimqulov",
#     "First_name": "Aziz",
#     "Age": 17,
#     "Year": 2007
# }
#
# with open('student.json', 'w')as fayl:
#     student = json.dump(oquvchi,fayl,indent=4)
#
# with open("student.json", "r")as fayl:
#     oquvchi = json.load(fayl)
# for kalit, qiymat in oquvchi.items():
#     print(f"{kalit}: {qiymat}")

# 3 masala
# with open('homework.txt', 'w')as fayl:
#     fayl.write("Finish homework \nClean the room \nRead a book")
#     qatorlar = 1
# with open("homework.txt", "r")as fayl:
#     for line in fayl:
#         print(f"{qatorlar}.", line.strip())
#         qatorlar += 1

# 4 masala
# with open('books.txt', 'w')as fayl:
#     fayl.write("O'tkan kunlar - Abdulla Qodiriy,  \n")
#     fayl.write("Momo Yer - Chingiz Aytmatov, \n")
#     fayl.write("Alifbo - Usmon Nosir, \n")
#     fayl.write("Seni yod etaman -  G'afur G'ulom\n")
#
# kitoblar = {}
# with open('books.txt', 'r')as fayl:
#     for line in fayl:
#         nom, moallif = line.strip().split(' - ')
#         kitoblar[nom] = moallif
# kitob_sorash = input("Sizga qanday kitob kerak ? :")
# if kitob_sorash in kitoblar:
#     print(f"Moallifi: {kitoblar[kitob_sorash]}")
# else:
#     print("Bunday kitob yoq ekan")