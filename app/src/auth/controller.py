from flask import Blueprint, render_template, request, redirect, flash

from app.common.helpers.enums import Roles
from app.common.models import User
from app.configs.extensions import db
from app.src.auth.view import LoginForm, RegisterForm

auth_bp = Blueprint(
    'auth',
    __name__,
    template_folder="../templates"
)


@auth_bp.route("/sign-up", methods=["GET"])
def sign_up_page():
    form = RegisterForm(request.form)
    return render_template("auth/register.html", form=form)


@auth_bp.route("/sign-up", methods=["POST"])
def sign_up():
    form = RegisterForm(request.form)
    if not form.validate():
        return render_template(
            "auth/register.html",
            form=form,
            error="You've provided wrong data! Try again.",
        )
    with db.session():
        db.session.add(
            User(
                username=form.username.data,
                password=form.password.data,
                role_name=Roles.user
            )
        )

    flash(
        "Thank you for signing up!",
        "success",
    )
    return redirect(url_for("login"))


@auth_bp.route("/login", methods=["POST"])
def login():
    form = LoginForm(request.form)
    with session:
        username = request.form["username"]
        try:
            user = session.query(User).filter_by(username=username).one()
            if request.form["password"] != user.password:
                return render_template(
                    "templates/login.html", error="Неправильний пароль!", form=form
                )
            web_session["logged_in"] = True
            web_session["can_create_test"] = user.can_create_test
            web_session["username"] = username
            web_session["name"] = user.name
            return redirect(url_for("dashboard"))
        except NoResultFound:
            return render_template(
                "templates/login.html",
                error="Користувач з такими реєстраційними даними не знайдений.",
                form=form,
            )
