import os
import requests
import readline
import multiprocessing.dummy as mp

apagar1 = os.popen("rm awdc.txt").read()
apagar3 = os.popen("rm  awdc2.txt").read()
criar1 = os.popen("echo >> awdc.txt").read()
criar2 = os.popen("echo >> awdc2.txt").read()

print("__________________________________________________________")
print("|                                      _____     ______  |")
print("|     /\     \          /\          /  |    \   /        |")
print("|    /  \     \        /  \        /   |     |  |        |")
print("|   /    \     \      /    \      /    |     |  |        |")
print("|  /------\     \    /      \    /     |     |  |        |")
print("| /        \     \  /        \  /      |     |  |        |")
print("|/          \     \/          \/       |_____/  \______  |")
print("----------------------------------------------------------")
print("")
print("")

awdc = input("@ ")

arquivo = open(awdc,"r").readlines()
common = open("common.txt","r").readlines()
Awdc = open("awdc2.txt","w")

for linha in arquivo:
    linha2 = linha.rstrip('\n')
    d = "https://" + linha2 + "/"
    print(d)

    for l in common:
        f = l.rstrip('\n')
        fd = d + f
        r = requests.get(fd)
        if r.status_code == 200:
            Awdc.write(fd)
            Awdc.write("\n")


    def func1(*args):
        os.popen("dirb " + d + " -w common.txt -o awdc.txt").read()
    p = mp.Pool(20)
    p.map(func1, range(0, 1))
    p.close()

    os.popen("cat awdc.txt | grep '" + d + "' | grep 'CODE:200' | cut -d ' ' -f2 | uniq -u >> awdc2.txt").read()

