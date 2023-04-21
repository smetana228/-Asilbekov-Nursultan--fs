import os
import os.path
import shutil
import zipfile
from pathlib import Path

def create(filename, dirs=os.getcwd()):
    p=os.getcwd()
    #Получает директорию
    if not dirs==os.getcwd():
        os.chdir(os.getcwd()+dirs)

    #Cоздание файла в случае если он еще не существует
    if not os.path.exists(filename):
            file = open(filename,'a')
            print(f'{filename} создан по директории {os.getcwd()}')

    #Если файл уже существует, спрашивает у пользователя, хочет ли он заменить файл
    else:
        ask=input(f'{filename} уже существует. Вы хотите его заменить? Y/N:')
        if ask=='Y':
            file = open(filename,'a')
            print(f'{filename} создан по директории {os.getcwd()}')
    os.chdir(p)
 	
def copy(filename,dirs=os.getcwd()):
    p=os.getcwd()

    #Получает директорию
    if not dirs==os.getcwd():
        dirs=os.getcwd()+dirs
    file_copy=filename

    #Дает названия скопированному файлу
    for x in range(len(filename)):
        if filename[x]=='.':
            file_copy=(filename[:x]+'_copy'+filename[x:])

    #Проверяет, существует ли файл, который пользватель хочет скопировать
    if not os.path.exists(filename):
        print(f'Невозможно скопировать {filename}, так как по директории {dirs} его не существует')

    #Проверяет не существует ли уже копия, если существует, спрашивает у пользователя, хочет ли он заменить копию или нет
    os.chdir(dirs) 
    if os.path.exists(file_copy):
        ask=input(f'{file_copy} уже существует. Вы хотите его заменить? Y/N:')
        os.chdir(p)
        if ask=='Y':
            file = open(file_copy,'a')
            shutil.copyfile(filename,file_copy)
            if not dirs==p:
                shutil.move(file_copy,dirs)
            print(f'{filename} скопирован под названием {file_copy} по директории {dirs}')
    os.chdir(p)

    #Копирует файл
    if os.path.exists(filename):
        shutil.copyfile(filename,file_copy)
        if not dirs==p:
            shutil.move(file_copy,dirs)
            shutil.copyfile(filename,file_copy)
        print(f'{filename} скопирован под названием {file_copy} по директории {dirs}')

        
def list_(directory=os.getcwd()):

    #Выводит все файлы в дирекории
    for adr, directs, files in os.walk(directory):
        for name in files:
            print(os.path.join(adr, name))

            
def move(filename, dirs):
    #Получает директории
    if not dirs==os.getcwd():
        dirs=os.getcwd()+dirs

    #Перемещает файл
    if os.path.exists(filename) and os.path.exists(direct):
        print(f'{filename} перемещен по директории {direct}')
        file_move=shutil.move(filename, direct)

    #Проверяет существует ли файл, который пользователь хочет переместить
    elif not os.path.exists(filename):
        print(f'Невозможно переместить {filename}, так как по директории {os.getcwd()} его не существует')
    #Проверяет существует ли директорию, по которой пользователь хочет переместить файл
    elif not os.path.exists(direct):
        print(f'Директории {direct} не существует')

        
def init(folder_name,dirs=os.getcwd()):

    #Получает директорию
    if not dirs==os.getcwd():
        dirs=os.getcwd()+dirs

    #Проверяет существует ли директория по которой пользователь хочет создать папку
    elif not os.path.exists(dirs):
        print(f'Директории {dirs} не существует')
    os.chdir(dirs)
    if not os.path.exists(folder_name)
        #Создает папку
        folder=os.mkdir(folder_name)
        print('Папка была успешно создана')
    else:
        print(f'Невозможно создать папку {folder_name}, так как она уже существует')

def backup(folder_name='fn'):

    #Конвертирует папку в зип файл
    if not os.path.exists(folder_name+'.zip'):
        fantasy_zip = zipfile.ZipFile(folder_name+'.zip', 'w')
        for folder, subfolders, files in os.walk(os.getcwd()):
            for file in files:
                fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), os.getcwd()), compress_type = zipfile.ZIP_DEFLATED)
        fantasy_zip.close()
        print('Бэкап был успешно создан')
    else:
        ask=input(f'{folder_name}.zip уже существует. Вы хотите его заменить? Y/N:')
        if ask=='Y':
            os.remove(folder_name+'.zip')
            fantasy_zip = zipfile.ZipFile(folder_name+'.zip', 'w')
            for folder, subfolders, files in os.walk(os.getcwd()):
                for file in files:
                    fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), os.getcwd()), compress_type = zipfile.ZIP_DEFLATED)
            fantasy_zip.close()
            print('Бэкап был успешно создан')

    
def snapshot(folder_name='fn'):
    #Копирует содержимое папки в папку snapshot
    p=os.getcwd()
    g='_'+os.getlogin()
    y='snapshot'+g
    def snap():
        folder=os.mkdir(y)
        for adr, directs, files in os.walk(p):
            for dit in directs:
                if not y in adr:
                    os.chdir(adr.replace(folder_name,f'{folder_name}\\{y}'))
                    if not dit==y:
                        os.mkdir(dit)
                    os.chdir(adr)
            for name in files:
                if not 'snapshot' in adr:
                    file=shutil.copy(name,adr.replace(folder_name,f'{folder_name}\\{y}'),follow_symlinks=False)
        print('Снэпшот был успешно сделан')
    if not os.path.exists(y):
        snap()
    else:
        shutil.rmtree(y)
        snap()

