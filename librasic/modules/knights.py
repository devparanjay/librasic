from datetime import datetime
from librasic.imports.imports import Book, Member, IssueRecord


# knight functions

def check_book_stock(book: Book):
    c_stock: int = int(book.b_c_stock)
    if c_stock > 0:
        return True
    else:
        return False


def check_book_name(book: Book) -> str:
    return str(book.b_name)


def check_member_fees_due(member: Member):
    return member.m_due_fees


def check_issue_date(issue_record: IssueRecord) -> datetime:
    return issue_record.r_i_date


def check_return_date(issue_record: IssueRecord) -> datetime:
    return issue_record.r_r_date


def find_issue_record(m_id, b_id):
    issue_record = IssueRecord.query.filter_by(b_id=b_id, m_id=m_id).first()
    return issue_record
