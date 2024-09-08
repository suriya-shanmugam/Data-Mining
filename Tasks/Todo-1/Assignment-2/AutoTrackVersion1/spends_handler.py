import json
from datetime import datetime

class SpendsHandler:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_expenses(self):
        with open(self.filename, 'w') as f:
            json.dump(self.expenses, f)

    def create_expense(self, data):
        expense = {
            'id': len(self.expenses) + 1,
            'title': data['title'],
            'amount': float(data['amount']),
            'date': data['date'],
            'description': data['description']
        }
        self.expenses.append(expense)
        self.save_expenses()
        return {'success': True, 'message': 'Expense added successfully'}

    def update_expense(self, data):
        expense_id = int(data['id'])
        for expense in self.expenses:
            if expense['id'] == expense_id:
                expense.update(data)
                self.save_expenses()
                return {'success': True, 'message': 'Expense updated successfully'}
        return {'success': False, 'message': 'Expense not found'}

    def delete_expense(self, expense_id):
        expense_id = int(expense_id)
        self.expenses = [e for e in self.expenses if e['id'] != expense_id]
        self.save_expenses()
        return {'success': True, 'message': 'Expense deleted successfully'}

    def get_expenses(self):
        return self.expenses

    def get_monthly_total(self):
        current_month = datetime.now().strftime('%Y-%m')
        total = sum(float(e['amount']) for e in self.expenses if e['date'].startswith(current_month))
        return round(total, 2)

    def get_all_time_total(self):
        total = sum(float(e['amount']) for e in self.expenses)
        return round(total, 2)