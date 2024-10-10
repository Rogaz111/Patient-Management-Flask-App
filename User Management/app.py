from flask import Flask
from routes.home import home_bp
from routes.patients import patients_bp
from routes.doctors import doctors_bp
from routes.medical_scheme import medical_scheme_bp
from routes.appointment import appointments_bp
from database_service import db, metadata, Base

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

# Register Blueprints (APP Routes)
app.register_blueprint(home_bp)
app.register_blueprint(patients_bp)
app.register_blueprint(doctors_bp)
app.register_blueprint(medical_scheme_bp)
app.register_blueprint(appointments_bp)


# Initialize the database service
@app.before_request
def initialize_db():
    # This function will run before the first request to the app, useful for setup tasks
    print("Database connection established.")

    # Create the tables if they don't exist
    Base.metadata.create_all(db)  # <-- This will create the tables based on models

    # Check if tables were created
    metadata.reflect(bind=db)
    print(f"Current Tables: {metadata.tables.keys()}")


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
