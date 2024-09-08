import google.generativeai as genai
import json
import os
from PIL import Image
from datetime import datetime

# Replace with your actual API key
genai.configure(api_key = os.getenv('API_KEY'))

def process_image(image_path):
    
    
    img_file = Image.open(image_path)
    
    prompt = """
    Extract Expense details from the Image including total amount spent, 
    Main detail as title, date in yyyy-MM-dd, and Summary in 10 words as Description.
    Date should be in yyyy-MM-dd format. If year is in two digits, change it to four.
    JSON keys are amount, title, date, and description.
    """
    model = genai.GenerativeModel('gemini-1.5-flash',
                              # Set the `response_mime_type` to output JSON
                              generation_config={"response_mime_type": "application/json"})
    response = model.generate_content([prompt, img_file])
    
    try:
        expense_data = json.loads(response.text)
        
        # Ensure date is in correct format
        date = datetime.strptime(expense_data['date'], '%Y-%m-%d')
        expense_data['date'] = date.strftime('%Y-%m-%d')
        
        # Ensure amount is a float
        expense_data['amount'] = float(expense_data['amount'])
        
        return expense_data
    except json.JSONDecodeError:
        return {'error': 'Failed to parse expense data from image'}
    except KeyError:
        return {'error': 'Missing required fields in expense data'}
    except ValueError:
        return {'error': 'Invalid date or amount format'}