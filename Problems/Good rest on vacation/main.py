duration = int(input())
food = int(input())
flight = int(input())
hotel_night = int(input())

print(duration * food + 2 * flight + hotel_night * (duration - 1))
