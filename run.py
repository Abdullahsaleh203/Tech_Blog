from flask_sqlalchemy import SQLAlchemy 
from tech_blog import app
if __name__ == '__main__':
    app.run(debug=True, port=8000)
db = SQLAlchemy(app)

from tech_blog import routes
