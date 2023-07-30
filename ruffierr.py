text_input = ['Низкий', 'Ниже среднего', 'Средний', 'Выше среднего', 'Высокий']

def get_ind(p1, p2, p3):
    if ((4*(p1 + p2 + p3) - 200) / 10) % 1 != 0:
        return (4*(p1 + p2 + p3) - 200) / 10
    return int((4*(p1 + p2 + p3) - 200) / 10)


def get_age(age):
    index = (min(15, age) - 7) // 2
    return 21 - 1.5 * index

def get_result(my_ind, min_level):
    if my_ind >= min_level:
        return 0
    min_level -= 4
    if my_ind >= min_level:
        return 1
    min_level -= 5
    if my_ind >= min_level:
        return 2
    min_level -= 5.5
    if my_ind >= min_level:
        return 3
    return 4

def test(p1, p2, p3, age, name):
    if age < 7:
        return 'Данных для данного возраста нет'
    else:
        index = get_ind(p1, p2, p3)
        res = text_input[get_result(index, get_age(age))]
        if name == '':
            return 'Ваш индекс Руфье: ' + str(index) + '\n' + '\n' + 'Уровень работоспособности сердца: ' + res
        else:
            return 'ваш индекс Руфье: ' + str(index) + '\n' + '\n' + 'Уровень работоспособности сердца: ' + res
