#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Meme # import your models here!

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Hello world"

@app.get('/api/memes')
def get_all_memes():
    return [ memes.to_dict() for memes in Meme.query.all()], 200

@app.get('/api/memes/<int:id>')
def get_one_meme(id):
    meme = Meme.query.where(Meme.id == id).first()

    if meme:
        return meme.to_dict(), 200
    else:
        return { "error": "Not found" }, 404
    
@app.post('/api/memes')
def post_meme():
    new_meme = Meme( 
        img_url=request.json.get('img_url'),
        caption=request.json.get('caption'),
        likes=request.json.get('likes')
        )

    db.session.add( new_meme )
    db.session.commit()

    return new_meme.to_dict(), 201
@app.patch('/api/memes/<int:id>')
def patch_meme(id):
    meme_update = Meme.query.where(Meme.id == id).first()

    if meme_update:
        for key in request.json.keys():
            if not key == 'id':
                setattr(meme_update, key, request.json[key])

        db.session.add ( meme_update )
        db.session.commit()

        return meme_update.to_dict(), 202
    else:
        return { 'error': "Not found" }, 404
    
@app.delete('/api/memes/<int:id>')
def delete_meme(id:int):

    memes_delete = Meme.query.where(Meme.id == id).first()

    if memes_delete:
        db.session.delete( memes_delete )
        db.session.commit()
        return {}, 204
    else:
        return { 'error': "Not found" }, 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)
