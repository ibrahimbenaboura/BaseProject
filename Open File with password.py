TheFile = open("==> THE FILE PATH HERE <==", "r")
TheTries = 3
ThePassword = "==> YOUR PASSWORD HERE <=="
FileContent = TheFile.read()


while TheTries > 0 :
    userpassword = input("Put The Password : ")



    if userpassword == ThePassword :
        print(FileContent)
        break



    else : 
        TheTries -= 1
        print("The Password Is Wrong.")
        print(f"You Have {TheTries} Tries Left.")



else :
    print("Your Tries Are Done.")

TheFile.close()      












