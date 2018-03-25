import account
import converter


def main():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    period = int(input("Введите период ведения счета в месяцах: "))

    result = account.calculate_income(rate, money, period)
    for i in range(len(converter.v)):
        a = converter.convert(money, i)
        b = converter.convert(result, i)
        print("Параметры счета ({0}):\n".format(a[0]), "Сумма ({0}): {1}".format(a[0], a[1]), "\n", "Ставка: ", rate,
              "\n", "Период: ", period, "\n", "Сумма на счете в конце периода ({0}): {1}".format(b[0], b[1]))


main()
