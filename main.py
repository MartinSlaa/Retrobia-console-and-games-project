import time
import test

def main():
    while True:
        text()
        choice = input("\n\nEnter choice: ")

        printLines(50)

        if(choice == "1"):
            print("\n\nGame 1")
            printLines(50)
            time.sleep(1)
        elif(choice == "2"):
            print("\n\nGame 2")
            printLines(50)
            time.sleep(1)
        elif(choice == "3"):
            print("\n\nGame 3")
            printLines(50)
            time.sleep(1)
        elif(choice == "0"):
            print("\n\nExiting...")
            printLines(50)
            time.sleep(1)
            break
        else:
            print("\n\nInvalid...")
            printLines(50)
            time.sleep(1)
            

def text():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    printLines(100)

    print("""\n
                ██████╗ ███████╗████████╗██████╗  ██████╗ ██████╗ ██╗ █████╗ 
                ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗██╔══██╗██║██╔══██╗
                ██████╔╝█████╗     ██║   ██████╔╝██║   ██║██████╔╝██║███████║
                ██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║██╔══██╗██║██╔══██║
                ██║  ██║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝██║██║  ██║
                ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝""")
    
    printLines(100)
    
    print("""\n
[About us]
[How to start]
[etc...]""")

    printLines(100)

    print("""\n
    1. [Game 1]
    2. [Game 2]
    3. [etc...]
    0. Exit""")

    printLines(50)

def printLines(num):
    for i in range(num):
        print("_", end = "")

main()