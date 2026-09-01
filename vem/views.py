import os
from hashlib import sha256
from flask import Blueprint, render_template, request, send_from_directory, session, flash, redirect, url_for, current_app
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename


vem = Blueprint('main', __name__)

@vem.route('/')
def index():
    return render_template(
        'index.html')
