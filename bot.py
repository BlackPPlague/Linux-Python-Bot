import os

os.system("clear")
typ = input("\033[92m[BOT:] Jaký server mám udělat (teamspeak), (minecraft), (fivem), (web), (mysql)\n\n\033[97m")

if typ == "teamspeak":
    # cd /home/teamspeak
    os.system("wget https://files.teamspeak-services.com/releases/server/3.12.1/teamspeak3-server_linux_amd64-3.12.1.tar.bz2")
    os.system("tar xvfj teamspeak3-server_linux_amd64-3.12.1.tar.bz2")
    # cd teamspeak3-server_linux_amd64
    os.system("cp * -R /home/teamspeak")
    # cd ..
    os.system("rm -r teamspeak3-server_linux_amd64")
    os.system("rm teamspeak3-server_linux_amd64-3.12.1.tar.bz2")
    os.system("touch .ts3server_license_accepted")
#   os.system("clear") // VYPLÉ KVŮLI TESTOVÁNÍ //
    os.system("./ts3server_startscript.sh start")
    # zkopírovat vše co je na stránce a uložit někam (nejlépe do složky daného uživatele pod názvem: token.txt atd...)
    print("\n\033[91m HOTOVO!!\n\033[97m")

elif typ == "minecraft":
    verze = input("\n\033[92m1.16.1\n1.16\n1.15.2\n1.15\n1.14.4\n1.14\n1.13.2\n1.13\n1.12.2\n1.12\n1.11.2\n1.11\n1.10.2\n1.10\n1.9.2\n1.9\n1.8.8\n1.8\n1.7.5\n1.5.2\n\n\033[97m")
    if verze == "1.16.1":
        print("1.16.1")
    elif verze == "1.16":
        print("1.16")

    elif verze == "1.15.2":
        print("1.15.2")

    elif verze == "1.15":
        print("1.15")

    elif verze == "1.14.4":
        print("1.14.4")

    elif verze == "1.14":
        print("1.14")

    elif verze == "1.13.2":
        print("1.13.2")

    elif verze == "1.13":
        print("1.13")

    elif verze == "1.12.2":
        print("1.12.2")

    elif verze == "1.12":
        print("1.12")

    elif verze == "1.11.2":
        print("1.11.2")

    elif verze == "1.11":
        print("1.11")

    elif verze == "1.10.2":
        print("1.10.2")

    elif verze == "1.10":
        print("1.10")

    elif verze == "1.9.2":
        print("1.9.2")

    elif verze == "1.9":
        print("1.9")

    elif verze == "1.8.8":
        print("1.8.8")

    elif verze == "1.8":
        print("1.8")

    elif verze == "1.7.5":
        print("1.7.5")

    elif verze == "1.5.2":
        print("1.5.2")

elif typ == "fivem":
    print("fivem")

elif typ == "web":
    print("web")

elif typ == "mysql":
    print("MySQL")