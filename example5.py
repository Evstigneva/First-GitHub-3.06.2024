class File:
    def __init__(self, name):
        self.name=name
        self.in_trash=False
        self.is_deleted=False
    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash=False
    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted=True
    def read(self):
        if self.is_deleted==True:
            print(f'ErrorReadFileDeleted({self.name})')
        elif self.in_trash==True:
            print(f'ErrorReadFileTrashed({self.name})')
        else:
            print(f'Прочитали все содержимое файла {self.name}')
    def write(self, content):
        if self.is_deleted==True:
            print(f'ErrorWriteFileDeleted({self.name})')
        elif self.in_trash==True:
            print(f'ErrorWriteFileTrashed({self.name})')
        else:
            print(f'Записали значение {content} в файл {self.name}')
class Trash:
    content=[]
    @staticmethod
    def add(a):
        if isinstance(a, File):
            Trash.content.append(a)
            a.in_trash=True
    @staticmethod
    def clear():
        print('Очищаем корзину')
        for i in Trash.content:
            File.remove()
            Trash.content.remove(i)
        print('Корзина пуста')
    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        