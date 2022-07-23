class ExpenseTracker:
    # class atrribute same accross all the object
    version_application = 0.1
    """ this is expense tracker class"""

    def __init__(self, tracker_category, opening_balance, budget):
        # instance_attribute varies from object to object
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget

    # Instance method
    def get_orignal_balnce(self):
        return self.convert_amount(self.opening_balance)

    # Instance method
    def check_balance(self, limit=1000):
        if self.opening_balance >= limit:
            return True
        else:
            return "Your opening balance is less than limit"

    # Static method
    @staticmethod
    def convert_amount(amount):
        return float(amount)
    # Factory method
    # class method
    @classmethod
    def get_attributes_from_string(cls, diary_entry: str):
        tracker_category, opening_balance, budget = diary_entry.split(" ")

        return ExpenseTracker(tracker_category.capitalize(),
                              cls.convert_amount(opening_balance),
                              cls.convert_amount(budget))


obj1 = ExpenseTracker.get_attributes_from_string("shopping 100 500")

print(obj1.__dict__)

