import typer
import csv
from faker import Faker
from src.model.bookings import Booking

BOOKING_CSV_FILE = "booking.csv"

app = typer.Typer()


@app.command()
def booking_csv_gen():
    with open(file=BOOKING_CSV_FILE, mode="w", newline="") as csv_file:
        fieldnames = Booking().model_dump().keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        faker = Faker()
        booking = Booking(
            firstname=faker.first_name(),
            lastname=faker.last_name(),
            totalprice=faker.random_int(min=1, max=10000, step=1),
            depositpaid=faker.boolean(chance_of_getting_true=50),
            additionalneeds=faker.paragraph(),
        )
        writer.writerow(booking.model_dump())


@app.command()
def booking_csv_read():
    pass


if __name__ == "__main__":
    app()
