import mmap
import multiprocessing
import os
import time

BUFFER_SIZE = 1024  # Размер буфера

def producer(mmap_filename, ready_event):
    # Открываем файл для записи в mmap
    with open(mmap_filename, "r+b") as f:
        mm = mmap.mmap(f.fileno(), BUFFER_SIZE)
        message = "Привет от производителя!"
        # Очищаем буфер и записываем строку
        mm.seek(0)
        mm.write(message.encode('utf-8').ljust(BUFFER_SIZE, b'\x00'))
        mm.flush()
        print("[Производитель] Сообщение отправлено.")
        mm.close()
    ready_event.set()  # Сигнал потребителю

def consumer(mmap_filename, ready_event):
    ready_event.wait()  # Ждём, пока производитель отправит данные
    with open(mmap_filename, "r+b") as f:
        mm = mmap.mmap(f.fileno(), BUFFER_SIZE)
        mm.seek(0)
        raw = mm.read(BUFFER_SIZE)
        message = raw.rstrip(b'\x00').decode('utf-8')
        print("[Потребитель] Принято сообщение:", message)
        mm.close()

if __name__ == "__main__":
    # Создаём временный файл для mmap
    mmap_filename = "shared_buffer.bin"
    # Инициализируем файл нулями
    with open(mmap_filename, "wb") as f:
        f.write(b'\x00' * BUFFER_SIZE)

    # Событие для синхронизации
    ready_event = multiprocessing.Event()

    # Создаём процессы
    p_producer = multiprocessing.Process(target=producer, args=(mmap_filename, ready_event))
    p_consumer = multiprocessing.Process(target=consumer, args=(mmap_filename, ready_event))

    # Запускаем процессы
    p_producer.start()
    p_consumer.start()

    # Ждём завершения
    p_producer.join()
    p_consumer.join()

    # Удаляем временный файл
    os.remove(mmap_filename)
