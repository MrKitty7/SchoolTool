import os
import sys
import subprocess
from datetime import date, datetime
print('-----------')
print('Welcome to the SchoolTool!')
print('-----------')
print('Select one of the options stated: ')
print('1. Homework')
print('2. Exams')
print('3. Resources')
selection = int(input())

def add_homework():
    with open('subjects.txt', 'r') as f:
        for subject in f.read().splitlines():
            path = 'subjects/' + subject.lower()
            try:
                os.makedirs('subjects')
                os.makedirs(path)
            except:
                continue
        sel_subject = input('Specify which subject you would like me to add homework to. ')
        title = input('Specify the title of the homework. ')
        content = input('Specify the contents of the homework. ')
        path = f'subjects/{sel_subject.lower()}/{date.today()}-{title}'
        with open(path, 'w') as f:
            f.write(content)
        
def view_homework():
    print('-----------')
    print('Welcome to the View section of the Homework Function! ')
    print('-----------')
    sel_subject = input("Specify what subject's homework you want to view. ")
    path = f'subjects/{sel_subject.lower()}'
    files = os.listdir(path)
    for file in files:
        print(file)
    homework_sel = input('Specify which homework you want to view. ')
    
    path = path + '/' + homework_sel
    
    with open(path, 'r') as f:
        for line in f.read().splitlines():
            print('\n')
            print(line)
            
def remove_homework():
    print('-----------')
    print('Welcome to the Remove Homework section of the Homework function!')
    print('-----------')
    sel_subject = input("Specify which subject's homework you want to remove. ")
    path = f'subjects/{sel_subject.lower()}'
    files = os.listdir(path)
    for file in files:
        print(file)
    sel_homework = input('Specify which homework you want to remove. ')
    os.remove(f'{path}/{sel_homework}')
    
            
def add_subject():
    print('-----------')
    print('Welcome to the Add Subject section of the Homework function!')
    print('-----------')
    subject = input('Specify the subject you want to add to my database. ')
    with open('subjects.txt', 'a') as f:
        f.write(f'{subject}\n')


def remove_subject():
    print('-----------')
    print('Welcome to the Remove Subject section of the Homework function. ')
    print('-----------')
    for folder in os.listdir('subjects'):
        print(folder)
    sel_subject = input('Specify the subject you want to remove. ')
    path = f'subjects/{sel_subject}'
    os.removedirs(path)

def list_all_homework():
    print('-----------')
    with open('subjects.txt', 'r') as f:
        for subject in f.read().splitlines():
            path = f'subjects/{subject.lower()}'
            for homework in os.listdir(path):
                print(f'{subject}: {homework}')
    print('-----------')
    
def homework():
    print('-----------')
    print('Welcome to the Homework function of the SchoolTool!')
    print('-----------')
    print('Select one of the options stated: ')
    print('1. Add homework')
    print('2. View homework')
    print('3. Remove homework')
    print('4. Add a Subject')
    print('5. Remove a Subject')
    print('6. List all Homework')
    selection = int(input())
    if selection == 1:
        add_homework()
        
    if selection == 2:
        view_homework()
        
    if selection == 3:
        remove_homework()

    if selection == 4:
        add_subject()
    
    if selection == 5:
        remove_subject()
    
    if selection == 6:
        list_all_homework()

def exams():
    print('-----------')
    print('Welcome to the Exams part of the SchoolTool! ')
    print('-----------')
    print('1. Add Exams')
    print('2. View Exams')
    print('3. Remove Exams')
    print('4. List all Exams')
    selection = int(input('Specify one of the options. '))
    print('-----------')
    def add_exams():
        with open('subjects.txt', 'r') as f:
            for subject in f.read().splitlines():
                path = 'exams/' + subject.lower()
                try:
                    os.makedirs(path)
                except:
                    continue
        subject = input('Specify for which subject you want to add an exam for. ')
        title = input('Specify the title of the exam. ')
        date = input('Specify the date the exam is on. ')
        notes = input('Specify any notes for the exam. ')
        path = f'exams/{subject.lower()}/{date}'
        with open(path, 'w') as f:
            f.write(title + '\n')
            f.write(notes)
    def view_exams():
        sel_subject = input('Specify which subject you want to view exams for. ')
        path = f'exams/{sel_subject.lower()}'
        files = os.listdir(path)
        for file in files:
            print(file)
        sel_exam = input('Specify which exam you want to view. ')
        path = f'{path}/{sel_exam}'
        with open(path, 'r') as f:
            print('-----------')
            print(f'Date: {os.path.basename(path)}\n')
            for line in f.read().splitlines():
                print(line)
            print('-----------')
    def remove_exams():
        sel_subject = input('Specify which subject you want to remove exams for. ')
        path = f'exams/{sel_subject.lower()}'
        for exam in os.listdir(path):
            print(exam)
        sel_exam = input('Specify which exam you would like me to remove. ')
        path = f'{path}/{sel_exam.lower()}'
        os.remove(path)
        
    def list_all_exams():
        with open('subjects.txt', 'r') as f:
            for subject in f.read().splitlines():
                path = f'exams/{subject.lower()}'
                for exam in os.listdir(path):
                    print(f'{subject}: {exam}')
        print('-----------')
    if selection == 1:
        add_exams()
    
    if selection == 2:
        view_exams()
    
    if selection == 3:
        remove_exams()
    
    if selection == 4:
        list_all_exams()
        
        
def resources():
    print('-----------')
    print('Welcome to the Resources function of the SchoolTool! ')
    print('-----------')
    
    print('1. E-Dnevnik Ocjene ')
    print('2. Izzi Digital')
    print('3. E-sfera')
    print('4. Microsoft Office 365')
    
    selection = int(input('Select one of the resources provided. '))
    
    if selection == 1:
        url = 'https://ocjene.skole.hr'
        if sys.platform == 'win32':
            os.startfile(url)
        else:
            subprocess.Popen(['xdg-open', url])
    
if selection == 1:
    homework()
    
if selection == 2:
    exams()
    
if selection == 3:
    resources()