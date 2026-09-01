import os
from hashlib import sha256
from flask import Blueprint, render_template, request, send_from_directory, session, flash, redirect, url_for, current_app
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename


vem = Blueprint('main', __name__)

@vem.route('/')
def index():
    saved_property_ids = []
    if session.get('user'):
        print("User in session:", session['user'])
        user_id = get_current_user_id()
        saved_properties = get_saved_for_user(user_id)
        saved_property_ids = [s.listingId for s in saved_properties]


    return render_template(
        'index.html')
