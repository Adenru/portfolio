import os

try:
    os.remove('README.MD')
except: pass



directories = next(os.walk('.'))[1]

final='''# Специалист по Data Science
репозиторий проектов для Яндекс.Практикум

| Название проекта | Описание | Используемые библиотеки | 
| :---------------------- | :---------------------- | :---------------------- |'''

for directory in directories:
    readme = open(directory+'\README.MD', 'r')
    text = readme.read().split('\n')
    readme.close()
    
    name = '**' + text[0][:-1] + '**'
    description = text[2][6:-1].lower()
    libraries = '*' + text[4][12:] + '*'



    final += f'\n| [{name}]({directory}) | {description} | {libraries} |'



savefile = open('README.MD','w+')
savefile.write(final)
savefile.close





