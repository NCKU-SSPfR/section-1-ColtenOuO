import webbrowser, sys,  os  

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def input_math():
    while True:
        user_input = input("1 times 1 = ? ")
        if user_input == 1: 
            Open_Video() 
            break
        elif user_input == "exit":
            sys.exit()
        else:
            print("Wrong! Try again.")
            Open_Video()
def Open_Video():
    webbrowser.open(url)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")

input_math()
