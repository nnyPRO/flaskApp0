from flask_wtf import FlaskForm
# input field
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
# ตัวเช็คว่ามัน validate รึป่าว
from wtforms.validators import InputRequired, Length

class CourseForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    description = TextAreaField('Course Description',
                                validators=[InputRequired(),
                                            Length(max=200)])
    price = IntegerField('Price', validators=[InputRequired()])
    level = RadioField('Level',
                       choices=['Beginner', 'Intermediate', 'Advanced'],
                       validators=[InputRequired()])
    available = BooleanField('Available', default='checked')
