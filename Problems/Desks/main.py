room_1 = int(input())
room_2 = int(input())
room_3 = int(input())

desks_1 = room_1 // 2 + room_1 % 2
desks_2 = room_2 // 2 + room_2 % 2
desks_3 = room_3 // 2 + room_3 % 2

print(desks_1 + desks_2 + desks_3)