function addExpense(event) {
    event.preventDefault();
    const form = event.target;
    const formData = {
        title: document.getElementById('title').value,
        amount: parseFloat(document.getElementById('amount').value),
        date: document.getElementById('date').value,
        description: document.getElementById('description').value
    };

    fetch('/expense', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            form.reset();
            
            // Update the expense list and totals
            fetchExpenseList();
            updateTotals();
        } else {
            alert('Error adding expense: ' + data.message);
        }
    })
    .catch(error => console.error('Error adding expense:', error));
}

document.addEventListener('DOMContentLoaded', function() {
    updateTotals();
    fetchExpenseList();

    const expenseForm = document.getElementById('expense-form');
    const receiptInput = document.getElementById('receipt');

    if (expenseForm) {
        expenseForm.addEventListener('submit', addExpense);
    } else {
        console.error('Expense form not found');
    }

    receiptInput.addEventListener('change', function(e) {
        if (e.target.files.length > 0) {
            fetchExpenseFromImage(e.target.files[0]);
        }
    });
});

function fetchMonthlyTotal() {
    fetch('/monthly_total')
        .then(response => response.json())
        .then(data => {
            document.getElementById('monthly-total').textContent = `$${data.total.toFixed(2)}`;
        })
        .catch(error => console.error('Error fetching monthly total:', error));
}

function fetchExpenseList() {
    fetch('/expense')
        .then(response => response.json())
        .then(expenses => {
            const expenseList = document.getElementById('expense-list');
            expenseList.innerHTML = '';
            expenses.forEach(expense => {
                const li = document.createElement('li');
                li.className = 'list-group-item d-flex justify-content-between align-items-center';
                li.innerHTML = `
                    <div>
                        <h6>${expense.title}</h6>
                        <small>${expense.date} - ${expense.description}</small>
                    </div>
                    <div>
                        <span class="badge bg-primary rounded-pill me-2">$${expense.amount.toFixed(2)}</span>
                        <button class="btn btn-sm btn-outline-secondary me-1" onclick="editExpense(${expense.id})">Edit</button>
                        <button class="btn btn-sm btn-outline-danger" onclick="deleteExpense(${expense.id})">Delete</button>
                    </div>
                `;
                expenseList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching expense list:', error));
}

function fetchExpenseFromImage(file) {
    const formData = new FormData();
    formData.append('file', file);

    fetch('/fetch_expense_from_image', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (!data.error) {
            document.getElementById('amount').value = data.amount;
            document.getElementById('title').value = data.title;
            document.getElementById('date').value = data.date;
            document.getElementById('description').value = data.description;
        } else {
            alert('Error processing image: ' + data.error);
        }
    })
    .catch(error => console.error('Error fetching expense from image:', error));
}

function editExpense(id) {
    // Implement edit functionality
    console.log('Edit expense:', id);
}

function deleteExpense(id) {
    if (confirm('Are you sure you want to delete this expense?')) {
        fetch(`/expense?id=${id}`, { method: 'DELETE' })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message);
                    fetchExpenseList();
                    updateTotals();
                } else {
                    alert('Error deleting expense: ' + data.message);
                }
            })
            .catch(error => console.error('Error deleting expense:', error));
    }
}

function updateTotals() {
    fetch('/monthly_total')
        .then(response => response.json())
        .then(data => {
            document.getElementById('monthly-total').textContent = `$${data.total.toFixed(2)}`;
        })
        .catch(error => console.error('Error fetching monthly total:', error));

    fetch('/all_time_total')
        .then(response => response.json())
        .then(data => {
            document.getElementById('all-time-total').textContent = `$${data.total.toFixed(2)}`;
        })
        .catch(error => console.error('Error fetching all-time total:', error));
}