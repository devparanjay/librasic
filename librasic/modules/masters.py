from librasic.modules.knights import *
from librasic.imports.imports import Book, Member, IssueRecord


# master functions

# master function for books


def check_book(b_id: int, func: str):
    book = Book.query.get_or_404(b_id, description="Book not found!")
    func_list = ['stock', 'name']
    if func in func_list:
        if func == 'stock':
            return check_book_stock(book)
        elif func == 'name':
            return check_book_name(book)
        elif func == '':  # todo add more functions here
            pass
        else:
            return f'There has been an issue with function {func}, please check the code.'
    else:
        return f'No such function {func} in the function list.'


# master function for members

def check_member(m_id: int, func: str):
    member = Member.query.get_or_404(m_id, description="Member not found!")
    func_list = ['fees_due']
    if func in func_list:
        if func == 'fees_due':
            return check_member_fees_due(member)
        elif func == '':  # todo add more functions here
            pass
        else:
            return f'There has been an issue with function {func}, please check the code.'
    else:
        return f'No such function {func} in the function list.'


# master function for issue records

def issue_records_actions(m_id: int, b_id: int, func: str):
    issue_record = find_issue_record(m_id, b_id)
    func_list = ['find_issue_date', 'find_return_date', 'find_record']
    if func in func_list:
        if func == 'find_issue_date':
            return check_issue_date(issue_record)  # type: ignore
        elif func == 'find_return_date':
            return check_return_date(issue_record)  # type: ignore
        elif func == 'find_record':
            return find_issue_record(m_id, b_id)
        elif func == '':  # todo add more functions here
            pass
        else:
            return f'There has been an issue with function {func}, please check the code.'
    else:
        return f'No such function {func} in the function list.'
