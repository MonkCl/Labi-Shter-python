
# 28.02.18
rub = 1
dollar = 56.3
euro = 68.67
yen = 0.52
v = [rub, dollar, euro, yen]
t = ['в рублях', 'в долларах', 'в евро', 'в йенах']


def convert(money, ind):
    return [t[ind], str(round(money / v[ind], 3))]
