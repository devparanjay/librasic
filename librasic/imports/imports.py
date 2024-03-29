from flask import redirect, render_template, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy_utils import ScalarListType
# from librasic.modules.app_setup import db, ENV_VARS
from librasic import db, ENV_VARS
from librasic.modules.classes import Book, Member, IssueRecord
from librasic.modules.masters import check_book, check_member, issue_records_actions
from librasic.modules.actors import issue_book_record, return_book_record
