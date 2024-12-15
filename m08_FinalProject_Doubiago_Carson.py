
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Toplevel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PersonalBudgetManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Budget Manager")
        
        self.income_data = []
        self.expense_data = []
        self.budget_goal = 0
        
        self.create_main_window()

    def create_main_window(self):
        # Main window elements
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
        
        tk.Label(self.main_frame, text="Personal Budget Manager", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.main_frame, text="Add Income/Expense", command=self.open_entry_window).pack(pady=5)
        tk.Button(self.main_frame, text="Set Budget Goal", command=self.open_budget_window).pack(pady=5)
        tk.Button(self.main_frame, text="View Reports", command=self.open_report_window).pack(pady=5)
        tk.Button(self.main_frame, text="Help and Tips", command=self.open_help_window).pack(pady=5)
        tk.Button(self.main_frame, text="Exit", command=self.root.quit).pack(pady=10)

    def open_entry_window(self):
        # Income and Expense Entry Window
        entry_window = Toplevel(self.root)
        entry_window.title("Add Income/Expense")

        tk.Label(entry_window, text="Type:").grid(row=0, column=0, padx=10, pady=5)
        type_var = tk.StringVar(value="Income")
        tk.OptionMenu(entry_window, type_var, "Income", "Expense").grid(row=0, column=1, padx=10, pady=5)

        tk.Label(entry_window, text="Amount:").grid(row=1, column=0, padx=10, pady=5)
        amount_entry = tk.Entry(entry_window)
        amount_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(entry_window, text="Category:").grid(row=2, column=0, padx=10, pady=5)
        category_entry = tk.Entry(entry_window)
        category_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(entry_window, text="Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
        date_entry = tk.Entry(entry_window)
        date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(entry_window, text="Add", command=lambda: self.add_entry(type_var.get(), amount_entry.get(), category_entry.get(), date_entry.get(), entry_window)).grid(row=4, column=0, columnspan=2, pady=10)

    def add_entry(self, entry_type, amount, category, date, window):
        try:
            amount = float(amount)
            if not category or not date:
                raise ValueError("Category and Date cannot be empty.")
            
            if entry_type == "Income":
                self.income_data.append((amount, category, date))
            else:
                self.expense_data.append((amount, category, date))
            
            messagebox.showinfo("Success", f"{entry_type} added successfully!")
            window.destroy()
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")

    def open_budget_window(self):
        # Budget Goal Setting Window
        budget_window = Toplevel(self.root)
        budget_window.title("Set Budget Goal")

        tk.Label(budget_window, text="Monthly Budget Goal:").grid(row=0, column=0, padx=10, pady=5)
        budget_entry = tk.Entry(budget_window)
        budget_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(budget_window, text="Set Goal", command=lambda: self.set_budget_goal(budget_entry.get(), budget_window)).grid(row=1, column=0, columnspan=2, pady=10)

    def set_budget_goal(self, goal, window):
        try:
            self.budget_goal = float(goal)
            messagebox.showinfo("Success", "Budget goal set successfully!")
            window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid budget goal. Please enter a number.")

    def open_report_window(self):
        # Report and Visualization Window
        report_window = Toplevel(self.root)
        report_window.title("Reports and Visualization")

        tk.Label(report_window, text="Expense Distribution by Category", font=("Arial", 14)).pack(pady=10)

        categories = [item[1] for item in self.expense_data]
        amounts = [item[0] for item in self.expense_data]

        if categories and amounts:
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
            ax.set_title("Expense Distribution")

            canvas = FigureCanvasTkAgg(fig, master=report_window)
            canvas.get_tk_widget().pack()
            canvas.draw()
        else:
            tk.Label(report_window, text="No expense data available.").pack(pady=10)

    def open_help_window(self):
        # Help and Tips Window
        help_window = Toplevel(self.root)
        help_window.title("Help and Tips")

        tk.Label(help_window, text="How to Use the Application", font=("Arial", 14)).pack(pady=10)
        tk.Label(help_window, text="1. Add your income and expenses.").pack(anchor="w")
        tk.Label(help_window, text="2. Set a monthly budget goal.").pack(anchor="w")
        tk.Label(help_window, text="3. View reports to track your progress.").pack(anchor="w")
        tk.Label(help_window, text="4. Use the tips to improve your budgeting.").pack(anchor="w")

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalBudgetManager(root)
    root.mainloop()
