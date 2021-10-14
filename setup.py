from app import create_app, db
from flask_migrate import Migrate


app = create_app()
app.app_context().push()
migrate = Migrate(app, db)

def reset():
    from app.models import User
    from app.models import Character
    db.drop_all()
    db.create_all()
    owner = User('cheat-commando', 'codemonkey')
    simon = Character(1, 'Simon', 'Renegade Haze-killer', 31)
    db.session.add(owner)
    db.session.add(simon)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)