from os import getenv
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")