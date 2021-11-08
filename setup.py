from app import create_app, db


app = create_app()
app.app_context().push()

def reset():
    from app.models import User, Character
    from app.mystuff import owner_password
    db.drop_all()
    db.create_all()
    owner = User('cheat-commando', owner_password)
    simon = Character(1, 'Simon', 'Renegade Haze-killer', 31)
    db.session.add(owner)
    db.session.add(simon)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)