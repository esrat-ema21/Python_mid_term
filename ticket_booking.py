class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        self.seats[id] = []
        for row in range(self.rows):
            row_data = []
            for col in range(self.cols):
                row_data.append(0)
            self.seats[id].append(row_data)

    def book_seats(self, id, seat_list):
       
        for seat in seat_list:

            row, col = seat

            if (0 <= row < self.rows) and (0 <= col < self.cols) and (self.seats[id][row][col] == 0):
               self.seats[id][row][col] =1
               print(f"Seat ({row+1}, {col+1}) booked for show {id}.")
               

            elif (0 <= row < self.rows) and (0 <= col < self.cols) and (self.seats[id][row][col] == 1):

                print(f"Seat ({row+1}, {col+1}) is already booked.")

            else:

                print(f"Error: Seat is invalid.")
                
    def view_show_list(self):
        print("  SHOW LIST:")
        print('--------------')
        for show in self.show_list:
            print(f"Show ID: {show[0]} Movie Name: {show[1]} Time: {show[2]}")
            print("--------------------------------------------------------")

    def view_available_seats(self, id):
        if id not in self.seats:
            print(f"Error: Show ID {id} does not exist.")
            return
        print('---------------------------------------')
        print(f"           Seats available:")
        print('---------------------------------------')
        print('  A = available and X = not available')
        print()
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] == 0:
                    print(f" A ",end=" ")
                else:
                    print(f" X ",end=" ")
            print("")
            print("---------------------------------------")

cineplex = Hall(10, 10, 1)

cineplex.entry_show("1", "  STREE  ", "10:00 AM")
cineplex.entry_show("2", "  JAWAN  ", "1:30 PM")
cineplex.entry_show("3", "12TH fAIL", "5:00 PM")
cineplex.entry_show("4", "  YODHA  ", "8:30 PM")


while True:
    print("**********************************")
    print(" WELCOME TO CINEPLEX CINEMA HALL")
    print("**********************************")
    print("1: VIEW TODAY'S SHOWS")
    print("2: VIEW AVAILABLE SEATS")
    print("3: BOOK TICKET")
    print("4: EXIT")
    print()
    option = int(input("ENTER OPTION: "))#input in intiger

    if option == 1:
        print('---------------')
        cineplex.view_show_list()
        
        
    elif option == 2:
        print('---------------')
        show_id = input("ENTER SHOW ID:")
        cineplex.view_available_seats(show_id)
        
        
    elif option == 3:
        print('--------------')
        show_id = input("ENTER SHOW ID: ")
        print('--------------')
        num_seats = int(input("NUMBER OF TICKETS: "))
        seat_list = []
        for seat in range(num_seats):
            row = int(input("ENTER SEAT ROW NO : "))
            col = int(input("ENTER SEAT COL NO : "))
            seat_list.append((row-1, col-1))#adjust row and col
        cineplex.book_seats(show_id, seat_list)
       
    elif option == 4:
        break