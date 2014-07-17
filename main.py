from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
    return render_template('example.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

# For testing purposes.
if __name__ == '__main__':
    app.run()
