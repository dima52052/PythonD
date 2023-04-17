from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Время сейчас =", current_time )
import datetime
current_finish_time = datetime.time(20, 00, 00)
print("Время финиш =", current_finish_time)

water_glass = int(input('Введите кол-во стаканов: '))

import datetime
dt1 = now
dt2 = datetime.datetime(2023,4,12,20,00)
tdelta = dt2 - dt1
print("Всего времени =",tdelta)
p1 = now
p2 = now + tdelta/3
p3 = p2 + tdelta/3
p4 = dt2
print("P1 =",p1.time())
print("P2 =",p2.time())
print("P3 =",p3.time())
print("P4 =",p4.time())

