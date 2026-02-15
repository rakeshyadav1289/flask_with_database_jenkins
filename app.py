from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config.from_object("config.Config")

mysql = MySQL(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, username, role FROM users WHERE id=%s", (user_id,))
    data = cur.fetchone()
    cur.close()
    if data:
        return User(*data)
    return None

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()
        flash("Registration successful! Please login.")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, username, password, role FROM users WHERE username=%s", (username,))
        data = cur.fetchone()
        cur.close()
        if data and bcrypt.check_password_hash(data[2], password):
            user = User(data[0], data[1], data[3])
            login_user(user)
            return redirect(url_for("admin" if user.role=="admin" else "dashboard"))
        else:
            flash("Invalid credentials")
    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return f"Welcome {current_user.username}! (User Dashboard)"

@app.route("/admin", methods=["GET","POST"])
@login_required
def admin():
    if current_user.role != "admin":
        flash("Access denied!")
        return redirect(url_for("dashboard"))
    cur = mysql.connection.cursor()
    if request.method == "POST":
        user_id = request.form["id"]
        new_username = request.form["username"]
        cur.execute("UPDATE users SET username=%s WHERE id=%s", (new_username, user_id))
        mysql.connection.commit()
        flash("User updated successfully!")
    cur.execute("SELECT id, username, role FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template("admin.html", users=users)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
