rooms={
    101:"available",
    102:"available",
    103:"available",
    104:"available",
    105:"available",
    106:"available",
    107:"available",
    108:"available",
    109:"available",
    110:"available",
}
customer={}
def show_rooms():
    print("------------room status-------------")
    for room in rooms:
        print('Room',room ,':',rooms[room])
def book_rooms():
    print("------------book status-------------")
    room=int(input("Enter room number:"))
    if room  in rooms:
        name = (input("Enter customer name:"))
        rooms[room] = "booked"
        customer[room] = name
        print("booked successfully")
    else:
        print("Invalid room number")

def view_bookings():
    print("------------booked status-------------:")
    if len(customer)==0:
        print("No bookings available")
    else:
        for room in customer:
            print('room',room,':',customer[room])
def update_bookings():
    print("-------------update booking status-------------:")
    room=int(input("Enter room number to update:"))
    if room in customer:
        new_room =int(input("Enter new room number:"))
        new_name=(input("Enter new  customer name:"))
        del customer[room]
        customer[new_room]=new_name
        print("successfully updated")
        print("updated successfully")
        print("room",new_room,":",customer[new_room])
    else:
        print("Invalid room number")
def cancel_bookings():
    print("--------------cancel booking status-------------:")
    room=int(input("Enter room number:"))
    if room in customer:
        del customer[room]
        rooms[room]="canceled"
        print("cancel  successfully")
    else:
        print("Invalid room number")

while True:
    print("-----HOTEL ROOMS BOOKING SYSTEM-------")
    print("1. show rooms")
    print("2. book rooms")
    print("3. view bookings")
    print("4. update bookings")
    print("5. cancel bookings")
    print("6. exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        show_rooms()
    elif choice==2:
        book_rooms()
    elif choice==3:
        view_bookings()
    elif choice==4:
        update_bookings()
    elif choice==5:
        cancel_bookings()
        print("thank you visit again")
        break

    else:
        print("Invalid choice")





