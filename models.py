from app import db
class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    package = db.Column(db.String(10), nullable=False)
    shift = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    mobileNo = db.Column(db.String(13), nullable=False)
    address = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    zip = db.Column(db.String(10), nullable=False)
    userId = db.Column(db.String(30), nullable=True)
    date = db.Column(db.String(30), nullable=True)
    def __repr__(self):
        return "<Name: {} {}>".format(self.firstName,self.lastName)

class Packages(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    fee = db.Column(db.String(10), nullable=False)
    createdBy = db.Column(db.String(30), nullable=False)
    modifiedBy = db.Column(db.String(30), nullable=False)
    createdDate = db.Column(db.String(30), nullable=True)
    modifiedDate = db.Column(db.String(30), nullable=True)
    message = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<Title: {}>".format(self.title)
        
class Shifts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    shiftFrom = db.Column(db.String(10), nullable=False)
    shiftTo = db.Column(db.String(10), nullable=False)
    createdBy = db.Column(db.String(30), nullable=False)
    modifiedBy = db.Column(db.String(30), nullable=False)
    createdDate = db.Column(db.String(30), nullable=True)
    modifiedDate = db.Column(db.String(30), nullable=True)
    message = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<Title: {}>".format(self.title)
        
class Trainers(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    mobileNo = db.Column(db.String(13), nullable=False)
    address = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    zip = db.Column(db.String(10), nullable=False)
    trainerId = db.Column(db.String(30), nullable=True)
    date = db.Column(db.String(30), nullable=True)
    def __repr__(self):
        return "<Name: {} {}>".format(self.firstName,self.lastName)
    
class Payments(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(30), nullable=False)
    month = db.Column(db.String(15), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    amount = db.Column(db.String(10), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return "<Name: {}>".format(self.userName)
        
class Attendance(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return "<Name: {}>".format(self.userName)