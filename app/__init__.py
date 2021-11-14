from flask import Flask


def update_extensions(app: Flask):
    """
    A method to add the common extensions to the app instance

    Factories are more preferable because of them helps not to
    initially bound extensions to application

    :param app: previously initialized flask app instance
    :return: app object with extensions
    """

    return app


def create_app(config_object="app.configs"):
    """
    Initialize the flask application
    :param config_object:
    :return:
    """

    app = Flask("HealthEat")
    app.config.from_object(config_object)
    update_extensions(app)

    return app
