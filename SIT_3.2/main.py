from jinja2 import Template
import matplotlib.pyplot as plt

def create_pict(x, y):
 #Построить линию графика, установить для нее цвет и толщину:
 line = plt.plot(x, y)
 plt.setp(line, color="blue", linewidth=2)
 # Вывести 2 оси, установить их в позицию zero:
 plt.gca().spines["left"].set_position("zero")
 plt.gca().spines["bottom"].set_position("zero")
 plt.gca().spines["top"].set_visible(False)
 plt.gca().spines["right"].set_visible(False)
 # Сохранть результат построения в файл:
 plt.savefig("pict.jpg")
 # Вернуть имя созданного файла
 return "pict.jpg"

def func(x):
    a=x*3 - 6*(x*x) + x + 5
    return(a)
def Zadanie1():
    x_list = list()
    f_list = list()
    a = -2
    b = 6
    n = 30
    h =round(((b-a)/n),1)
    x = a
    while x <= b:
        x_list.append(round(x,1))
        f_list.append(round(func(x),1))
        x += h

    # Прочитать шаблон из файла function_template.html
    f_template = open('function_template.html', 'r', encoding='utf-8-sig')
    html = f_template.read()
    f_template.close()

    # Создать объект-шаблон
    template = Template(html)
    # Указать, что в шаблоне будет использована функция len
    template.globals["len"] = len
    # Cоздадать файл для HTML-страницы
    f = open('function.html', 'w', encoding='utf-8-sig')
    # Сгенерировать страницу на основе шаблона

    name_pict = create_pict(x_list, f_list)

    result_html = template.render(x=x_list, y=f_list, len=len, pict=name_pict)
    # Вывести сгенерированную страницу в файл
    f.write(result_html)
    f.close()
#Zadanie1()

def f_x(x, n_var):
    if n_var == 0:
        y = x ** 3 - 6 * x ** 2 + x + 5
    elif n_var == 1:
        y = x ** 2 -5 * x +1
    elif n_var == 2:
        y = 1 / (x ** 2 + 1)
    return (y)
def Zadanie2():
    n_var = 0
    list_name_f = ["f(x)", "y(x)", "z(x)"]
    list_name_f_long=["f(x)=x^3 - 6x^2 + x + 5", "y(x) = x^2 - 5x + 1 ", "z(x) = 1 / (x^2 + 1)"]
    x_list = list()
    f_list = list()
    a = -2
    b = 6
    n = 30
    h =round(((b-a)/n),1)
    x = a
    while x <= b:
        x_list.append(round(x,1))
        f_list.append(round(f_x(x,n_var),2))
        x += h

    count_f = len(list_name_f)

    # Прочитать шаблон из файла function_template.html
    f_template = open('functions_template2.html', 'r', encoding='utf-8-sig')
    html = f_template.read()
    f_template.close()

    # Создать объект-шаблон
    template = Template(html)
    # Указать, что в шаблоне будет использована функция len
    template.globals["len"] = len
    # Cоздадать файл для HTML-страницы
    f = open('function2.html', 'w', encoding='utf-8-sig')
    # Сгенерировать страницу на основе шаблона

    name_pict = create_pict(x_list, f_list)


    result_html = template.render(list_f=list_name_f, count_f= count_f, x=x_list,
                                  y=f_list, len=len, pict=name_pict,a=a,b=b,n=n,
                                  name_f=list_name_f_long, n_var=n_var)
    # Вывести сгенерированную страницу в файл
    f.write(result_html)
    f.close()
Zadanie2()