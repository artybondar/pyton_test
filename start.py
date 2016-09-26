# utf-8
# PEP-8
# dir help - функции помощи, пример: dir(os),help(psutil)
# pip install name_module - установка стороннего модуля
# pass - пустышка
# type - тип переменной
import os # подключение модуля работы с ОС
import sys # подключение модуля работы с системой
import psutil # подключение стороннего модуля
import shutil

print("Привет, программист!")
name = input("Ваше Имя: ")
print(name,", добро пожаловать в мир Python!")
answer = ''
while answer !='Q':
	answer = input("Хочешь работать? (Y/N/Q)")	
	if answer == 'Y':
		print("Вы молодец!")
		print("1 - Вевести список файлов")
		print("2 - Вывести инфо о системе")
		print("3 - Вывести список процессов")
		print("4 - Копирование файлов в текущей папке")
		do = int(input("Укажите действие: "))
		if do == 1:
			print(os.listdir())
		elif do == 2:
			print("Данные о системе:")
			print("Количество процессов: ",psutil.cpu_count())
			print("Платформа: ",sys.platform)
			print("Теущая папка: ",os.getcwd())
			print("Пользователь: ",os.getlogin())
		elif do == 3:
			print(psutil.pids())
		elif do == 4:
			print("Дублирование текущих файлов...")
			file_list = os.listdir()
			i = 0
			while i < len(file_list):
				if  os.path.isfile(file_list[i]):
					newfile = file_list[i] + '.dup'
					shutil.copy(file_list[i], newfile) # копирование
					i +=1
			print("... Дублирование завершено.")
		else:
			print("Нет такого ответа")
	elif answer == 'N':
		print("До свидания!")
	else:
		pass
	