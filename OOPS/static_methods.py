class ExpenseTracker:
    # class atrribute same accross all the object
    version_application = 0.1
    """ this is expense tracker class"""
    def __init__(self,tracker_category,opening_balance,budget):
        # instance_attribute varies from object to object
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget

    #Instance method
    def get_orignal_balnce(self):
        return self.convert_amount(self.opening_balance)
    #Instance method
    def check_balance(self,limit=1000):
        if self.opening_balance >= limit:
            return True
        else:
            return "Your opening balance is less than limit"
    #Static method
    @staticmethod
    def convert_amount(amount):
        return float(amount)

obj1 = ExpenseTracker("Home",1000,1000)
obj2 = ExpenseTracker("Business",900,2000)

#print(obj2.check_balance())
print(obj2.get_orignal_balnce())
