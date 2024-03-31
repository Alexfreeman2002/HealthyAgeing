from app import db, app

def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()