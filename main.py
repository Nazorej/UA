# Это программа на Python
# Распознавание украинского текста
# https://github.com/UB-Mannheim/tesseract/wiki

# Импортируем модули
import cv2
import pytesseract
from tqdm import tqdm

# Укажите путь к исполняемому файлу tesseract в вашей системе
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Укажите количество файлов для обработки
num_files = 10

# Создаем файл для записи всего текста
with open('output_all.txt', 'w') as all_f:
    # Обработка файлов от 1.png до num_files.png
    for i in tqdm(range(1, num_files+1), desc="Обработка файлов"):
        # Формируем имя файла
        filename = f'{i}.png'
        
        # Загрузите изображение
        img = cv2.imread(filename)

        # Преобразуйте изображение в текст с помощью pytesseract
        text = pytesseract.image_to_string(img, lang='ukr')

        # Запишите текст в отдельный файл
        with open(f'output{i}.txt', 'w') as f:
            f.write(text)
        
        # Добавьте текст в общий файл
        all_f.write(text + '\n\n')

print(f"Текст записан в файлы output1.txt до output{num_files}.txt и output_all.txt")
