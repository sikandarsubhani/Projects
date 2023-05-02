# models.py

from lesco import app,db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phone_numbers = db.relationship('PhoneNumber', backref='user', lazy=True)
    reference_numbers = db.relationship('ReferenceNumber', backref='user', lazy=True)

class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class ReferenceNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch_no = db.Column(db.String(2), nullable=False)
    sub_div = db.Column(db.String(5), nullable=False)
    ref_no = db.Column(db.String(8), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)




'''
user1 = User(name='John Doe')
db.session.add(user1)
db.session.commit()

phone1 = PhoneNumber(number='03111111111', user=user1)
phone2 = PhoneNumber(number='03121111111', user=user1)

ref1 = ReferenceNumber(batch_no=0o3, sub_div=11225, ref_no=45612312, user=user1)

db.session.add_all([phone1, phone2, ref1])
db.session.commit()


# assuming you already have an existing User object
new_phone_number = PhoneNumber(number='03111111111', user=user1)

# add the new phone number to the session
db.session.add(new_phone_number)

# commit the changes to the database
db.session.commit()

SELECT User.id, User.name, Phone_Number.number, Reference_Number.batch_no, Reference_Number.sub_div, Reference_Number.ref_no
FROM User
LEFT JOIN Phone_Number ON User.id = Phone_Number.user_id
LEFT JOIN Reference_Number ON User.id = Reference_Number.user_id;

'''