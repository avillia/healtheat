from wtforms import (
    Form,
    StringField,
    PasswordField,
    validators,
)


class RegisterForm(Form):
    username = StringField("username", [validators.Length(min=4, max=25)])
    password = PasswordField(
        "password",
        [
            validators.Regexp(
                r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
                message="Password must contain at least:"
                "<ul>"
                "<li>8 symbols</li>"
                "<li>1 letter</li>"
                "<li>1 digit</li>"
                "</ul>",
            ),
            validators.DataRequired(),
        ],
    )
    confirmation = PasswordField(
        "confirmation",
        [
            validators.EqualTo("password", message="Password doesn't match!"),
            validators.DataRequired(),
        ],
    )


class LoginForm(Form):
    username = StringField("your username", [validators.Length(min=4, max=25)])
    PasswordField(
        "password",
        [
            validators.Regexp(
                r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
                message="Not correct password",
            ),
            validators.DataRequired(),
        ],
    )
