import sys
import json


data = []

def main():
    # Проверяем, переданы ли аргументы
    if len(sys.argv) > 1:
        
        data = sys.argv[1:]  
        print("Переданные данные:", data)
        file = data[0]
        with open(f'{file}.json', 'r') as f:  # Открываем файл для чтения
            loaded_array = json.load(f)
            for i in range(len(loaded_array)):
                text = loaded_array[i].split()
                bol = False
                while bol != True:
                    answe = input(f"Введите перевод слова {text[0]}: ")
                    if answe == text[1]:
                        print("Вы овтветили верно!")
                        bol = True
                    else: 
                        print("Попробуйте ещё раз")
                        continue

            
            print("Вы дали перевод всем словам!")

            
    else:
        print("Не переданы данные.")




if __name__ == "__main__":
    main()

