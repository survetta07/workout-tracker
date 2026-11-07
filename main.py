def calculate_volume(weight, reps):
    return weight * reps


def add_workout(workouts, name, weight, reps):
    workout = {"name": name, "weight": weight, "reps": reps}
    workouts.append(workout)


def show_workouts(workouts):
    if len(workouts) == 0:
        print("Список пока пуст")
        return
    for number, workout in enumerate(workouts, 1):
        volume = calculate_volume(workout["weight"], workout["reps"])
        print(f"{number}. {workout['name']}: {workout['weight']} кг x {workout['reps']} раз, объём {volume}")


def get_total_volume(workouts):
    total = 0
    for workout in workouts:
        total = total + calculate_volume(workout["weight"], workout["reps"])
    return total


workouts = []

while True:
    print()
    print("1. Добавить упражнение")
    print("2. Показать все упражнения")
    print("3. Показать общий объём")
    print("4. Выход")
    choice = input("Выбери пункт: ")

    if choice == "1":
        name = input("Название упражнения: ")
        weight = input("Вес (кг): ")
        reps = input("Повторения: ")
        if weight.isdigit() and reps.isdigit():
            add_workout(workouts, name, int(weight), int(reps))
            print("Упражнение добавлено!")
        else:
            print("Ошибка: вес и повторения должны быть целыми числами")
    elif choice == "2":
        show_workouts(workouts)
    elif choice == "3":
        print("Общий объём:", get_total_volume(workouts))
    elif choice == "4":
        print("До встречи в зале!")
        break
    else:
        print("Нет такого пункта, попробуй ещё раз")