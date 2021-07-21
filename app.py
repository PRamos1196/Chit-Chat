import os
from os.path import join, dirname
from dotenv import load_dotenv
import flask
import flask_sqlalchemy
import flask_socketio
import requests
from rfc3987 import parse

dotenv_path = join(dirname(__file__), "sql.env")
load_dotenv(dotenv_path)
app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")
sql_user = os.environ["SQL_USER"]
sql_pwd = os.environ["SQL_PASSWORD"]
key = os.environ["KEY"]
database_uri = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
db = flask_sqlalchemy.SQLAlchemy(app)
db.app = app
db.init_app(app)
import messages


@socketio.on("new google user")
def on_new_google_user(data):
    name = data["name"]
    email = data["email"]
    if not returning_user_handler(email):
        push_new_user_to_db(
            data["name"], data["email"], data["imageUrl"], messages.AuthUserType.GOOGLE
        )
    socketio.emit(
        "login-successful", {"name": name, "email": email, "imageUrl": data["imageUrl"]}
    )
    print(data["name"])
    return data["name"] + " " + data["email"] + " " + data["imageUrl"]


def emit_all_oauth_users():
    all_users = [name.name for name in db.session.query(messages.AuthUser).all()]
    socketio.emit("accounts received", {"allUsers": all_users})
    return all_users


def push_new_user_to_db(name, email, image_url, auth_type):
    db.session.add(messages.AuthUser(name, email, image_url, auth_type))
    db.session.commit()
    emit_all_oauth_users()


def returning_user_handler(email):
    users = db.session.query(messages.AuthUser).all()
    for user in users:
        if user.email == email and user.email == email:
            return True
    return False


@socketio.on("new-message")
def emit_all_messages():
    all_messages = []
    all_users = []
    all_urls = []
    type_of = []
    for message_string in (
        db.session.query(messages.Messages).order_by(messages.Messages.id).all()
    ):
        try:
            if parse(message_string.message, rule="IRI"):
                if (
                    message_string.message[-4:] == ".gif"
                    or message_string.message[-4:] == ".png"
                    or message_string.message[-4:] == ".jpg"
                ):
                    all_messages.append({"message": str(message_string.message)})
                    all_users.append({"username": message_string.username})
                    all_urls.append({"urls": message_string.imageUrl})
                    type_of.append({"type": "img"})
                else:
                    all_messages.append({"message": str(message_string.message)})
                    all_users.append({"username": message_string.username})
                    all_urls.append({"urls": message_string.imageUrl})
                    type_of.append({"type": "url"})
        except ValueError:
            all_messages.append({"message": message_string.message})
            all_users.append({"username": message_string.username})
            all_urls.append({"urls": message_string.imageUrl})
            type_of.append({"type": "msg"})
    socketio.emit(
        "message_history",
        {
            "allMessages": all_messages,
            "allUsers": all_users,
            "all_urls": all_urls,
            "type_of": type_of,
        },
    )


@socketio.on("oneTime")
def one_time():
    all_messages = []
    all_users = []
    all_urls = []
    for message_string in (
        db.session.query(messages.Messages).order_by(messages.Messages.id).all()
    ):
        all_messages.append({"message": message_string.message})
        all_users.append({"username": message_string.username})
        all_urls.append({"urls": message_string.imageUrl})
    socketio.emit(
        "message_history",
        {"allMessages": all_messages, "allUsers": all_users, "all_urls": all_urls},
    )


def bot_handling(text):
    url_something = "https://api.funtranslations.com/translate/cheunh.json?text=" + text
    print(text)
    chuenh_translator_api = requests.get(
        url_something, headers={"X-Funtranslations-Api-Secret": key}
    )
    data = chuenh_translator_api.json()
    return data


def joke_api():
    url_joke = "https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,political,racist,sexist"
    joke_made = requests.get(url_joke).json()
    if "joke" not in joke_made:
        joke_setup = joke_made["setup"]
        joke_del = joke_made["delivery"]
        return joke_setup + joke_del
    return joke_made["joke"]


@socketio.on("new-messages")
def new_message_recieved(data):
    text = data["message"]
    command = text.split(" ")[0]
    base = text[:2]
    if base == "!!":
        if command == "!!about":
            message = "Hello i am Cheunh bot, I translate your native tongue into a complex and dense tongue that is used in the Star Wars lore"
        elif command == "!!help":
            message = "Commands \n!!about --- About the chat bot itself and what it translates \n!!help --> See all commands that this bot will respond to \n!!funtranslate <insert text here>"
        elif command == "!!funtranslate":
            fun_trans = text.split("!!funtranslate")
            text_translate = fun_trans[1]
            print(text_translate)
            translates_text = bot_handling(text_translate)
            print(translates_text)
            message = translates_text
        elif command == "!!joke":
            translated_text = joke_api()
            message = translated_text
            print(message)
        else:
            message = (
                "This command is not recognized my master... please try something else"
            )
        data = {
            "message": message,
            "username": "Cheunh Bot",
            "url": "https://avatarfiles.alphacoders.com/123/123561.png",
        }
        db.session.add(
            messages.Messages(data["username"], data["message"], data["url"])
        )
        db.session.commit()
    else:
        db.session.add(
            messages.Messages(data["username"], data["message"], data["url"])
        )
        db.session.commit()
    emit_all_messages()
    return data["message"]


# *******************************************************************************************************************
# Handles for socketio.run needs app, host = (IP, 0.0.0.0), port = 8080, and debug=true


@app.route("/")
def home():
    emit_all_oauth_users()
    return flask.render_template("index.html")


if __name__ == "__main__":
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
