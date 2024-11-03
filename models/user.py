from extensions.ext_database import db
import uuid
from flask_login import UserMixin


class User(UserMixin, db.Model):
    # User id with uuid
    id = db.Column(db.String(255), primary_key=True, default=lambda: str(uuid.uuid4()))
    google_id = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(255))

    # Timestamps
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    last_login_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    last_login_ip = db.Column(db.String(255))