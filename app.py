from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dashboard page (HTML)
@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')


# Dashboard API endpoint (JSON)
@app.route('/api/dashboard-data')
def dashboard_data():
    transactions = [
        # Income
        {"date": "2025-11-01", "category": "Sales - Groceries", "amount": 35000, "description": "Monthly Food Sales"},
        {"date": "2025-11-03", "category": "Sales - Electronics", "amount": 15000, "description": "Monthly Electronics Sales"},
        {"date": "2025-11-06", "category": "Sales - Apparel", "amount": 12000, "description": "Monthly Apparel Sales"},
        {"date": "2025-11-09", "category": "Online Orders", "amount": 30000, "description": "E-commerce Sales"},

        # Expense
        {"date": "2025-11-12", "category": "Staff Salaries", "amount": -12000, "description": "Employee Payments"},
        {"date": "2025-11-14", "category": "Rent", "amount": -15000, "description": "Monthly Rent"},
        {"date": "2025-11-16", "category": "Utilities", "amount": -2000, "description": "Electricity and Water Bills"},
        {"date": "2025-11-18", "category": "Supplies", "amount": -3500, "description": "Cleaning & Store Supplies"},
        {"date": "2025-11-20", "category": "Marketing", "amount": -2500, "description": "Advertisement Campaigns"},
        {"date": "2025-11-22", "category": "Gas", "amount": -2300, "description": "Gas Bill Payment"},
        {"date": "2025-11-24", "category": "Internet", "amount": -1500, "description": "Internet Bill Payment"}

    ]

    total_income = sum(t["amount"] for t in transactions if t["amount"] > 0)
    total_expense = sum(abs(t["amount"]) for t in transactions if t["amount"] < 0)
    balance = total_income - total_expense

    return jsonify({
        "transactions": transactions,
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    })


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)


