regular_guests = set()
VIP_guests = set()

num_of_guests = int(input())

for _ in range(num_of_guests):
    reservation_code = input()
    if reservation_code[0].isdigit():
        VIP_guests.add(reservation_code)
    else:
        regular_guests.add(reservation_code)

coming_guest = input()

while not coming_guest == "END":

    if coming_guest in VIP_guests:
        VIP_guests.remove(coming_guest)
    elif coming_guest in regular_guests:
        regular_guests.remove(coming_guest)

    coming_guest = input()

not_arrived_guests = len(VIP_guests) + len(regular_guests)
print(not_arrived_guests)

for reservation_code in sorted(VIP_guests):
    print(reservation_code)
for reservation_code in sorted(regular_guests):
    print(reservation_code)
