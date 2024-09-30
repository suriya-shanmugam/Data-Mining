# Note-taking App with Image Support

## Overview

This is a simple yet powerful note-taking application built with Flask and PostgreSQL. It allows users to create, read, update, and delete notes with support for tags and image attachments. The application features a responsive web interface for easy note management.

## Features

- Create and edit notes with titles and content
- Add tags to notes for easy categorization
- Attach images to notes
- View a list of all notes


## Requirements

- Python 3.7+
- PostgreSQL
- Flask
- SQLAlchemy
- psycopg2-binary

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/suriya-shanmugam/Data-Mining
   cd Todo4/note-taking-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install flask flask-sqlalchemy psycopg2-binary
   ```

4. Set up the PostgreSQL database:
   - Create a new database named `note_taking_app`
   - Update the database URI in `app.py` with your PostgreSQL credentials:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/note_taking_app'
     ```

5. Initialize the database:
   ```
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Use the interface to:
   - Create new notes by filling in the title, content, tags, and optionally attaching an image
   - View the list of existing notes
   - Click on a note to view its details and edit it
   - Update notes by modifying their content and clicking "Save Note"
   - Create a new note at any time by clicking "New Note"

## Project Structure

- `app.py`: The main Flask application file containing route definitions and database models
- `index.html`: The single-page frontend interface
- `README.md`: This file, containing project documentation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Improvements

- Add user authentication and personal note collections
- Implement a rich text editor for note content
- Add support for multiple images per note
- Create a tagging system with autocomplete
- Implement a search functionality for notes
- Add sorting and filtering options for the note list