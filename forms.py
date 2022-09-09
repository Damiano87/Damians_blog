from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField(label="Enter your email", validators=[DataRequired()])
    password = PasswordField(label="Enter your password", validators=[DataRequired()])
    name = StringField(label="Enter your name", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class LoginForm(FlaskForm):
    email = StringField(label="Enter your email", validators=[DataRequired()])
    password = PasswordField(label="Enter password", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
