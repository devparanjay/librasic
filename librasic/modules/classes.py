from datetime import datetime

from librasic.imports.imports import JSON, Column, db

# classes


class Book(db.Model):
    b_id: int = db.Column(db.Integer, primary_key=True)
    b_name = db.Column(db.String, nullable=False)
    b_t_stock = db.Column(db.Integer, nullable=False, default=1)
    b_c_stock = db.Column(db.Integer, default=b_t_stock)
    b_issued_to = db.Column(db.String)
    b_authors = db.Column(db.String, nullable=False)
    b_lang = db.Column(db.String, nullable=False, default="eng")
    b_publication_date = db.Column(db.DateTime)
    b_publisher = db.Column(db.String)
    b_isbn = db.Column(db.Integer, nullable=False)
    b_isbn13 = db.Column(db.Integer)
    b_pages = db.Column(db.Integer)
    b_rating = db.Column(db.Float)
    b_ratings_count = db.Column(db.Integer)
    b_text_reviews_count = db.Column(db.Integer)
    b_date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return "<Book %r>" % self.b_id


class Member(db.Model):
    m_id = db.Column(db.Integer, primary_key=True)
    m_name = db.Column(db.String, nullable=False)
    # m_books_issued = db.Column(db.String)
    # m_books_issued = db.Column(ScalarListType())
    m_books_issued = Column(JSON, default={}, nullable=False)
    m_date_added = db.Column(db.DateTime, default=datetime.utcnow)
    m_due_fees = db.Column(db.Float, default=0)
    m_total_fees = db.Column(db.Float, default=0)

    def __repr__(self) -> str:
        return "<Member %r>" % self.m_id


class IssueRecord(db.Model):
    r_id = db.Column(db.Integer, primary_key=True, default=0)
    r_i_date = db.Column(db.DateTime, nullable=False)
    r_r_date = db.Column(db.DateTime)
    b_id = db.Column(db.Integer, db.ForeignKey(Book.b_id), nullable=False)
    m_id = db.Column(db.Integer, db.ForeignKey(Member.m_id), nullable=False)

    def __repr__(self) -> str:
        return "<Issue Record %r>" % self.r_id


class Fees(db.Model):
    f_id = db.Column(db.Integer, primary_key=True)
    m_id = db.Column(db.Integer, db.ForeignKey(Member.m_id), nullable=False)
    f_total_amount = db.Column(db.Float, nullable=False)
    f_due_amount = db.Column(db.Float, default=0, nullable=False)
    f_notes = db.Column(db.String)

    def __repr__(self) -> str:
        return "<Fee Record %r>" % self.f_id
