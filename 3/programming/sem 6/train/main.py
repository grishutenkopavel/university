# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 1

"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы: 

1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.

2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

3. Посчитайте долю (процент) погибших на параходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром survival;
2) полом человека и параметром survival;
3) классом, в котором пассажир ехал, и параметром survival.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?


Для вычисления 3, 4, 5, 6, 7, 8 используйте тип данных float с точностью два знака в дробной части. 


"""

import pandas  # импортирование библиотеки для считывания данных

# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pandas.read_csv('train.csv', index_col="PassengerId")


# TODO #1
def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """

    n_male, n_female = 0, 0

    for sex in data['Sex']:
        if sex == 'male':
            n_male += 1
        else:
            n_female += 1

    return n_male, n_female


# TODO #2
def get_port_distrib(data):
    """  
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """

    port_S, port_C, port_Q = 0, 0, 0

    for port in data['Embarked']:
        if port == 'S':
            port_S += 1
        if port == 'C':
            port_C += 1
        if port == 'Q':
            port_Q += 1

    return port_S, port_C, port_Q


# TODO #3
def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """

    n_died, perc_died = 0, 0

    for survived in data['Survived']:
        if survived == 0:
            n_died += 1
    perc_died = n_died * 100 / len(data) 
    return n_died, perc_died


# TODO #4
def get_class_distrib(data):
    """
    4. Какише доли составляли пассажиры первого, второго, третьего класса?    
    """
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = 0, 0, 0

    for pcls in data['Pclass']:
        if pcls == 1:
            n_pas_f_cl += 1
        elif pcls == 2:
            n_pas_s_cl += 1
        elif pcls == 3:
            n_pas_t_cl += 1
    
    numOfPassengers = len(data)
    n_pas_f_cl = n_pas_f_cl * 100 / numOfPassengers
    n_pas_s_cl = n_pas_s_cl * 100 / numOfPassengers
    n_pas_t_cl = n_pas_t_cl * 100 / numOfPassengers

    return n_pas_f_cl, n_pas_s_cl, n_pas_t_cl


# TODO #5
def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """

    corr_val = -1
    corr_val = corr_val = data['SibSp'].corr(data['Parch'])

    return corr_val


# TODO #6-1
def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - возрастом и параметром survival;

    """

    corr_val = -1
    corr_val = data['Age'].corr(data['Survived'])

    return corr_val


# TODO #6-2
def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - полом человека и параметром survival;
    """
    #do list
    corr_val = -1
    corr_val = data['Survived'].corr(data['Survived'])
    
    return corr_val

print(find_corr_sex_survival(data))
# TODO #6-3
def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - классом, в котором пассажир ехал, и параметром survival.
    """

    return data["Pclass"].corr(data["Survived"])


# TODO #7
def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """

    mean = round(data["Age"].mean(), N_DIGITS_FLOAT)
    median = round(data["Age"].median(), N_DIGITS_FLOAT)

    return mean, median


# TODO #8
def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """

    mean = round(data["Fare"].mean(), N_DIGITS_FLOAT)
    median = round(data["Fare"].median(), N_DIGITS_FLOAT)

    return mean, median


# TODO #9
def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """
    isMale = data["Sex"] == "male"
    return data[isMale].mode().at[0, "Name"]


# TODO #10
def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
    ageMore15 = data["Age"] > 15
    isMale = data["Sex"] == "male"
    isFemale = data["Sex"] == "female"

    maleName = data[ageMore15 & isMale].mode().at[0, "Name"]
    femaleName = data[ageMore15 & isFemale].mode().at[0, "Name"]

    return maleName, femaleName


# ------------------------------

# Реализуем вычисление количества пассажиров на параходе и опишем предварительные действия с данными (считывание)

# После загрузки данных с помощью метода read_csv и индексации его по первому столбцу данных (PassangerId) становится доступно выборка данных по индексу. 
# С помощью запроса ниже мы можем получить имя сотого пассажира

#print(type(data.iloc[100]))
print(data.iloc[100]['Sex'])

print(len(data))

def get_number_of_pass(data_file):
    """
        Подсчет количества пассажиров. 
        data_file - str
        В качестве аргумента удобнее всего использовать строковую переменную, куда будет передаваться название файла (т. к. далее, возможно, потребуется подсчитать параметры для другого набора данных test.csv)
    """
    male_int, female_int = 0, 0
    # считывание и обработка данных
    data = pandas.read_csv(data_file, index_col="PassengerId")

    # считать данных из столбца возможно с помощью метода value_counts()
    res = data['Sex'].value_counts()
    # res будет содержать ассоциативный массив, ключами в котором являются значения столбца sex, а целочисленные значениями - количества пассажиров обоих полов
    male_int, female_int = res['male'], res['female']
    return male_int, female_int


def test_get_number_of_pass():
    assert get_number_of_pass('train.csv') == (577,314), " Количество мужчин и женщин на Титанике"


# аналогично протестировать остальные функции