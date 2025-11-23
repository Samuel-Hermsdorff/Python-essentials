#FileNotFound

# try:
#     file = open("a_file.txt", encoding="utf-8")
#     a_dic = {"key":"value"}
#     print(a_dic["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w", encoding="utf-8")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height shoud not be over 3 meters")

bmi = weight / height ** 2
print(bmi)