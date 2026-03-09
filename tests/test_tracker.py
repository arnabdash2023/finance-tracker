import pytest
import os
from app.storage import init_db, DB_NAME
from app.tracker import add_expense, get_expenses, delete_expense

@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Fresh database for every test."""
    init_db()
    yield
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

def test_add_expense():
    add_expense("2026-03-09", "Food", 250.0, "Lunch")
    expenses = get_expenses()
    assert len(expenses) == 1
    assert expenses[0][2] == "Food"
    assert expenses[0][3] == 250.0

def test_add_multiple_expenses():
    add_expense("2026-03-09", "Food", 250.0, "Lunch")
    add_expense("2026-03-09", "Transport", 50.0, "Bus")
    expenses = get_expenses()
    assert len(expenses) == 2

def test_delete_expense():
    add_expense("2026-03-09", "Food", 250.0, "Lunch")
    expenses = get_expenses()
    expense_id = expenses[0][0]
    delete_expense(expense_id)
    assert len(get_expenses()) == 0

def test_empty_database():
    assert get_expenses() == []
