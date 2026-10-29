# from database import add_expense, get_connection

# add_expense(
#     350.00,
#     "Food",
#     "Lunch",
#     "2026-10-25"
# )

# print("Expense added successfully!")

# connection = get_connection()
# cursor = connection.cursor()

# cursor.execute("SELECT * FROM expenses")
# for row in cursor.fetchall():
#     print(row)

# cursor.close()
# connection.close()



# from expense import create_expense

# create_expense(
#     500.00,
#     "Transport",
#     "Bus fare",
#     "2026-10-25"
# )

# print("Expense created successfully!")



# from expense import get_all_expenses

# expenses = get_all_expenses()

# for expense in expenses:
#     print(expense)
# from expense import display_expenses

# display_expenses()



# from expense import validate_amount

# print(validate_amount("100"))
# print(validate_amount("0"))
# print(validate_amount("abc"))



# from expense import validate_amount

# test_values = ["100", "0", "abc", "-50"]

# for value in test_values:
#     try:
#         result = validate_amount(value)
#         print(f"{value} -> Valid: {result}")
#     except ValueError as error:
#         print(f"{value} -> Error: {error}")


# from expense import validate_amount

# tests = ["250", "0", "-50", "abc", "nan", "inf"]

# for value in tests:
#     try:
#         result = validate_amount(value)
#         print(f"{value!r} ACCEPTED: {result}")
#     except ValueError as error:
#         print(f"{value!r} REJECTED: {error}")


# from expense import validate_date
# from datetime import date, timedelta

# tests = [
#     date.today().isoformat(),
#     (date.today() - timedelta(days=1)).isoformat(),
#     (date.today() + timedelta(days=1)).isoformat(),
#     "2026-02-30",
#     "hello",
# ]

# for value in tests:
#     try:
#         result = validate_date(value)
#         print(repr(value), "ACCEPTED:", result)
#     except ValueError as error:
#         print(repr(value), "REJECTED:", error)


# from expense import get_total_expenses

# total = get_total_expenses()

# print(f"Total expenses: Rs. {total:.2f}")


# from expense import get_expenses_by_category

# results = get_expenses_by_category()

# print("Expenses by category:")

# for category, total in results:
#     print(f"{category or 'Uncategorized'}: Rs. {total:.2f}")


# from expense import get_expenses_by_date

# results = get_expenses_by_date("2026-10-25", "2026-10-26")

# print("Daily expense report:")

# for expense_date, total in results:
#     print(f"{expense_date}: Rs. {total:.2f}")




from expense import get_monthly_expenses

results = get_monthly_expenses()

print("Monthly Expense Report:")

if not results:
    print("No expenses found.")
else:
    for year, month, total in results:
        print(f"{year}-{month:02d}: Rs. {total:.2f}")
