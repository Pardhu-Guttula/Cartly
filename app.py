from backend import create_app
from backend.models import init_db
from backend.routes.auth_route import auth_bp

# Epic Title: User Login Functionality

app = create_app()
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000)