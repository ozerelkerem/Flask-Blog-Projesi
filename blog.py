from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)
app.secret_key="ybblog"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "12345678"
app.config["MYSQL_DB"] = "yb_blog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntülemek için giriş yapınız.","danger")
            return redirect(url_for("login"))
    return decorated_function

# Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim",validators=[validators.Length(min = 4,max = 25)])
    username = StringField("Kullanıcı Adı",validators=[validators.Length(min = 5,max = 35)])
    email = StringField("Email",validators=[validators.Email(message="Lütfen Geçerli Email Adresi Giriniz.")])
    password = PasswordField("Parola: ",validators=[
        validators.DataRequired(message="Lütfen bir parola giriniz."),
        validators.EqualTo(fieldname="confirm",message="Parolarınız uyuşmuyor")
    ])
    confirm = PasswordField("Parola Doğrula :")
# Kullanıcı Giriş Formu
class LoginForm(Form):
    username = StringField("Kullanıcı Adı :")
    password = PasswordField("Şifre :")
class ArticleForm(Form):
    title = StringField("Makale Başlığı:",validators=[validators.length(min = 5,max =100)])
    content = TextAreaField("Makele İçeriği",validators=[validators.length(min=5)])

@app.route("/")
def index():
    return render_template("index.html",cevap = "hayır1")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register",methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()
        query = "insert into users (name,email,username,password) values(%s,%s,%s,%s)"
        cursor.execute(query,(name,email,username,password))
        mysql.connection.commit()
        cursor.close()
        flash("Başarıyla kayıt oldunuz.","success")

        return redirect(url_for("login"))
    else:
        return render_template("register.html",form = form)

@app.route("/login",methods = ["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data
        query = "select * from users where username = %s"
        cursor = mysql.connection.cursor()
        result = cursor.execute(query,(username,))
        if result > 0:
            data = cursor.fetchone()
            print(data["password"],password)
            if sha256_crypt.verify(password,data["password"]):
                flash("Başarıyla giriş yaptınız ","success")
                session["logged_in"] = True
                session["username"] = username
                return redirect(url_for("index"))
            else:
                flash("Şifreniz yanlış.","danger")
                return redirect(url_for("login"))

        else:
            flash("Böyle bir kullanıcı yok.","danger")
            return redirect(url_for("login"))
        
        cursor.close()
    else:
        return render_template("login.html",form = form)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/dashboard")
@login_required
def dashboard():
    cursor = mysql.connection.cursor()
    query = "select * from articles where author = %s"
    result = cursor.execute(query,(session["username"],))
    if result > 0:
        articles = cursor.fetchall()
        return render_template("dashboard.html",articles=articles)

    return render_template("dashboard.html")

@app.route("/addarticle",methods = ["POST","GET"])
@login_required
def addarticle():
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        title = form.title.data
        content = form.content.data
        cursor = mysql.connection.cursor()
        query = "insert into articles (title,author,content) values(%s,%s,%s)"
        cursor.execute(query,(title,session["username"],content))
        mysql.connection.commit()
        cursor.close()
        flash("Makale başarı ile eklendi.","success")
        return redirect(url_for("dashboard"))
    return render_template("addarticle.html",form = form)
    
@app.route("/articles")
def articles():
    cursor = mysql.connection.cursor()
    query = "select * from articles"
    result = cursor.execute(query)
    if result > 0:
        articles = cursor.fetchall()
        return render_template("articles.html",articles=articles)
    else:
        return render_template("articles.html")

    cursor.close()
@app.route("/article/<string:id>")
def article(id):
    cursor = mysql.connection.cursor()
    query = "select * from articles where id = %s"
    result = cursor.execute(query,(id,))
    if result > 0:
        article = cursor.fetchone()
        return render_template("article.html",article = article)
    else:
        return render_template("article.html")
    cursor.close()
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cursor = mysql.connection.cursor()
    query = "select * from articles where author = %s and id = %s"
    result = cursor.execute(query,(session["username"],id))
    if result > 0:
        query2 = "delete from articles where id = %s"
        cursor.execute(query2,(id,))
        mysql.connection.commit()
        return redirect(url_for("dashboard"))
    else:
        flash("Böyle bir makale yok yada bu makaleyi silmek için yetkiniz yok.","danger")
        return redirect(url_for("index"))
@app.route("/edit/<string:id>",methods =["POST","GET"])
@login_required
def edit(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        query = "select * from articles where author = %s and id = %s"
        result = cursor.execute(query,(session["username"],id))
        if result == 0:
            flash("Böyle bir makale yok yada bu makaleye güncellemek için yetkiniz yok.","danger")
            return redirect(url_for("index"))
        else:
            article = cursor.fetchone()
            form = ArticleForm()
            form.title.data = article["title"]
            form.content.data = article["content"]
        return render_template("update.html",form = form)
    else:
        form = ArticleForm(request.form)
        newTitle = form.title.data
        newContent = form.content.data

        query = "update articles set title =%s,content = %s where id = %s"
        cursor = mysql.connection.cursor()
        cursor.execute(query,(newTitle,newContent,id))
        mysql.connection.commit()
        flash("Makale Başarı İle güncellendi","success")

        return redirect(url_for("dashboard"))
@app.route("/search",methods =["POST","GET"])
def search():
    if request.method == "GET":
        return redirect(url_for("index"))
    else:
        keyword = request.form.get("keyword")
        cursor = mysql.connection.cursor()
        query = "select * from articles where title like %s"
        result = cursor.execute(query,("%"+str(keyword)+"%",))
        if result == 0:
            flash("Böyle bir makale bulunamadı","warning")
            return redirect(url_for("articles"))
        else:
            articles = cursor.fetchall()
            return render_template("articles.html",articles = articles)





if __name__ == "__main__":
    app.run(debug=True)