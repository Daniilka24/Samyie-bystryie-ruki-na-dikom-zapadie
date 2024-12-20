import random
import time
print("Это программа, которая замеряет скорость печати.")
print("Вам будет показана случайная фраза, которую вам предстоит напечатать самостоятельно. Готовы?")
input()

phrase1 = "В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!"
phrase2 = "Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства."
phrase3 = "Съешь ещё этих мягких французских булок да выпей же чаю."

start_time = time.time()
a = random.randint(1, 3)
if a == 1:
  print(phrase1)
if a == 2:
  print(phrase2)
if a == 3:
  print(phrase3)
user_input = input("Напечатайте фразу выше: ")
end_time = time.time()
elapsed_time = end_time - start_time
symbols_per_minute = len(user_input)/elapsed_time*60


print(f"Ваша скорость печати: {symbols_per_minute} символов в минуту.")
print(f"Время, затраченное на печать: {elapsed_time} секунд.")