#5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

q = int(input("Здравствуйте! Сколько продуктов желаете добавить в систему?\n\t Кол-во: "))
chr = "Название", "Цена", "Количество", "Ед.изм"
products, names, prices, quantity, uoms = [], [], [], [], []
for i in range(q):
    print(f"Введите характеристики для товара # {i + 1} :")
    name, price, quantity, uom = input("\tНазвание : "), input("\tЦена товара : "), input("\tКоличество : "), \
                                 input("\tЕд.изм : ")
    products_up = (i + 1, {chr[0]: name, chr[1]: price, chr[2]: quantity, chr[3]: uom})
    products.append(products_up)
    names.append(products[i][1].get(chr[0]))
    prices.append(products[i][1].get(chr[1]))
    quantity.append(products[i][1].get(chr[2]))
    uoms.append(products[i][1].get(chr[3]))
analytics ={chr[0]: names, chr[1]: prices, chr[2]: Quantity, chr[3]: uoms}
print(f"Статистика по товарам ниже \n{analytics}")