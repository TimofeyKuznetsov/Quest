import time
import random
def Choice(options):#Выбор
    options=options.split(', ')
    for i in range(len(options)):
        print('> '+options[i])
    while 1!=0:
        choice,yes_or_no=input('Номер вашего варианта: '),0
        for i in range(len(options)):
            if str(i+1)==choice:
                choice,yes_or_no=int(choice),1
                break
        if yes_or_no:
            break
    return choice
def Ending(option1,option2):#Окончание глагола в зависимости от числа
    if quantity==1:
        return option1#Единственное число
    else:
        return option2#Множетвенное число или уважительное обращение
def DopOutput(output,i):
    print(output[i],end='')
def Output(output):#Вывод который в будующем хочу выполнять по буквам
    output=list(output)
    for i in range(0,len(output),2):
        time.sleep(0.1)
        DopOutput(output,i)
    print(output)
#appeal=''
#while 1!=0:
#    appeal=input('Как к вам обращаться? На ты или на Вы? ').lower()
#if appeal=='ты':
#    quantity=1
#        break
#    elif appeal=='вы':
#        while 1!=0:
#            attitude=input('Множественное число или уважительное обращение? ').lower()
#            if attitude=='уважительное обращение' or attitude=='множественное число':
#                if attitude=='уважительное обращение':
#                    appeal='Вы'
#                break
#        quantity=2
#        break
appeal='ты'
quantity=1
Output(f'В будующем {appeal} заинтересовал{Ending("ся","ись")} физикой, особенно теорией о параллельных вселенных. Наконец, через несколько лет {appeal} смог{Ending("","ли")} открыть портал в одну из них. К сожалению как только {appeal} вош{Ending("ёл","ли")} в него {appeal} почуствовал{Ending("","и")} боль в затылке и провалились в темноту. Проснул{Ending("ся","ись")} {appeal} в комнате с решётчатой дверью.')
Choice('Попробовать открыть дверь')
Output(f'{appeal.capitalize()} выш{Ending("ел","ли")} в коридор. Слева вы видите ещё камеры заточения, идущие до конца коридора, а справа из-за угла коридора льется сонечный свет.')
if Choice('Пойти налево, Пойти направо')==1:
    if random.randint(1,2)==1:
        Output(f'Пройдя налево {appeal} вид{Ending("ишь","ите")} в камере старика.')
        if Choice('Разбудить его, Не будить')==1:
            Output(f'Он просыпается -"Кто ты такой и почему на свободе?"')
            Choice('Рассказать правду, Солгать')