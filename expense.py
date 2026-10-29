import database

from database import get_connection
from datetime import datetime
import logging
import math 

def add_expense(amount, category, description, expense_date):
    connection = get_connection()
    cursor = None

    try:
        
        cursor = connection.cursor()

        query = """
            INSERT INTO expenses
            (amount, category, description, expense_date)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (amount, category, description, expense_date)
        )
        

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def get_all_expenses():
    connection = get_connection()
    cursor = None
    try:
        cursor = connection.cursor()
        query = "SELECT * From expenses"
        cursor.execute(query)
        expenses = cursor.fetchall()
        return expenses

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def get_expenses_by_category():
    connection = get_connection()
    cursor = None 
    try:
        cursor = connection.cursor()
        query = """ SELECT category, SUM(amount)
                    FROM expenses
                    GROUP BY category;"""
        cursor.execute(query)
        expenses = cursor.fetchall()
        return expenses 
    finally:
        if cursor is not None:
            cursor.close()
        connection.close()

def get_expenses_by_date(start_date,end_date):
    
    connection = get_connection()
    cursor = None
    try:
        cursor = connection.cursor()
        query = """ SELECT expense_date, SUM(amount)
                    FROM expenses
                    WHERE expense_date BETWEEN %s AND %s
                    GROUP BY expense_date
                    ORDER BY expense_date"""
        cursor.execute(query,(start_date,end_date))
        expenses = cursor.fetchall()
        return expenses 
    finally:
        if cursor is not None:
            cursor.close()
        connection.close()

def get_total_expenses():
    connection = get_connection()
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT COALESCE(SUM(amount),0) FROM expenses")
        total_expense = cursor.fetchone()
        return total_expense[0]
    finally:
        if cursor is not None:
            cursor.close()
        connection.close()   


def get_monthly_expenses():
    connection = get_connection()
    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                YEAR(expense_date) AS expense_year,
                MONTH(expense_date) AS expense_month,
                SUM(amount) AS monthly_total
            FROM expenses
            GROUP BY YEAR(expense_date), MONTH(expense_date)
            ORDER BY expense_year, expense_month
        """

        cursor.execute(query)
        expenses = cursor.fetchall()
        return expenses

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def display_expenses():
    try:
        # raise RuntimeError("Test retrieval error handling")
        expenses = get_all_expenses()
        if not expenses:
            print("No expenses found.")
            return
        
        for expense in expenses:

            expense_id = expense[0]
            print("ID :",expense_id)
            amount = expense[1]
            print(f"Amount : Rs. {amount:.2f}")
            category = expense[2]
            print("Category :",category)
            description = expense[3]
            print("Description :",description)
            expense_date = expense[4]
            print("Date",expense_date)
    except Exception:
        print("Could not retrieve expenses. Please try again.")
        logging.exception("Unexpected error while retrieving expenses")
        return
    
def validate_amount(amount):
    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("Invalid amount. Please enter a valid number.")
    if not math.isfinite(amount):
        raise ValueError("Amount must be a finite number.")
        
    if amount <= 0:
        raise ValueError("the amount must be greater than zero.")
    return amount


def validate_date(date_text):
    
    try:
        expense_date = datetime.strptime(date_text, "%Y-%m-%d")
        
    except ValueError:
        raise ValueError("Invalid date. Please use YYYY-MM-DD and enter a real calendar date.")
    if expense_date.date() > datetime.today().date():
        raise ValueError ("Future expense dates are not allowed.")
    return expense_date.date()


def validate_text(value, field_name):
    value = value.strip()

    if not value:
        raise ValueError(
            f"{field_name} cannot be empty. Please enter a valid {field_name.lower()}."
        )

    return value
    