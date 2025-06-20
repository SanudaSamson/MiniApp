
import datetime

def greet(name):
    now = datetime.datetime.now()
    return f"Hello, {name}!. It's {now.strftime('%Y-%m-%d %H:%M:%S')}."

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))