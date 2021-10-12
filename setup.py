from app import create_app, db
from flask_migrate import Migrate

app = create_app()
app.app_context().push()
migrate = Migrate(app, db)

def reset():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)