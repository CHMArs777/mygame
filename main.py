from random import randint
import time
hp = 100
speed = 0
distance = 0
totalDistance = 400
rock = 1
yeti = 2
niger = 3
def CheckSkill(enemy, hp, speed):
    print('Влево - 1; Вправо - 2; Подпрыгнуть - 3;')
    storona = int(input('Куда повернуть?:'))
    udar = randint(1, 3)
    if storona == udar:
        hp = hp - 20
        speed = 0
        print('Ты впечатался в препятствие')
        print('ХП:', hp)
    elif (storona != 1) and (storona != 2) and (storona != 3):
        print('Ты сделал неудачную сальтуху')
        hp = hp - 20
        speed = 0
    else:
        print('Ты увернулся. Красавчик!')
while True:
    if hp <= 0:
        print("ПОТРАЧЕНО")
        break
    if distance >= totalDistance:
        print("ЛЕГЧАЙШЕ")
        break
    speed = speed + 1
    print(speed, " скорость")
    distance = distance + speed
    print(distance, " дистанция")
    time.sleep(0.5)
    chance = randint(1,3)
    if chance == yeti:
        print('Ты попался на ЙЕТИ!')
        CheckSkill(yeti, hp, speed)
    if chance == rock:
        print('Its ROOOOOCK!')
        CheckSkill(rock, hp, speed)
    if chance == niger:
        print('niger niger niger')
        CheckSkill(yeti, hp, speed)
