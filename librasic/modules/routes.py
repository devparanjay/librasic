from datetime import datetime

import requests

from librasic import app
from librasic.imports.imports import (
    Book,
    IssueRecord,
    Member,
    db,
    issue_book_record,
    jsonify,
    make_response,
    redirect,
    render_template,
    request,
    return_book_record,
)
from librasic.modules.app_setup import reset_database
from librasic.utils import check_auth


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("dashboard.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")


@app.route("/books", methods=["GET", "POST"])
@check_auth
def show_books():
    books = Book.query.order_by(Book.b_date_added).all()
    return render_template("books.html", books=books)


@app.route("/members", methods=["GET", "POST"])
@check_auth
def show_members():
    members = Member.query.order_by(Member.m_date_added).all()
    return render_template("members.html", members=members)


@app.route("/issue-records", methods=["GET", "POST"])
@check_auth
def show_issue_records():
    issue_record = IssueRecord.query.order_by(IssueRecord.r_i_date.desc()).all()
    return render_template("issue-records.html", issue_record=issue_record)


@app.route("/reset-database", methods=["POST"])
@check_auth
def reset_db():
    reset_database()
    return "Database reset successfully", 200


@app.route("/search-page", methods=["GET", "POST"])
@check_auth
def search_page():
    return render_template("search-page.html")


@app.route("/import-books", methods=["GET", "POST"])
@check_auth
def import_books():
    return render_template("import-books.html")


@app.route("/add-new-book", methods=["GET", "POST"])
@check_auth
def add_book_form():
    return render_template("add-new-book.html")


@app.route("/new-issue", methods=["GET", "POST"])
@check_auth
def new_issue_form():
    return render_template("new-issue.html")


@app.route("/return-issued-book", methods=["GET", "POST"])
@check_auth
def return_issue_form():
    return render_template("return-book.html")


@app.route("/fees-payment", methods=["GET", "POST"])
@check_auth
def pay_fees_form():
    return render_template("fees-payment.html")


@app.route("/edit-book/<int:b_id>", methods=["GET", "POST"])
@check_auth
def edit_book_form(b_id):
    book = Book.query.get_or_404(b_id, description="Book not found!")
    return render_template("edit-book.html", b_id=b_id, book=book)


@app.route("/edit-member/<int:m_id>", methods=["GET", "POST"])
@check_auth
def edit_member_form(m_id):
    member = Member.query.get_or_404(m_id, description="Member not found!")
    return render_template("edit-member.html", m_id=m_id, member=member)


@app.route("/frappe-import", methods=["GET", "POST"])
@check_auth
def frappe_import():
    if request.method == "POST":
        api_title = request.form["book_title"]
        api_authors = request.form["book_authors"]
        api_publisher = request.form["book_publisher"]
        api_isbn = request.form["book_isbn"]
        api_pages = request.form["import_pages"]
        api_params = {}
        if api_title:
            api_params["title"] = api_title
        if api_authors:
            api_params["authors"] = api_authors
        if api_publisher:
            api_params["publisher"] = api_publisher
        if api_isbn:
            api_params["isbn"] = api_isbn
        if api_pages:
            api_params["pages"] = api_pages
        api_response = requests.get(
            "https://frappe.io/api/method/frappe-library", params=api_params
        )
        api_response_json = api_response.json()
        books_to_import = api_response_json["message"]
        print("books_to_import = \n", books_to_import)

        for book in books_to_import:
            # check if b_id already exists in the database
            if Book.query.filter_by(b_id=int(book["bookID"])).first():
                print(f"Book {int(book['bookID'])} already exists in the database.")
                continue
            # if isbn ends with X, replace X with 10
            if book["isbn"].endswith("X"):
                book["isbn"] = book["isbn"][:-1] + "10"
            # fallback date format
            try:
                b_pub_date = datetime.strptime(
                    book["publication_date"], "%d/%m/%Y"
                ).date()
            except ValueError:
                b_pub_date = datetime.strptime(
                    book["publication_date"], "%m/%d/%Y"
                ).date()

            new_book = Book(
                b_id=int(book["bookID"]),
                b_name=book["title"],
                b_t_stock=10,
                b_c_stock=10,
                b_authors=book["authors"],
                b_lang=book["language_code"],
                b_publication_date=b_pub_date,
                b_publisher=book["publisher"],
                b_isbn=int(book["isbn"]),
                b_isbn13=int(book["isbn13"]),
                b_pages=int(book["  num_pages"]),
                b_rating=float(book["average_rating"]),
                b_ratings_count=int(book["ratings_count"]),
                b_text_reviews_count=int(book["text_reviews_count"]),
            )
            try:
                db.session.add(new_book)
                db.session.commit()
            except Exception as e:
                print(f'Error adding book {int(book["bookID"])} to database: ', e)
                return f'There was an error adding the book {int(book["bookID"])} to the databse. Please check the code.'
        return redirect("/books")
    else:
        return render_template("import-books.html")


@app.route("/github-demo-import", methods=["GET", "POST"])
@check_auth
def github_demo_import():
    if request.method == "POST":
        api_response = requests.get(
            "https://github.com/devparanjay/librasic/raw/main/demo-data/frappe_data.json"
        )
        api_response_json = api_response.json()
        books_to_import = api_response_json["message"]
        print("books_to_import = \n", books_to_import)

        for book in books_to_import:
            # check if b_id already exists in the database
            if Book.query.filter_by(b_id=int(book["bookID"])).first():
                print(f"Book {int(book['bookID'])} already exists in the database.")
                continue
            # if isbn ends with X, replace X with 10
            if book["isbn"].endswith("X"):
                book["isbn"] = book["isbn"][:-1] + "10"
            # fallback date format
            try:
                b_pub_date = datetime.strptime(
                    book["publication_date"], "%d/%m/%Y"
                ).date()
            except ValueError:
                b_pub_date = datetime.strptime(
                    book["publication_date"], "%m/%d/%Y"
                ).date()

            new_book = Book(
                b_id=int(book["bookID"]),
                b_name=book["title"],
                b_t_stock=10,
                b_c_stock=10,
                b_authors=book["authors"],
                b_lang=book["language_code"],
                b_publication_date=b_pub_date,
                b_publisher=book["publisher"],
                b_isbn=int(book["isbn"]),
                b_isbn13=int(book["isbn13"]),
                b_pages=int(book["  num_pages"]),
                b_rating=float(book["average_rating"]),
                b_ratings_count=int(book["ratings_count"]),
                b_text_reviews_count=int(book["text_reviews_count"]),
            )
            try:
                db.session.add(new_book)
                db.session.commit()
            except Exception as e:
                print(f'Error adding book {int(book["bookID"])} to database: ', e)
                return f'There was an error adding the book {int(book["bookID"])} to the databse. Please check the code.'
        return redirect("/books")
    else:
        return render_template("import-books.html")


@app.route("/add-book", methods=["GET", "POST"])
@check_auth
def add_book():
    if request.method == "POST":
        b_id = request.form["book_id"]
        b_name = request.form["book_name"]
        b_t_stock = request.form["book_total_stock"]
        b_c_stock = request.form["book_current_stock"] or b_t_stock
        # b_authors = list(str(request.form['book_authors']).split('/'))
        b_authors = request.form["book_authors"]
        b_lang = request.form["book_language"]
        book_pub_date_str = request.form["book_pub_date"]
        b_publication_date = datetime.strptime(book_pub_date_str, "%d/%m/%Y").date()
        b_publisher = request.form["book_pub_name"]
        b_isbn = request.form["book_isbn"]
        b_isbn13 = request.form["book_isbn13"]
        b_pages = request.form["book_pages"]
        b_rating = request.form["book_rating"]
        b_ratings_count = request.form["book_ratings_count"]
        b_text_reviews_count = request.form["book_text_reviews_count"]

        new_book = Book(
            b_id=b_id,
            b_name=b_name,
            b_t_stock=b_t_stock,
            b_c_stock=b_c_stock,
            b_authors=b_authors,
            b_lang=b_lang,
            b_publication_date=b_publication_date,
            b_publisher=b_publisher,
            b_isbn=b_isbn,
            b_isbn13=b_isbn13,
            b_pages=b_pages,
            b_rating=b_rating,
            b_ratings_count=b_ratings_count,
            b_text_reviews_count=b_text_reviews_count,
        )

        try:
            db.session.add(new_book)
            db.session.commit()
            return redirect("/books")
        except Exception as e:
            print("Error adding book to database: ", e)
            return "There was an error adding the book to the databse. Please check the code."

    else:
        return render_template("add-new-book.html")


@app.route("/delete-book/<int:b_id>", methods=["GET", "POST"])
@check_auth
def delete_book(b_id):
    book = Book.query.get_or_404(b_id, description="Book not found!")
    try:
        db.session.delete(book)
        db.session.commit()
        return redirect("/books")
    except Exception as e:
        print("Error deleting the book: ", e)
        return "There was an error deleting the book. Please check the code."


@app.route("/add-member", methods=["GET", "POST"])
@check_auth
def add_member():
    if request.method == "POST":
        m_id = request.form["member_id"]
        m_name = request.form["member_name"]

        new_member = Member(m_id=m_id, m_name=m_name)

        try:
            db.session.add(new_member)
            db.session.commit()
            return redirect("/members")
        except Exception as e:
            return print("Error adding member to database: ", e)

    else:
        return render_template("add-new-member.html")


@app.route("/delete-member/<int:m_id>", methods=["GET", "POST"])
@check_auth
def delete_member(m_id):
    member = Member.query.get_or_404(m_id, description="Member not found!")
    try:
        db.session.delete(member)
        db.session.commit()
        return redirect("/members")
    except Exception as e:
        return print("Error deleting the member: ", e)


@app.route("/update-book/<int:b_id>", methods=["GET", "POST"])
@check_auth
def update_book(b_id):
    book = Book.query.get_or_404(b_id, description="Book not found!")
    if request.method == "POST":
        book.b_id = request.form["book_id"]
        book.b_name = request.form["book_name"]
        book.b_t_stock = request.form["book_total_stock"]
        book.b_c_stock = request.form["book_current_stock"]
        # book.b_authors = list(str(request.form['book_authors']).split('/'))
        book.b_authors = request.form["book_authors"]
        book.b_lang = request.form["book_language"]
        book_pub_date_str = request.form["book_pub_date"]
        book_pub_date_obj = datetime.strptime(
            book_pub_date_str.split(" ")[0], "%Y-%m-%d"
        )
        book.b_publication_date = book_pub_date_obj
        book.b_publisher = request.form["book_pub_name"]
        book.b_isbn = request.form["book_isbn"]
        book.b_isbn13 = request.form["book_isbn13"]
        book.b_pages = request.form["book_pages"]
        book.b_rating = request.form["book_rating"]
        book.b_ratings_count = request.form["book_ratings_count"]
        book.b_text_reviews_count = request.form["book_text_reviews_count"]

        try:
            db.session.commit()
            return redirect("/books")
        except Exception as e:
            print("Error updating the database: ", e)
            return "There was an error updating book details in the databse. Please check the code."

    else:
        return render_template("edit-book.html", book=book)


@app.route("/update-member/<int:m_id>", methods=["GET", "POST"])
@check_auth
def update_member(m_id):
    member = Member.query.get_or_404(m_id, description="Member not found!")
    if request.method == "POST":
        member.m_id = request.form["member_id"]
        member.m_name = request.form["member_name"]

        try:
            db.session.commit()
            return redirect("/members")
        except Exception as e:
            return print("Error updating the database: ", e)

    else:
        members = Member.query.order_by(Member.m_date_added).all()
        return render_template("members.html", members=members)


# todo: feature to pass multiple books so multiple books can be issued at the same time


@app.route("/issue-book", methods=["GET", "POST"])
@check_auth
def issue_book():
    m_id = request.form["member_id"]
    b_id = request.form["book_id"]
    issue_book_record(m_id=m_id, b_id=b_id)
    return redirect("/issue-records")


# todo: feature to pass multiple books so multiple books can be returned at the same time


@app.route("/return-book/<int:r_id>", methods=["GET", "POST"])
@check_auth
def return_book(r_id):
    if r_id == 0:
        r_id = request.form("issue_record_id")
    return_book = return_book_record(r_id=r_id)
    if return_book.status_code != 400:
        return redirect("/issue-records")
    else:
        return make_response(
            "There was an error returning the book. Please check the code.", 400
        )
    # return redirect('/issue-records')


# todo: move pay_fees to actors.py
@app.route("/pay-fees", methods=["GET", "POST"])
@check_auth
def pay_fees():
    m_id: int = request.form["memberId"]
    payment_amount: float = float(request.form["paymentAmount"])
    member = Member.query.get_or_404(m_id, description="Member not found!")
    total_due_fees: float = member.m_due_fees

    if payment_amount > total_due_fees:
        return make_response(
            400, {"message": "Payment amount cannot be greater than due fees."}
        )

    due_fees: float = total_due_fees - payment_amount
    member.m_due_fees = due_fees
    member.m_total_fees += payment_amount
    db.session.commit()

    return redirect("/members")


@app.route("/search-database", methods=["POST"])
@check_auth
def search_db():
    query = str(request.form.get("query"))
    search_type = str(request.form.get("search_type"))
    members = []
    books = []

    if search_type == "Books":
        books = Book.query.filter(
            Book.b_name.like("%" + query + "%")
            | Book.b_id.like("%" + query + "%")
            | Book.b_isbn.like("%" + query + "%")
            | Book.b_authors.like("%" + query + "%")
        ).all()
        books_result = []
        for book in books:
            books_result.append(
                {
                    "b_id": book.b_id,
                    "b_name": book.b_name,
                    "b_authors": book.b_authors,
                    "b_c_stock": book.b_c_stock,
                }
            )

    elif search_type == "Members":
        members = Member.query.filter(
            Member.m_name.like("%" + query + "%")
            | Member.m_id.like("%" + query + "%")
            | Member.m_date_added.like("%" + query + "%")
        ).all()
        members_result = []
        for member in members:
            books_issued: dict = dict(member.m_books_issued)
            members_result.append(
                {
                    "m_id": member.m_id,
                    "m_name": member.m_name,
                    "m_due_fees": member.m_due_fees,
                    "m_num_b_issued": sum(books_issued.values()),
                }
            )

    elif search_type == "IssueRecords":
        issue_records = IssueRecord.query.filter(
            IssueRecord.r_id.like("%" + query + "%")
            | IssueRecord.b_id.like("%" + query + "%")
            | IssueRecord.m_id.like("%" + query + "%")
        ).all()
        issue_records_result = []
        for record in issue_records:
            # m_num_books_issued: int = 0
            # for key in books_issued.keys():
            #     # key = int(key)
            #     if int(key) != 0:
            #         m_num_books_issued += books_issued[key]
            book = Book.query.get(record.b_id)
            member = Member.query.get(record.m_id)
            issue_records_result.append(
                {
                    "r_id": record.r_id,
                    "b_id": record.b_id,
                    "b_name": book.b_name,
                    "m_id": record.m_id,
                    "m_name": member.m_name,
                    "r_i_date": record.r_i_date,
                    "r_r_date": record.r_r_date,
                }
            )

    if search_type == "Books":
        return jsonify(books_result)
    elif search_type == "Members":
        return jsonify(members_result)
    elif search_type == "IssueRecords":
        return jsonify(issue_records_result)
