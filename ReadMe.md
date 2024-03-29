# Librasic
***Simple management for simple libraries.***

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-FCA121?style=flat-square&logo=sqlalchemy&logoColor=white) ![SQLite](https://img.shields.io/badge/-SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white)

Librasic is a Python-based library management system built with Flask and SQLAlchemy. It provides a simple and efficient way to manage books, members, and transactions in a library.

<!-- todo -->
<!-- Librasic Screenshots -->

## Features

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

To run the application, execute the following command in the project directory:
```sh
python run.py
```

## Development

This project uses Flask for the web framework and SQLAlchemy for the ORM. Migrations are handled by Alembic.

## Roadmap

- **Delete Functionality**: Implement the delete function for Books and Members.
*Highest Priority*
- **Table Sorting**: Allow sorting tables by ascending or descending table headers in all tables.
*Highest Priority*
- **Table Filters**: Implement filters for table headers in all tables.
*High Priority*
- **Mobile Responsiveness**: While the webapp works just fine on smaller devices, some things are visually broken here and there that need to be fixed.
*High Priority*
- **Fee Payment Records**: Implement storing and display of fee payment records.
*Low Priority*
- **Statistics and Reports**: Generate statistics and reports on book circulation, popular genres, and member activity.
*Lowest Priority*

## Feedback, Bugs, and Issues

Something not working right? Something could be done better? Something that should be there but isn't?
Feel free to create an issue and we'll figure it out! :D

## Contributing

Contributions are welcome!
Please create a detailed issue first and proceed with the PR if and once assigned.

## License

This project is licensed under the terms of the MIT license. See the LICENSE file for details.