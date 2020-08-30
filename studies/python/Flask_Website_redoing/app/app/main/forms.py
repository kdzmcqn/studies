from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

    """
    WTForms standard HTML fields
    
    BooleanField            Checkbox with True and False values
    DateField               Text field that accepts a datetime.date value in a given format
    DateTimeField           Text field that accepts a datetime.datetime value in a given format
    DecimalField            Text field that accepts a decimal.Decimal value
    FileField               File upload field
    HiddenField             Hidden text field
    MultipleFileField       Multiple file upload field
    FieldList               List of fields of a given type
    FloatField              Text field that accepts a floating-point value
    FormField               Form embedded as a field in a container form
    IntegerField            Text field that accepts an integer value
    PasswordField           Password text field
    RadioField              List of radio buttons
    SelectField             Drop-down list of choices
    SelectMultipleField     Drop-down list of choices with multiple selection
    SubmitField             Form submission button
    StringField             Text field
    TextAreaField           Multiple-line text field
    
    WTForms validators
    
    DataRequired            Validates that the field contains data after type conversion
    Email                   Validates an email address
    EqualTo                 Compares the values of two fields; useful when requesting 
                            a password to be entered twice for confirmation
    
    InputRequired           Validates that the field contains data before type conversion
    IPAddress               Validates an IPv4 network address
    Length                  Validates the length of the string entered
    MacAddress              Validates a MAC address
    NumberRange             Validates that the value entered is within a numeric range
    Optional                Allows empty input in the field, skipping additional validators
    Regexp                  Validates the input against a regular expression
    URL                     Validates a URL
    UUID                    Validates a UUID
    AnyOf                   Validates that the input is one of a list of possible values
    NoneOf                  Validates that the input is none of a list of possible values
    """
