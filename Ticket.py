
summa = 0
kol_vo = input('Сколько билетов вы хотите приобрести на мероприятие? ')
kol_vo = int(kol_vo)
for i in range(kol_vo):
    i += 1
    years_ticket = input(f'Введите возраст посетителя для билета №{i}? ')
    years_ticket = int(years_ticket)
    if years_ticket < 18:
             print('Билет бесплатный')
    elif 25 > years_ticket >= 18:
            summa += 990
            print('Стои мость билета: 990 руб.')
    else:
            summa += 1390
            print('Стоимость билета: 1390 руб.')
if kol_vo > 3:
    summa = summa - ((summa / 100) * 10)
    print(f'Сумма к оплате {summa} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3-х человек')
else:
    print(f'Сумма к оплате {summa} руб.')