File = open("raw.txt", "r")

for i in range(15):
    Linw = File.readline()
    Linsplit = Linw.split(":")
    print(Linsplit[1] + ":" + Linsplit[0] + ",")