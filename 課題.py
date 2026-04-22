#1
# animals.txtファイルを生成して、動物（3匹）を追加して
with open("animals.txt","r") as animals_file:
    for animals in animals_file:
       print("名称：",animals.strip())

#2 OK
with open("fruits.txt","w") as fruits_file:
    fruits_file.write("apple","banana","orange")
with open(fruits_file,"r") as fruits_file:
    for fruits in fruits_file:
        print("名称：",fruits.strip())

#3 OK
def write_list(todo):
    with open("task.txt","a") as task_file:
        task_file.write(todo+"\n")
def read_list():
    with open("task.txt", "r") as task_file:
        for task in task_file:
            print("やること：", task.strip())

write_list(input("ToDoリストに入力："))
read_list()
