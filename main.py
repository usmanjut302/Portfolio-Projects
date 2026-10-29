
from expense import (
    add_expense,
    display_expenses,
    validate_amount,
    validate_date,
    validate_text,
    get_total_expenses,
    get_expenses_by_category,
    get_expenses_by_date,
    get_monthly_expenses,
)
import logging


logging.basicConfig(
    filename="expense_tracker.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    while True:
        print("="*5,"AI EXPENSE TRACKER","="*5)
        print("1. Add Expense")
        print("2. View all Expenses")
        print("3. View total expenses")
        print("4. View expenses by category")
        print("5. View expenses by date")
        print("6. View monthly expenses")
        print("7. Exit")
        print("Choose an Option")
        try:
            choice = int(input("Enter the choice:"))
            
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue    

        if choice ==1:
            try:
                amount = (input("Enter the amount:"))
                # raise RuntimeError("Test database failure handling")
                add_expense(
                    
                    amount =validate_amount(amount),
                    
                    category = validate_text(input("Enter the category: "), "Category"),
                    description = validate_text(input("Enter the description: "), "Description"),
                    expense_date = validate_date(input("Enter the date (YYYY-MM-DD):"))
                )
                print("Expense added successfully!")
            except ValueError as error:
                print("Error:", error)   
            except Exception as error:
                print("Could not save the expense due to an unexpected error.") 
                logging.exception("Unexpected error while saving expense")
        elif choice ==2:
            display_expenses()
        elif choice == 3:
            total_expense = get_total_expenses()
            print(f"Amount: Rs. {total_expense:.2f}")
        
        elif choice == 4:
            try:
                # raise RuntimeError("Test category report error handling")
                expense_by_category = get_expenses_by_category()
                print("-" * 5, "Expense by category", "-" * 5)

                if not expense_by_category:
                    print("No expenses found.")
                else:
                    for category, total_expense in expense_by_category:
                        category = category or "Uncategorized"
                        print(f"{category}: Rs. {total_expense:.2f}")

            except Exception:
                print("Could not retrieve the category-wise report.")
                logging.exception(
                    "Unexpected error while retrieving category-wise report"
                )
       
        
        elif choice == 5:
            try:
                start_date = validate_date(
                    input("Enter the start date (YYYY-MM-DD): ")
                )
                end_date = validate_date(
                    input("Enter the end date (YYYY-MM-DD): ")
                )

                if start_date > end_date:
                    print("Error: Start date cannot be later than end date.")
                    continue

                expenses_by_date = get_expenses_by_date(
                    start_date, end_date
                )

                print("-" * 5, "Expenses by date", "-" * 5)

                if not expenses_by_date:
                    print("No expenses found for this date range.")
                else:
                    for expense_date, total in expenses_by_date:
                        print(f"{expense_date}: Rs. {total:.2f}")

            except ValueError as error:
                print("Error:", error)
            except Exception:
                print("Could not retrieve the date-wise report.")
                logging.exception(
                    "Unexpected error while retrieving date-wise report"
                )
        
        elif choice == 6:
            try:
                monthly_expenses = get_monthly_expenses()

                print("-" * 5, "Monthly Expense Report", "-" * 5)

                if not monthly_expenses:
                    print("No expenses found.")
                else:
                    for year, month, total in monthly_expenses:
                        print(f"{year}-{month:02d}: Rs. {total:.2f}")

            except Exception:
                print("Could not retrieve the monthly expense report.")
                logging.exception(
                    "Unexpected error while retrieving monthly expense report"
                )

        elif choice == 7:
            print("Goodbye")
            break

        elif choice == 7:
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try again")        



if __name__ == "__main__":
    main()
            