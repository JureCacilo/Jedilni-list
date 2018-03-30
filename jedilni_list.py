# Programcek, ki ti shrani jedilni list, ki ga vneses, v txt datoteko
print("Dobrodosli v programu za pisanje jedilnega lista.")
jedilni_list = {}
izbira = "da"
jedilni_list_file = open("jedilni_list.txt", "w+")

while True:
    jed = input("Vnesi jed, ki jo zelite v jedilnem listu: ")
    cena = float(input("Vnesite ceno jedi (v evrih): "))
    jedilni_list[jed] = cena

    izbira = input("Zelite vnesti se eno jed (da/ne):")

    if izbira.lower() == "ne":
        break


print("Jedilni list:")
jedilni_list_file.write("Jedilni list:\n")

for jed in jedilni_list:
    print("Jed: "+ jed +" , cena: " + str(jedilni_list[jed])+" evra")
    jedilni_list_file.write("Jed: "+ jed +" , cena: " + str(jedilni_list[jed])+" evra\n")

