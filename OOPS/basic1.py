class ExpenseTracker:
    # class atrribute same accross all the object
    version_application = 0.1
    """ this is expense tracker class"""
    def __init__(self,tracker_category,opening_balance,budget):
        # instance_attribute varies from object to object
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget

home_tracker = ExpenseTracker("Home",1000,1000)
shop_tracker = ExpenseTracker("Shop",2000,2000)
print(getattr(home_tracker,'tracker_category'))
print(home_tracker.__dict__)
print(home_tracker.version_application)


