from flask import Flask, render_template, request, redirect
app = Flask(__name__)
blog_posts = []

@app.route('/')
def hello_world():
    author = "Charles"
    name = "Dickens"
    return render_template('index.html', author=author, name=name)

@app.route('/write_post', methods = ['POST'])
def write_post():
    text = request.form['text']
    blog_posts.append(text)
    print(blog_posts)
    return redirect('/')

@app.route('/blog_posts.html')
def posts():
    return render_template('emails.html', blog_posts=blog_posts)

if __name__ == "__main__":
	app.run()