from app import create_app, db
from flask_migrate import Migrate
from app.models import User

app = create_app()
app.app_context().push()
migrate = Migrate(app, db)

app.run(debug=True)