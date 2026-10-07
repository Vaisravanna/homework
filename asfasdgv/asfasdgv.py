tasks = ["Исправить ошибку входа", "Проверить сервер", "Обновить программу"]

while True:
    print("\n1 - Показать все задачи")
    print("2 - Добавить новую задачу")
    print("3 - Удалить выполненную задачу")
    print("4 - Показать количество задач")
    print("0 - Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        if len(tasks) == 0:
            print("Список задач пуст")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

    elif choice == "2":
        task = input("Введите новую задачу: ")
        tasks.append(task)

    elif choice == "3":
        if len(tasks) == 0:
            print("Список задач пуст")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])
            n = int(input("Введите номер выполненной задачи: "))
            tasks.pop(n - 1)

    elif choice == "4":
        print("Количество задач:", len(tasks))

    elif choice == "0":
        break

    if len(tasks) > 5:
        print("Внимание! Накопилось много задач.")