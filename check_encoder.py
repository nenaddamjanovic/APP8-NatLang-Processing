#  Provera tipa enkodera za tekstualni fajl
import chardet

with open("miracle_in_the_andes.txt", "rb") as file:
    raw_data = file.read()

result = chardet.detect(raw_data)
print(result)

