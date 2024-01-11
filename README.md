# E-Perpus
The Electronic Perpus or E-Library application developed with Python Django is designed for administrative purposes. It provides a user-friendly interface that allows the admin to manage the library's digital collection and handle reservations.

## Requipment & Install

`
Requires Python version 3.10
`
`
django-widget-tweaks
`
`
djangorestframework
`
`
xhtml2pdf
`
`
django-static
`
`
django-cors-headers 
`
`
django-import-export 
`
`
eventlet
`
`
whitenoise
`

Install Django
```
pip install Django
```
or you can use pipenv
```
pip install pipenv
```
after install pipenv (pip environment), you can run:
```
pipenv install
```
after that, run:
```
pipenv shell
```
don't forget to setting DB and Secret Key.
Next, you can run using:
```
python3 manage.py runserver [your_ip]:[your_port]
```
or you can using gunicorn:
```
gunicorn eperpus.wsgi:application --bind [your_ip]:[your_port] --workers [number] --threads [number] --worker-connections [number] --max-requests [number] --max-requests-jitter [number] --timeout [number]
```
is optional:
`
threads
`
`
 worker-connections
`
`
 max-requests
`
`
 max-requests-jitter
`
`
 timeout 
`

## Page Login
![image](https://github.com/Rahmn-Dev/E-Perpus/assets/66931894/82eb484b-d67b-45d0-9643-e311074989bf)
This login page only for admin.

## Page Dashboard
![image](https://github.com/Rahmn-Dev/E-Perpus/assets/66931894/253f4730-3f41-41b5-80de-2c7a2479453e)
The application provides an interactive dashboard where the admin can access various administrative functions.

## Page borrower of books
![image](https://github.com/Rahmn-Dev/E-Perpus/assets/66931894/6e291422-a9a0-42f8-9878-7cc641e57373)
Once users are registered, they can reserve books through their accounts. The admin can view and manage these reservations, approving or denying them based on availability.

## Page Student List
![image](https://github.com/Rahmn-Dev/E-Perpus/assets/66931894/5f78e8b2-5e51-42df-83c7-ad5c4e31756b)
The admin has the ability to add and manage user accounts for the library system. This includes registering new users, updating user information, and managing user roles and permissions.

## Page Books
![image](https://github.com/Rahmn-Dev/E-Perpus/assets/66931894/4f6fce42-135d-4647-8c9e-5fa47ac177f4)
The admin can add, edit, and delete books from the digital collection. Each book entry includes details such as title, author, genre, and availability status.

## Example Modals
![image](https://github.com/Rahmn-Dev/E-Perpus/assets/66931894/4fed5d48-d873-48a4-a8b5-e28292c0f23e)

## Future Development 
In the next phase of development, the application will be enhanced to incorporate user reservation functionality. Users will be able to create accounts, search for available books, and make reservations through the system. The admin will then manage these reservations, approve or deny them based on availability, and notify users of the status of their requests.


