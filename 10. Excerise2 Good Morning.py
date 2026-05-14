import time

name = input("Enter your name: ")
name = name.capitalize()

present_time = time.strftime("%H:%M:%S")
present_time = int(time.strftime("%H"))

if 2 <= present_time <= 12:
    print(f"Good Morning {name}", " its time: ", present_time)
elif 12 >= present_time <= 5:
    print(f"Good Afternoon {name}", " its time: ", present_time)
elif 5 >= present_time <= 8:
    print(f"Good Evening {name}", " its time: ", present_time)
else:
    print(f"Good Night{name}", " its time: ", present_time)
