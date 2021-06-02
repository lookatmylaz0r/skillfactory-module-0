import numpy as np

number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")
for count in range(1, 101):  # более компактный вариант счетчика
    if number == count: break  # выход из цикла, если угадали
print(f"Вы угадали число {number} за {count} попыток.")


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


def game_core_v3(number, start=1, end=101):
    '''Делаем манипуляции с диапазоном от 1 до 100 - по сути реализуем бинарный поиск'''
  count = 1 #заводим счетчик
  while number != start and number != end: #создаем цикл
    range_middle = np.floor((end - start) / 2) #заводим переменную, в которую возвращается разность конца и начала диапазона, деленная пополам, округленная вниз (работаем только с четными числами)
    if number > (start + range_middle): #если загаданное чило больше суммы начала диапазона и половины изначального диапазона
      start += range_middle #начало диапазона равна половине изначального диапазона
    else:
      end -= range_middle #иначе конец диапазона равен
    count += 1 #увеличиваем счетчик на 1
  if number == start:
    print ('number = ' + str(start)) #выводим сообщение, если искомое число равно start
  else:
    print ('number = ' + str(end)) #выводим сообщение, если искомое число равно end
  return count #возвращаем число итераций (счетчик)


score_game(game_core_v3)