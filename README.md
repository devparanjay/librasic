# Librasic
***Simple management for simple libraries.***

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-FCA121?style=flat-square&logo=sqlalchemy&logoColor=white) ![SQLite](https://img.shields.io/badge/-SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white) ![Bootstrap 5](https://img.shields.io/badge/-Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white) ![Jinja](https://img.shields.io/badge/-Jinja-B41717?style=flat-square&logo=jinja&logoColor=white) ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

Librasic is a Python-based library management system built with Flask and SQLAlchemy. It provides a simple and efficient way to manage books, members, and transactions in a library.

Librasic is meant to be used by the librarian and currently supports only one user.
There might be features that support multiple users with different authority levels and such in future.
<!-- todo -->
<!-- Librasic Screenshots -->

## Features

- **Simple Authentication**: Simple basic authentication for the Librarian to use the application.
- **Manage Books**: Add, edit, and delete books. Each book has attributes like name, authors, language, publication date, publisher, ISBN, pages, rating, and more.
- **Manage Members**: Add, edit, and delete members.
- **Issue and Return Books**: Keep track of books issued and returned by members. (Issue Records / Transactions)
- **Rent Fee**: Set a custom daily book rent fee.
- **Fees Calculation**: Calculate the fees owed by a member upon Book return.
- **Fee Records**: See the total fees paid by the member, along with the current fees owed.
- **Fee Limit**: Set a maximum allowed fee limit for any member to disallow further issuance until fees is paid.
- **Easy Search**: Easily search for books and members by Name, ID, or other attributes through the sidebar.
- **Database Migrations**: Easily manage database schema changes with Flask-Migrate.
- **Frappe API Import**: Directly import books via the API by Frappe using either/any Title, ISBN, Authors, and Publisher.

## Demo Usage

- Go to the demo deployment -
https://devparanjay.pythonanywhere.com/
- Use these credentials when prompted -
    - Username:
``
demo
``
    - Password:
``
librasic
``
- Optionaly import the demo data from Github via the "Import Books" page, since PythonAnywhere does not work Frappe API.

## Installation

1. Clone the repository:
```sh
git clone https://github.com/devparanjay/librasic.git
```

2. Navigate to the project directory:
```sh
cd librasic
```

2.5 Create and activate a virtual environment (optional):
```sh
virtualenv env
```
Windows -
```sh
env/Scripts/activate
```
Linux -
```sh
source env/bin/activate
```

3. Install the required Python packages:
```sh
pip install -r requirements.txt
```

## Usage

1. Configure the variables in the librasic/librasic/envconfig.json file:
```json
{
    "LIBRARIAN_USERNAME": "uu",
    "LIBRARIAN_PASSWORD": "pp",
    "DEFAULT_RENT_FEE": 20,
    "DEFAULT_LATE_FEE": 50
}
```

To run the application, execute the following command in the project directory:
```sh
python run.py
```

## Development

This project uses Flask for the web framework and SQLAlchemy for the ORM. Migrations are handled by Alembic.

## Roadmap

- ~~**Delete Functionality**: Implement the delete function for Books and Members.
*Highest Priority*~~ ![Completed](https://img.shields.io/date/1711726543.svg?color=%2372dd77&style=flat-square&logo=calendar&label=Completed)
- **Table Sorting**: Allow sorting tables by ascending or descending table headers in all tables.
*Highest Priority*
- **Table Filters**: Implement filters for table headers in all tables.
*High Priority*
- **Mobile Responsiveness**: While the webapp works just fine on smaller devices, some things are visually broken here and there that need to be fixed.
*High Priority*
- **Better Security**: Implement better security for storing sensitive data that does not expose credentials in a simple JSON config file.
*Medium Priority*
- **Better Database**: Librasic currently uses Python's SQLite3 for its database, but it's not an idea solution. Move to PostgreSQL.
*Low Priority*
- **Better Authentication**:
Implement better authentication if it exists. Better = equaly simple but provides more security.
*Low Priority*
- **Fee Payment Records**: Implement storing and display of fee payment records.
*Low Priority*
- **Statistics and Reports**: Generate statistics and reports on book circulation, popular genres, and member activity.
*Lowest Priority*

## Screenshots

- **Dashboard**:
  ![devparanjay pythonanywhere com dashboard](https://github.com/devparanjay/librasic/assets/45117614/298ae262-38e6-4411-9a27-c134c00164d6)

- **Books**:
  ![devparanjay pythonanywhere com books](https://github.com/devparanjay/librasic/assets/45117614/d0810439-acd5-4334-9c83-8f48987efcc5)

- **Members**:
  ![devparanjay pythonanywhere com members](https://github.com/devparanjay/librasic/assets/45117614/332def78-f80c-420e-95c3-6c76eb0d7eb7)

- **Issue Records**:
  ![devparanjay pythonanywhere com issue-records](https://github.com/devparanjay/librasic/assets/45117614/b01de211-29b7-4f77-8612-82e030fab317)

- **Import Books**:
  ![devparanjay pythonanywhere com import-books](https://github.com/devparanjay/librasic/assets/45117614/937bdc6d-ca9d-4c6f-958e-a6727bf88504)

- **Fees Payment**:
  ![devparanjay pythonanywhere com fees-payment](https://github.com/devparanjay/librasic/assets/45117614/c370da8e-9c73-4fae-b14d-1e3b162b755c)

- **Search**:
  ![devparanjay pythonanywhere com search](https://github.com/devparanjay/librasic/assets/45117614/6d604f53-a3f4-4e18-a372-b610c2fd5c9a)

- **Add Book**:
  ![devparanjay pythonanywhere com add-book](https://github.com/devparanjay/librasic/assets/45117614/50256b7b-bf34-4f6f-902b-454d3f1f65f7)

- **Edit Book**:
  ![devparanjay pythonanywhere com edit-book](https://github.com/devparanjay/librasic/assets/45117614/510b574c-bd5f-4e96-8015-aa387a58c89e)

- **Add Member**:
  ![devparanjay pythonanywhere com add-member](https://github.com/devparanjay/librasic/assets/45117614/9fb86813-d312-4ff0-bdf7-c4af9e2e8593)

- **Issue Book**:
  ![devparanjay pythonanywhere com new-issue](https://github.com/devparanjay/librasic/assets/45117614/bc976f4d-5698-4ae5-afd6-779a6034408b)

- **Return Book**:
  ![devparanjay pythonanywhere com return-issued-book](https://github.com/devparanjay/librasic/assets/45117614/68f2690a-a00b-4132-9562-ee31f2e589a2)


## Feedback, Bugs, and Issues

Something not working right? Something could be done better? Something that should be there but isn't?
Feel free to create an issue and we'll figure it out! :D

## Contributing

Contributions are welcome!
Please create a detailed issue first and proceed with the PR if and once assigned.

## License

This project is licensed under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE. See the LICENSE file for details.
