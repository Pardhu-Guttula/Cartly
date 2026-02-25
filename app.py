from backend import create_app
from backend.models import init_db

# Epic Title: User Signup Functionality

app = create_app()

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000)