import os
import stat
import sys
from pathlib import Path

def get_filesystem_info(path="/"):
    """Получение информации о файловой системе по указанному пути."""
    try:
        # Получаем статистику о файловой системе (работает в Unix-подобных системах)
        fs_info = os.statvfs(path)
        
        print(f"Информация о файловой системе для пути: {path}")
        print("-" * 50)
        print(f"Размер блока: {fs_info.f_bsize} байт")
        print(f"Общее количество блоков: {fs_info.f_blocks}")
        print(f"Количество свободных блоков: {fs_info.f_bfree}")
        print(f"Количество доступных блоков (для непривилегированных пользователей): {fs_info.f_bavail}")
        print(f"Общее количество inode: {fs_info.f_files}")
        print(f"Количество свободных inode: {fs_info.f_ffree}")
        print(f"Количество доступных inode (для непривилегированных пользователей): {fs_info.f_favail}")
        
        # Вычисляем общий и свободный размер в ГБ
        total_size_gb = (fs_info.f_blocks * fs_info.f_bsize) / (1024 ** 3)
        free_size_gb = (fs_info.f_bfree * fs_info.f_bsize) / (1024 ** 3)
        print(f"Общий размер: {total_size_gb:.2f} ГБ")
        print(f"Свободный размер: {free_size_gb:.2f} ГБ")
        
        # Тип файловой системы (не всегда доступен в os.statvfs, зависит от ОС)
        # Для Windows или онлайн-компиляторов может потребоваться другой подход
        try:
            if sys.platform.startswith('win'):
                print("Тип файловой системы: NTFS (предположительно для Windows)")
            else:
                print("Тип файловой системы: Не удалось определить через os.statvfs")
        except Exception as e:
            print(f"Ошибка при определении типа файловой системы: {e}")
            
    except OSError as e:
        print(f"Ошибка при получении информации о файловой системе: {e}")
        print("Примечание: os.statvfs() работает только в Unix-подобных системах. Для Windows используйте другие методы.")

def get_file_info(file_path):
    """Получение информации о конкретном файле."""
    try:
        # Получаем статистику о файле
        file_stats = os.stat(file_path)
        print(f"\nИнформация о файле: {file_path}")
        print("-" * 50)
        print(f"Inode: {file_stats.st_ino}")
        
        # Определяем тип файла с помощью stat
        mode = file_stats.st_mode
        if stat.S_ISREG(mode):
            print("Тип файла: Обычный файл")
        elif stat.S_ISDIR(mode):
            print("Тип файла: Директория")
        elif stat.S_ISLNK(mode):
            print("Тип файла: Символическая ссылка")
        else:
            print("Тип файла: Другое")
            
        # Атрибуты файла (права доступа)
        print(f"Права доступа (в восьмеричном виде): {oct(mode & 0o777)}")
        print(f"Владелец (UID): {file_stats.st_uid}")
        print(f"Группа (GID): {file_stats.st_gid}")
        print(f"Размер: {file_stats.st_size} байт")
        print(f"Время последнего доступа: {file_stats.st_atime}")
        print(f"Время последней модификации: {file_stats.st_mtime}")
        
    except OSError as e:
        print(f"Ошибка при получении информации о файле {file_path}: {e}")

# Тестирование функций
if __name__ == "__main__":
    # Информация о файловой системе (для корневого каталога или текущего)
    get_filesystem_info("/")
    
    # Информация о конкретных файлах
    # В онлайн-компиляторе может не быть доступа к файлам, поэтому используем текущий скрипт или временный файл
    try:
        # Пробуем получить информацию о текущем файле
        current_file = __file__
        get_file_info(current_file)
    except NameError:
        # Если __file__ недоступен (например, в Jupyter), создадим временный файл
        temp_file = "/tmp/testfile.txt" if not sys.platform.startswith('win') else "testfile.txt"
        try:
            with open(temp_file, 'w') as f:
                f.write("Тестовый файл")
            get_file_info(temp_file)
        except Exception as e:
            print(f"Не удалось создать временный файл: {e}")
