# Smart hotel project in Django

A Django project with 7 models.

## Tech stack

- Python 3
- Django
- Database: SQLite

## Project structure

- `smart_hotel_project/`: project settings and root URLs
- `financial_app/`: Django app
- `hotel_app/`: Django app
- Tests: `financial_app/tests.py`, `hotel_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Expense` | `financial_app` | category, amount, date, description, room_expense |
| `Payment` | `financial_app` | method, reservation, date, amount |
| `Address` | `hotel_app` | streetName, city, country, ZipCode |
| `Hotel` | `hotel_app` | name, capacity, nbStars, address |
| `Room` | `hotel_app` | number, type, rate, hotel, status |
| `Guest` | `hotel_app` | cin, passportNumber, name, familyName, nationality, reservations |
| `Reservation` | `hotel_app` | guest, room, reservationDate, inDate, outDate, totalAmount, status |

## URL routes

Declared in `urls.py`:

- `/blog/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver
```

There is no `requirements.txt`; the packages above are the ones the settings and imports refer to.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
