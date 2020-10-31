from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, validators
from wtforms.validators import DataRequired


class MNISTForm(FlaskForm):
    temp = SelectField(
        'Attribute',
        choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')],
        [validators.DataRequired()]
    )
    submit = SubmitField('Submit')


class AttributeForm(FlaskForm):
    collar = SelectField(
        'Collar',
        choices=[('0', 'No'), ('1', 'Yes')],
        [validators.DataRequired()]
    )
    gender = SelectField(
        'Gender',
        choices=[('Male', 'Male'), ('Female', 'Female')],
        [validators.DataRequired()]
    )
    necktie = SelectField(
        'NeckTie',
        choices=[('0', 'No'), ('1', 'Yes')],
        [validators.DataRequired()]
    )
    pattern = SelectField(
        'Pattern',
        choices=[('Floral', 'Floral'), ('Graphic', 'Graphic'), ('Plaid', 'Plaid'), ('Solid', 'Solid'), ('Spot', 'Spot'), ('Stripe', 'Stripe')],
        [validators.DataRequired()]
    )
    placket = SelectField(
        'Placket',
        choices=[('0', 'No'), ('1', 'Yes')],
        [validators.DataRequired()]
    )
    scarf = SelectField(
        'Scarf',
        choices=[('0', 'No'), ('1', 'Yes')],
        [validators.DataRequired()]
    )
    skinexposure = SelectField(
        'Skin Exposure',
        choices=[('0', 'No'), ('1', 'Yes')],
        [validators.DataRequired()]
    )
    category = SelectField(
        'Category',
        choices=[('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8')],
        [validators.DataRequired()]
    )
    neckline = SelectField(
        'Neckline',
        choices=[('0', '1'), ('1', '2'), ('2', '3'), ('3', '4')],
        [validators.DataRequired()]
    )
    sleevelength = SelectField(
        'Sleeve Length',
        choices=[('0', '1'), ('1', '2'), ('2', '3')],
        [validators.DataRequired()]
    )
    submit = SubmitField('Submit')