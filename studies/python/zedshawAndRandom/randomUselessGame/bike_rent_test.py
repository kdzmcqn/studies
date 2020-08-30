import unittest
from datetime import datetime, timedelta
from bikerental import BikeRental, Customer

class BikeRentalTest(unittest.TestCase):

    def test_Bike_Rental_Displays_correct_stock(self):
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEqual(shop1.displaystock(), 0)
        self.assertEqual(shop2.displaystock(), 10)

    def test_noneganum_hourlybasis(self):
        shop = BikeRental(10)
        self.assertEqual(shop.RentBikeOnHourlyBasis(-1), None)

    def test_nozeronum_hourlybasis(self):
        shop = BikeRental(10)
        self.assertEqual(shop.RentBikeOnHourlyBasis(0), None)

    def test_validnoofBikes_hourlybasis(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.RentBikeOnHourlyBasis(2).hour, hour)

    def test_invalidnoofbikes_hourlybasis(self):
        shop = BikeRental(10)
        self.assertEqual(shop.RentBikeOnHourlyBasis(11), None)


    def test_noneganum_dailybasis(self):
        shop = BikeRental(10)
        self.assertEqual(shop.RentBikeOnDailyBasis(-1), None)

    def test_nozeronum_dailybasis(self):
        shop = BikeRental(10)
        self.assertEqual(shop.RentBikeOnDailyBasis(0), None)

    def test_validnoofBikes_dailybasis(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.RentBikeOnDailyBasis(2).hour, hour)

    def test_invalidnoofbikes_dailybasis(self):
        shop = BikeRental(10)
        self.assertEqual(shop.RentBikeOnDailyBasis(11), None)


    def test_noneganum_Weeklybasis(self):
        shop = BikeRental(10)
        self.assertEqual(shop.RentBikeOnWeeklyBasis(-1), None)

    def test_nozeronum_Weeklybasis(self):
        shop = BikeRental(10)
        self.assertEqual(shop.RentBikeOnWeeklyBasis(0), None)

    def test_validnoofBikes_Weeklybasis(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.RentBikeOnWeeklyBasis(2).hour, hour)

    def test_invalidnoofbikes_Weeklybasis(self):
        shop = BikeRental(10)
        self.assertEqual(shop.RentBikeOnWeeklyBasis(11), None)


    def test_returnBike_for_valid_rentalTime(self):
        shop = BikeRental(10)
        customer = Customer()

        request = customer.returnBike()
        self.assertIsNone(shop.return_bike(request))

        self.assertIsNone(shop.return_bike((0,0,0)))


    def test_returnBike_for_invalid_rentalBasis(self):
        shop = BikeRental(10)
        customer = Customer()

        customer.rentalTime = datetime.now()
        customer.bikes = 3
        customer.rentalBasis = 7

        request = customer.returnBike()
        self.assertEqual(shop.return_bike(request), 0)

    def test_returnBike_for_invalidNoOfBikes(self):
        shop = BikeRental(10)
        customer = Customer()

        customer.rentalTime = datetime.now()
        customer.rentalBasis = 1

        customer.bikes = 0
        request = customer.returnBike()
        self.assertIsNone(shop.return_bike(request))


    def test_returnBike_for_valid_credentials(self):
        shop = BikeRental(50)
        customer1 = Customer()
        customer2 = Customer()
        customer3 = Customer()
        customer4 = Customer()
        customer5 = Customer()
        customer6 = Customer()



        customer1.rentalBasis = 1 # hourly
        customer2.rentalBasis = 1  # hourly
        customer3.rentalBasis = 2  # daily
        customer4.rentalBasis = 2 # daily
        customer5.rentalBasis = 3  # weekly
        customer6.rentalBasis = 3 # weekly


        customer1.bikes = 1
        customer2.bikes = 5
        customer3.bikes = 2
        customer4.bikes = 8
        customer5.bikes = 12
        customer6.bikes = 20


        customer1.rentalTime = datetime.now() + timedelta(hours=-4)
        customer2.rentalTime = datetime.now() + timedelta(hours=-23)
        customer3.rentalTime = datetime.now() + timedelta(days=-4)
        customer4.rentalTime = datetime.now() + timedelta(days=-13)
        customer5.rentalTime = datetime.now() + timedelta(weeks=-6)
        customer6.rentalTime = datetime.now() + timedelta(weeks=-12)


        request1 = customer1.returnBike()
        request2 = customer2.returnBike()
        request3 = customer3.returnBike()
        request4 = customer4.returnBike()
        request5 = customer5.returnBike()
        request6 = customer6.returnBike()

        self.assertEqual(shop.return_bike(request1), 200)
        self.assertEqual(shop.return_bike(request2), 4025)
        self.assertEqual(shop.return_bike(request3), 1200)
        self.assertEqual(shop.return_bike(request4), 15600)
        self.assertEqual(shop.return_bike(request5), 48600)
        self.assertEqual(shop.return_bike(request6), 162000)



class CustumerTest(unittest.TestCase):

    def test_return_Bike_with_valid_input(self):
        customer = Customer()
        now = datetime.now()
        customer.rentalTime = now
        customer.rentalBasis = 1
        customer.bikes = 4

        self.assertEqual(customer.returnBike(), (now, 1, 4))

    def test_return_Bike_with_invalid_input(self):
        customer = Customer()
        customer.rentalBasis = 1
        customer.bikes = 0
        customer.rentalTime = 0
        self.assertEqual(customer.returnBike(), (0, 0, 0))


if __name__ == '__main__':
    unittest.main()
