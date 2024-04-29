import sqlalchemy as db


engine = db.create_engine("mysql://root:123456@mysql:3306/Automate", max_overflow=5)

# Create the Metadata Object
metadata_obj = db.MetaData()
User_info = db.Table(
    'User_info',
    metadata_obj,
    db.Column('name', db.String(100), primary_key=True),
    db.Column('password', db.String(100)),
    db.Column('phone_number', db.String(100)),
)

Book_info = db.Table(
    'Book_info',
    metadata_obj,
    db.Column('title', db.String(100), primary_key=True),
    db.Column('categories', db.String(100)),
    db.Column('authors', db.String(100)),
    db.Column('ratings', db.String(100)),
    db.Column('price', db.String(100)),
)

Booking_record  = db.Table(
    'Booking_record',
    metadata_obj,
    db.Column('record_number', db.Integer, primary_key=True,autoincrement=True),
    db.Column('name', db.String(100)),
    db.Column('title', db.String(100)),
    db.Column('price', db.String(100))
)

# Create the profile table
metadata_obj.create_all(engine)
