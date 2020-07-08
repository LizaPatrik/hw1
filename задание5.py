rev = int(input("Введите значение выручки"))
costs = int(input("Введите значение издержек"))
if rev < costs:
    print("Компания работает с убытком:", costs - rev)
else:
    print("Компания работает с прибылью:", rev - costs)
    rent = (rev - costs) / rev
    print("Компания работает с рентабильностью:", "{:.2f}".format(rent))
    staff = int(input("Введите количество сотрудников"))
    print("Прибыль фирмы на одного сотрудника:", "{:.0f}".format((rev - costs) / staff))