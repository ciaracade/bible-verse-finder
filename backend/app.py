from flask import Flask
from routes import verseSearch
import nltk

nltk.download('gutenberg')

app = Flask(__name__)

# Register the blueprint from the verseSearch route
app.register_blueprint(verseSearch.bp)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
