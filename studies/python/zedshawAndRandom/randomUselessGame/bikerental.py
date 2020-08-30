import datetime

class BikeRental:

    def __init__(self, stock = 0):
        self.stock = stock

    def displaystock(self):
        print("We have currently {} bikes to rent".format(self.stock))
        return self.stock

    def RentBikeOnHourlyBasis(self, n):
        if n <= 0:
            print("Number of bikes should be positive.")
            return None

        elif n > self.stock:
            print("We currently have {} bikes available to rent".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} no. of bike on hourly basis"
                  "today at {} hours.".format(n, now.hour))
            print("You will be charged Php 50 for each hour per bike.")

            self.stock -= n

            return now


    def RentBikeOnDailyBasis(self, n):
        if n <= 0:
            print("Number of bikes should be positive.")
            return None

        elif n > self.stock:
            print("We currently have {} bikes available to rent".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} no. of bike on daily basis"
                  "today at {} hours.".format(n, now.hour))
            print("You will be charged Php 150 for each hour per bike.")

            self.stock -= n
            return now


    def RentBikeOnWeeklyBasis(self, n):
        if n <= 0:
            print("Number of bikes should be positive.")
            return None

        elif n > self.stock:
            print("We currently have {} bikes available to rent".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} no. of bike on weekly basis"
                  "today at {} hours.".format(n, now.hour))
            print("You will be charged Php 675 for each hour per bike.")

            self.stock -= n

            return now

    def return_bike(self, request):

        rentalTime,  rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600, 2) * 50 * numOfBikes

            elif rentalBasis == 2:
                bill = round(rentalPeriod.days, 2) * 150 * numOfBikes

            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7, 2) * 675 * numOfBikes

            if (3 <= numOfBikes <= 5):
                print("You are eligible for Family discount of 30%")
                bill = round(bill * 0.7, 2)

            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be Php {}".format(bill))
            return bill

        else:
            print("Are you sure you rented a bike with us?")
            return None


class Customer:

    def __init__(self):
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        bikes = input("How many bikes would you like to rent?")

        try:
            bikes = int(bikes)
        except ValueError:
            print("Please input a number.")
            return -1

        if bikes < 1:
            print("Invalid input")
            return -1
        else:
            self.bikes = bikes

        return self.bikes

    def returnBike(self):
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes

        else:
            return 0, 0, 0

