<h1>Auto Expense Tracker - Prototype</h1>

<p> This is protype of the application that helps you track the expenses and helps you to quick add the expense by Uploading a <b> Receipt</b>. It process the Image and auto populate the necessary information smartly using the AI giving the user better experience. 

[Video Demo](https://youtu.be/fHOWOT6Uyrw)

## Features

- Monthly expense report
- List of recent expenses
- Add, update, and delete expenses
- Extract expense details from receipt images
- Responsive web interface

## Prerequisites

- Python 3.7+
- Flask
- Google Cloud Vision API credentials
- Gemini API key

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/suriya-shanmugam/Data-Mining
   cd Tasks/Todo-1/Assignment-2/AutoTrackVersion1
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Gemini API key:
   - Create a `.env` file in the project root
   - Add your Gemini API key: `GEMINI_API_KEY=your_api_key_here`


## Running the Application

1. Start the Flask development server:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

## Project Structure

- `app.py`: Main Flask application file
- `spends_handler.py`: Handles expense-related operations
- `image_processor.py`: Processes receipt images using Gemini API
- `templates/index.html`: HTML template for the web interface
- `static/script.js`: JavaScript file for client-side logic
- `static/styles.css`: CSS file for styling
- `expenses.json`: JSON file for storing expense data

## Usage

1. **Adding an Expense**: 
   - Fill out the expense form with details (amount, title, date, description)
   - Optionally upload a receipt image to auto-fill the form
   - Click "Add Expense" to save

2. **Viewing Expenses**: 
   - The monthly total is displayed at the top
   - The list of expenses is shown below the form

3. **Editing an Expense**: 
   - Click the "Edit" button next to an expense
   - Update the details in the form
   - Click "Update Expense" to save changes

4. **Deleting an Expense**: 
   - Click the "Delete" button next to an expense
   - Confirm the deletion when prompted

