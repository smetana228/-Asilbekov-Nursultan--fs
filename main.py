import os
import os.path
import shutil
from pathlib import Path
from commands import*
import sys
if sys.argv[1]=='create':
        if len(sys.argv)==2:
                print('Введите название файла')
        elif len(sys.argv)==3:
                create(sys.argv[2])
        elif len(sys.argv)==4:
                create(sys.argv[2],sys.argv[3])
if sys.argv[1]=='copy':
        if len(sys.argv)==2:
                print('Введите название файла')
        elif len(sys.argv)==3:
                copy(sys.argv[2])
        elif len(sys.argv)==4:
                copy(sys.argv[2],sys.argv[3])
if sys.argv[1]=='init':
        if len(sys.argv)==2:
                print('Введите название папки')
        elif len(sys.argv)==3:
                init(sys.argv[2])
        elif len(sys.argv)==4:
                init(sys.argv[2],sys.argv[3])
if sys.argv[1]=='list_':
        if len(sys.argv)==2:
                list_()
        elif len(sys.argv)==3:
                list(sys.argv[2])
if sys.argv[1]=='move':
        if len(sys.argv)==2:
                print('Введите название папки')
        elif len(sys.argv)==3:
                print('Введите название директории')
        elif len(sys.argv)==4:
                move(sys.argv[2],sys.argv[3])
if sys.argv[1]=='backup':
        if len(sys.argv)==2:
                backup()
        elif len(sys.argv)==3:
                backup(sys.argv[2])
if sys.argv[1]=='snapshot':
        if len(sys.argv)==2:
                snapshot()
        elif len(sys.argv)==3:
                snapshot(sys.argv[2])




'''
def create(filename, dirs=os.getcwd()):
    p=os.getcwd()
    if not dirs==os.getcwd():
        os.chdir(os.getcwd()+dirs)
    if not os.path.exists(filename):
            print(f'{filename} создан по директории {os.getcwd()}')
            file = open(filename,'a')
    else:
        ask=input(f'{filename} уже существует. Вы хотите его заменить? Y/N:')
        print(ask)
        if ask=='Y':
            print(f'{filename} создан по директории {os.getcwd()}')
            file = open(filename,'a')
    os.chdir(p)
 	
def copy(filename):
    file_copy=filename
    for x in range(len(filename)):
        if filename[x]=='.':
            file_copy=(filename[:x]+'_copy'+filename[x:])
    if os.path.exists(file_copy):
        ask=input(f'{file_copy} уже существует. Вы хотите его заменить? Y/N:')
        print(ask)
        if ask=='Y':
            print(f'{filename} скопирован под названием {file_copy} по директории {os.getcwd()}')
            file = open(file_copy,'a')
            shutil.copyfile(filename,file_copy)
    if os.path.exists(filename):
        print(f'{filename} скопирован под названием {file_copy} по директории {os.getcwd()}')
        file = open(file_copy,'a')
        shutil.copyfile(filename,file_copy)
    if not os.path.exists(filename):
        print(f'Невозможно скопировать {filename}, так как по директории {os.getcwd()} его не существует')

        
def list_(directory=os.getcwd()):
    for adr, directs, files in os.walk(directory):
        for name in files:
            print(os.path.join(adr, name))

            
def move(filename, direct):
    if os.path.exists(filename) and os.path.exists(direct):
        print(f'{filename} перемещен по директории {direct}')
        file_move=shutil.move(filename, direct)
    elif not os.path.exists(filename):
        print(f'Невозможно переместить {filename}, так как по директории {os.getcwd()} его не существует')
    elif not os.path.exists(direct):
        print(f'Директории {direct} не существует')

        
def init(folder_name,dirs=os.getcwd()):
    p=''.join(reversed(os.getcwd()))
    os.chdir(dirs)
    folder=os.mkdir(folder_name)

    
def backup(folder_name):
    folder_backup=folder_name+'_backup'
    p=''.join(reversed(os.getcwd()))
    h=p
    for x in range(len(p)):
        if not p[x].isalpha():
            g=h[x:]
            break
    g=''.join(reversed(g))
    h=g+folder_name
    f=g+folder_backup
    if os.path.exists(h):
        os.chdir(g)
        folder=os.mkdir(folder_backup)
        os.chdir(h)
        for adr, directs, files in os.walk(h):
            for name in files:
                print(name)
                file=shutil.copy(name,f,follow_symlinks=False)
    else:
        print(f'Папки под названием {folder_name} не существует')

    
def snapshot(direct):
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    if os.exists(direct):
        for file_name in os.listdir(dir_path):
            
            my_file = drive.CreateFile({'title': f'{file_name}'})
            my_file.SetContentFile(os.path.join(direct, file_name))
            my_file.Upload()
            print(f'File {file_name} was uploaded!')
                
        print(f'Директория {direct} была успешно загружен в облако')
    else:
        print(f'Директории {direct} не существует')
'''
    
    


