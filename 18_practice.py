numder_tickets = int(input('Введите количество билетов: '))
ticket_price = 0
while numder_tickets != 0:
    age = int(input('Введите возраст посетителя: '))
    if age < 1:
        print('Вы ввели неверный возраст. Попробуйте еще раз: ')
        continue
    elif age < 18:
        break
    elif 18 <= age <= 25:
        ticket_price += 990
    elif 25 < age <= 100:
        ticket_price += 1390
    elif age > 100:
        print('Вы ввели неверный возраст. Попробуйте еще раз: ')
        continue
    numder_tickets -= 1

print('Сумма к оплате: ', ticket_price)
