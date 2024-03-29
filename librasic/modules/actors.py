import random
from datetime import datetime

from flask import jsonify, make_response

from librasic.imports.imports import (
    ENV_VARS,
    Book,
    IssueRecord,
    Member,
    check_book,
    check_member,
    db,
)

# actor functions


def get_random_four_digit():
    return str(random.randint(1000, 9999)).zfill(3)


def issue_book_record(m_id: int, b_id: int):
    member = Member.query.get_or_404(m_id, description="Member not found!")
    issue_date = datetime.utcnow()

    # checking book stock and fees due
    inStock = check_book(b_id, "stock")
    member_fees_due = check_member(m_id, "fees_due")

    if inStock and member_fees_due <= 500:
        # last_issue = IssueRecord.query.first()
        last_issue = IssueRecord.query.order_by(IssueRecord.r_id.desc()).first()
        # generate r_id
        new_r_id = str(last_issue.r_id + 1) if last_issue else get_random_four_digit()
        # check if r_id already exists in database
        while IssueRecord.query.filter_by(r_id=new_r_id).first():
            new_r_id = get_random_four_digit()

        new_issue_record = IssueRecord(
            r_id=new_r_id, r_i_date=issue_date, b_id=b_id, m_id=m_id
        )

        try:
            book = Book.query.get(b_id)
            book.b_c_stock -= 1
            # print(member.m_books_issued)
            if member.m_books_issued is None:
                member.m_books_issued = {}

            if member.m_books_issued and b_id in member.m_books_issued:
                updated_books = member.m_books_issued[b_id] + 1
            else:
                updated_books = 1

            new_member = {
                "m_id": member.m_id,
                "m_name": member.m_name,
                "m_books_issued": {**member.m_books_issued, b_id: updated_books},
            }
            # print(new_member)
            member_up = Member(**new_member)
            db.session.add(new_issue_record)
            db.session.merge(member_up)
            db.session.commit()
            # print(member.m_books_issued)
        except Exception as e:
            print("Error while adding issue to database: ", e)
            # HTTP status code for internal server error
            return jsonify(
                {
                    "message": "There was an error adding this issue record to the database. Please check the code."
                }
            ), 500

    elif member_fees_due > 500:
        # HTTP status code for conflict error
        return jsonify(
            {
                "message": f"Member's due fees exceed INR {ENV_VARS['DEFAULT_RENT_FEE']}/-"
            }
        ), 409
    else:
        # HTTP status code for not found error
        return jsonify(
            f"Book {check_book(b_id, 'name')} is currently not in stock."
        ), 404


def return_book_record(r_id: int):
    issue_record = IssueRecord.query.get_or_404(
        r_id, description="Issue Record not found!"
    )
    if not issue_record.r_r_date:
        m_id: int = issue_record.m_id
        b_id: int = issue_record.b_id
        member = Member.query.get_or_404(m_id, description="Member not found!")
        book = Book.query.get_or_404(b_id, description="Book not found!")
        return_date = datetime.utcnow()
        # issue_record = issue_records_actions(m_id, b_id, 'find_record')

        # calculating due fees
        days_rented = (return_date - issue_record.r_i_date).days
        daily_book_fee = ENV_VARS["DEFAULT_RENT_FEE"]
        total_fee = daily_book_fee * days_rented

        # updating IssueRecord and Book table with return date stock and updating Member table with the booked currently issued
        issue_record.r_r_date = return_date
        all_books_issued: dict = dict(member.m_books_issued)
        currently_issued = [
            key for key, value in all_books_issued.items() if value != 0
        ]
        if str(b_id) in currently_issued:
            all_books_issued[str(b_id)] -= 1
        member.m_books_issued = all_books_issued
        book.b_c_stock += 1
        member.m_due_fees += total_fee
        db.session.commit()
        response = make_response(
            jsonify({"message": "This book has been returned successfully."}), 200
        )
    else:
        response = make_response(
            jsonify({"message": "This book has already been returned."}), 400
        )
    return response


def pay_fees(m_id: int, fees_paid: int):
    member = Member.query.get_or_404(m_id, description="Member not found!")
    total_due_fees = member.m_due_fees

    # updating database
    member.m_due_fees = total_due_fees - fees_paid
    member.m_total_fees += fees_paid
    db.session.commit()
