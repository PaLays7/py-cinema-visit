# write your imports here
from app.cinema import bar, hall
from app.people import cinema_staff, customer

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    bar.CinemaBar()
    hall.CinemaHall(hall_number)
    customer.Customer(customers[0], customers[1])
    cinema_staff.Cleaner(cleaner)