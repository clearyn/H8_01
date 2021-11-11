from flask import Flask, request, render_template, url_for
from markupsafe import escape
import webbrowser
from author_book import author_book

##Create the application instance (Include template html)
app = Flask(__name__, template_folder='templates')

##Custom generator link for homepage
def indexLink():
    yield url_for('index')
    yield url_for('show_user_profile', username = 'Wawan Reginold')
    yield url_for('show_post', post_id = 1)
    yield url_for('show_subpath', subpath = 1)
    yield url_for('login', method='POST')
    yield url_for('author')

##Routing
@app.route('/')
def index():
    links = []
    for link in indexLink():
        links.append(link)
    return render_template('home.html', hellomessage = 'Heloo User', links =links)

##Varialbe Rules
@app.route('/user/<username>')
def show_user_profile(username):    # show the user profile for that user    
     return f'User {escape(username)}'
@app.route('/post/<int:post_id>')
def show_post(post_id):    # show the post with the given id, the id is an integer    
    return f'Post {post_id}'
@app.route('/path/<path:subpath>')
def show_subpath(subpath):    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

##Another example book
@app.route('/author', methods=['GET', 'POST'])
def author():
    if 'author_id' in request.form:
        author_book[request.form['author_id']] = []

    return render_template('authors.html', author_book = author_book)


##HTTP Methods
@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':        
        return 'do_the_login()' 
    else:       
        return 'show_the_login_form()'
    
if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(debug=True)