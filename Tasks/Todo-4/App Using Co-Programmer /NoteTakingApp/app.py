from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from io import BytesIO
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/note_taking_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    tags = db.relationship('Tag', secondary='note_tags', back_populates='notes')
    images = db.relationship('Image', back_populates='note', cascade='all, delete-orphan')

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    notes = db.relationship('Note', secondary='note_tags', back_populates='tags')

class NoteTag(db.Model):
    __tablename__ = 'note_tags'
    note_id = db.Column(db.Integer, db.ForeignKey('notes.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey('notes.id'), nullable=False)
    image_data = db.Column(db.LargeBinary)
    file_name = db.Column(db.String(100))
    mime_type = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    note = db.relationship('Note', back_populates='images')

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.form
    new_note = Note(
        title=data['title'],
        content=json.dumps({'text': data['content']})
    )
    
    # Handle tags
    tags = json.loads(data.get('tags', '[]'))
    for tag_name in tags:
        tag = Tag.query.filter_by(name=tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
        new_note.tags.append(tag)
    
    # Handle image
    if 'image' in request.files:
        file = request.files['image']
        if file.filename != '':
            new_image = Image(
                image_data=file.read(),
                file_name=file.filename,
                mime_type=file.content_type
            )
            new_note.images.append(new_image)
    
    db.session.add(new_note)
    db.session.commit()
    return jsonify({'message': 'Note created successfully', 'id': new_note.id}), 201

@app.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    return jsonify([{
        'id': note.id,
        'title': note.title,
        'tags': [tag.name for tag in note.tags],
        'created_at': note.created_at,
        'updated_at': note.updated_at,
        'has_image': len(note.images) > 0
    } for note in notes])

@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = Note.query.get_or_404(note_id)
    return jsonify({
        'id': note.id,
        'title': note.title,
        'content': json.loads(note.content),
        'tags': [tag.name for tag in note.tags],
        'created_at': note.created_at,
        'updated_at': note.updated_at,
        'image': note.images[0].id if note.images else None
    })

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    note = Note.query.get_or_404(note_id)
    data = request.form
    note.title = data.get('title', note.title)
    note.content = json.dumps({'text': data.get('content', json.loads(note.content)['text'])})
    
    # Update tags
    note.tags.clear()
    tags = json.loads(data.get('tags', '[]'))
    for tag_name in tags:
        tag = Tag.query.filter_by(name=tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
        note.tags.append(tag)
    
    # Handle image
    if 'image' in request.files:
        file = request.files['image']
        if file.filename != '':
            # Remove old image if exists
            if note.images:
                db.session.delete(note.images[0])
            
            new_image = Image(
                image_data=file.read(),
                file_name=file.filename,
                mime_type=file.content_type
            )
            note.images.append(new_image)
    
    note.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Note updated successfully'}), 200

@app.route('/images/<int:image_id>', methods=['GET'])
def get_image(image_id):
    image = Image.query.get_or_404(image_id)
    return send_file(
        BytesIO(image.image_data),
        mimetype=image.mime_type,
        as_attachment=True,
        download_name=image.file_name
    )

@app.route('/')
def index():
    return send_file('templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)