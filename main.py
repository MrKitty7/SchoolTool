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

if os.path.isdir('exams') == False:
        os.makedirs('exams')
        print("LOG: Created folder 'exams'.")
            
if os.path.isdir('subjects') == False:
        os.makedirs('subjects')
        print("LOG: Created folder 'subjects'.")
            
if os.path.isdir('resources') == False:
        os.makedirs('resources')
        print("LOG: Created folder 'resources'.")
            


def add_homework():
    with open('subjects.txt', 'r') as f:
        for subject in f.read().splitlines():
            path = 'subjects/' + subject.lower()
            # Creates folders for each subject
            os.makedirs(path)
        sel_subject = input('Specify which subject you would like me to add homework to. ')
        title = input('Specify the title of the homework. ')
        content = input('Specify the contents of the homework. ')
        path = f'subjects/{sel_subject.lower()}/{date.today()}-{title}'
        with open(path, 'w') as f:
            f.write(content)
        
        print('LOG: Done adding homework.')
        
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
    
    print('LOG: Done viewing homework. ')
            
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
    
    print('LOG: Done removing homework. ')
    
            
def add_subject():
    print('-----------')
    print('Welcome to the Add Subject section of the Homework function!')
    print('-----------')
    subject = input('Specify the subject you want to add to my database. ')
    with open('subjects.txt', 'a') as f:
        f.write(f'{subject}\n')

    print('LOG: Done adding subject. ')

def remove_subject():
    print('-----------')
    print('Welcome to the Remove Subject section of the Homework function. ')
    print('-----------')
    for folder in os.listdir('subjects'):
        print(folder)
    sel_subject = input('Specify the subject you want to remove. ')
    path = f'subjects/{sel_subject}'
    os.removedirs(path)
    
    print('LOG: Done removing subject. ')

def list_all_homework():
    print('-----------')
    with open('subjects.txt', 'r') as f:
        for subject in f.read().splitlines():
            path = f'subjects/{subject.lower()}'
            for homework in os.listdir(path):
                print(f'{subject}: {homework}')
    print('-----------')
    print('LOG: Done listing all homework. ')
    
def homework():
    if os.path.isdir('subjects') == False:
            os.makedirs('subjects')
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
        if os.path.isdir('exams') == False:
            os.makedirs('exams')
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
            
        print('LOG: Done adding exams. ')
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
            print('LOG: Done adding exams. ')
            
    def remove_exams():
        sel_subject = input('Specify which subject you want to remove exams for. ')
        path = f'exams/{sel_subject.lower()}'
        for exam in os.listdir(path):
            print(exam)
        sel_exam = input('Specify which exam you would like me to remove. ')
        path = f'{path}/{sel_exam.lower()}'
        os.remove(path)
        print('LOG: Done removing exams. ')
        
    def list_all_exams():
        with open('subjects.txt', 'r') as f:
            for subject in f.read().splitlines():
                path = f'exams/{subject.lower()}'
                for exam in os.listdir(path):
                    print(f'{subject}: {exam}')
        print('-----------')
        print('LOG: Done listing all exams. ')
        
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
    
    print('1. Add a new resource. ')
    print('2. Open resources. ')
    
    selection = int(input('Select one of the resources provided. '))
    
    def add_resources():
        if os.path.isdir('resources') == False:
            os.makedirs('resources')
            
        resource_name = input('Specify the name of the resource you want to add. ')
        resource_url = input('Specify the url to the resource. ')
        path = f'resources/{resource_name}'
        
        with open(path, 'w') as f:
            f.write(resource_url)

        print('LOG: Done adding resources. ')
        
    def open_resources():
        print('-----------')
        path = 'resources'
        for line in os.listdir(path):
            print(line)
        print('-----------')
        sel_resource = input('Specify which resource you want to open. ')
        path = f'resources/{sel_resource}'
        with open(path, 'r') as f:
            url = f.read()
            
        os.startfile(url)

        print('LOG: Done opening resources. ')
    
    if selection == 1:
        add_resources()
    
    if selection == 2:
        open_resources()
    
if selection == 1:
    homework()
    
if selection == 2:
    exams()
    
if selection == 3:
    resources()