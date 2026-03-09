from app.storage import get_connection, init_db

def add_expense(date, category, amount, note=""):
    init_db()
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO expenses (date, category, amount, note) VALUES (?, ?, ?, ?)",
            (date, category, float(amount), note)
        )

def get_expenses():
    init_db()
    with get_connection() as conn:
        return conn.execute("SELECT * FROM expenses").fetchall()

def delete_expense(expense_id):
    init_db()
    with get_connection() as conn:
        conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
