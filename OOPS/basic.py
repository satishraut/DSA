class ExpenseTracker:
    """ this is expense tracker class"""
    expence_tracker_version = 0.1
    def __init__(self,tracker_category,opening_balance,budget):
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget

home_tracker = ExpenseTracker("Home",1000,1000)
print(getattr(home_tracker,'opening_balance'))
print(hasattr(home_tracker,'opening_balance1'))

