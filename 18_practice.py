numder_tickets = int(input('Введите количество билетов: '))
ticket_price = 0
for i in range(number_ticeks):
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

if number_tickets > 3:
    ticket_price *= 0.9

print('Сумма к оплате: ', ticket_price)
