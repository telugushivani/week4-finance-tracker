class FinanceTracker:
    # This is the constructor method that runs when an object is created
    def __init__(self):
        # List to store all expense records
        self.expenses = []
    
    # Main method to run the finance tracker application
    def run(self):
        # Print header line
        print("=" * 60)
        # Print application title
        print("          PERSONAL FINANCE TRACKER")
        # Print footer line
        print("=" * 60)
        
        # Infinite loop to keep the menu running until user exits
        while True:
            # Print menu separator
            print("\n" + "=" * 40)
            # Print menu title
            print("              MAIN MENU")
            # Print menu separator
            print("=" * 40)

            # Display menu options
            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. Search Expenses")
            print("4. Generate Monthly Report")
            print("5. View Category Breakdown")
            print("6. Set/Update Budget")
            print("7. Export Data to CSV")
            print("8. View Statistics")
            print("9. Backup/Restore Data")
            print("0. Exit")
            print("=" * 40)
            
            # Take user input and remove extra spaces
            choice = input("\nEnter your choice (0-9): ").strip()
            
            # If user selects option 1, call add_expense method
            if choice == '1':
                self.add_expense()

            # If user selects option 2, call view_expenses method
            elif choice == '2':
                self.view_expenses()

            # If user selects option 3, call search_expenses method
            elif choice == '3':
                self.search_expenses()

            # If user selects option 4, call generate_monthly_report method
            elif choice == '4':
                self.generate_monthly_report()

            # If user selects option 5, call view_category_breakdown method
            elif choice == '5':
                self.view_category_breakdown()

            # If user selects option 6, call set_budget method
            elif choice == '6':
                self.set_budget()

            # If user selects option 7, call export_data method
            elif choice == '7':
                self.export_data()

            # If user selects option 8, call view_statistics method
            elif choice == '8':
                self.view_statistics()

            # If user selects option 9, call backup_restore method
            elif choice == '9':
                self.backup_restore()

            # If user selects 0, exit the program
            elif choice == '0':
                print("\n" + "=" * 60)
                print("Thank you for using Personal Finance Tracker!")
                print("=" * 60)
                break  # Stop the loop

            # If user enters invalid input
            else:
                print("Invalid choice! Please enter 0-9.")
    
    # Method to add a new expense
    def add_expense(self):
        print("\n--- ADD NEW EXPENSE ---")
        # Future code for adding expense will be written here
        print("Expense added successfully!")
    
    # Method to display all expenses
    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        # Future code for viewing expenses will be written here
        print("Displaying all expenses...")
    
    # Method to search expenses
    def search_expenses(self):
        print("\n--- SEARCH EXPENSES ---")
        # Future code for searching expenses will be written here
        print("Searching expenses...")
    
    # Method to generate monthly expense report
    def generate_monthly_report(self):
        print("\n--- MONTHLY REPORT ---")
        # Future code for monthly report will be written here
        print("Generating monthly report...")
    
    # Method to view expenses by category
    def view_category_breakdown(self):
        print("\n--- CATEGORY BREAKDOWN ---")
        # Future code for category breakdown will be written here
        print("Showing category breakdown...")
    
    # Method to set or update budget
    def set_budget(self):
        print("\n--- SET/UPDATE BUDGET ---")
        # Future code for budget setting will be written here
        print("Setting budget...")
    
    # Method to export data to CSV file
    def export_data(self):
        print("\n--- EXPORT DATA ---")
        # Future code for exporting data will be written here
        print("Exporting data...")
    
    # Method to view statistics
    def view_statistics(self):
        print("\n--- STATISTICS ---")
        # Future code for statistics will be written here
        print("Showing statistics...")
    
    # Method to backup or restore data
    def backup_restore(self):
        print("\n--- BACKUP/RESTORE ---")
        # Future code for backup and restore will be written here
        print("Managing backups...")

# Main function – program execution starts here
def main():
    # Create object of FinanceTracker class
    tracker = FinanceTracker()
    # Call the run method
    tracker.run()

# This condition checks whether the script is run directly
if __name__ == "__main__":
    # Call main function
    main()

