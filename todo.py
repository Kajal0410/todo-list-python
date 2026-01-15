import json

data_file = "todo_data.json"

def read_data():
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except:
        return []

def write_data(data):
    with open(data_file, "w") as f:
        json.dump(data, f)

def add():
    data = read_data()
    t = input("Enter task: ")
    data.append([t, False])
    write_data(data)
    print("Task added")

def show():
    data = read_data()
    if not data:
        print("No tasks")
    else:
        for i in range(len(data)):
            status = "Done" if data[i][1] else "Pending"
            print(f"{i+1}. {data[i][0]} - {status}")

def done():
    data = read_data()
    show()
    try:
        n = int(input("Task number: "))
        data[n-1][1] = True
        write_data(data)
        print("Task completed")
    except:
        print("Error")

def remove():
    data = read_data()
    show()
    try:
        n = int(input("Task number: "))
        data.pop(n-1)
        write_data(data)
        print("Task removed")
    except:
        print("Error")

while True:
    print("\n1.Add  2.Show  3.Done  4.Remove  5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add()
    elif ch == "2":
        show()
    elif ch == "3":
        done()
    elif ch == "4":
        remove()
    elif ch == "5":
        break
    else:
        print("Invalid")
