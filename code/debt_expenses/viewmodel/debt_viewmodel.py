from debt_expenses.debt import DebtExpenses


class DebtViewModel:
    def __init__(self, req_sum=None, percent_rate=None, period=None, year=None):
        # params
        self.req_sum = req_sum
        self.percent_rate = percent_rate
        self.period = period
        self.year = year
        # status
        self.error_message = 'Please enter data'
        self.payment = None
        self.expenses = None

    def set_req_sum(self, value):
        self.req_sum = value

    def get_req_sum(self):
        return self.req_sum

    def set_percent_rate(self, value):
        self.percent_rate = value

    def get_percent_rate(self):
        return self.percent_rate

    def set_period(self, value):
        self.period = value

    def get_period(self):
        return self.period

    def set_year(self, value):
        self.year = value

    def get_year(self):
        return self.year

    def perform_repayment(self, repayment):
        try:
            debt = DebtExpenses(int(self.req_sum), float(self.percent_rate), int(self.period))
            if 'equal_amounts' in repayment:
                self.payment, self.expenses = debt.equal_amounts_repayment(int(self.year))
            else:
                self.payment, self.expenses = debt.equal_payments_repayment(int(self.year))
            self.update_error_message()
        except Exception:
            self.update_result()
            self.error_message = 'Error: Incorrect input'

    def get_payment(self):
        return self.payment

    def get_expenses(self):
        return self.expenses

    def update_result(self):
        self.payment = None
        self.expenses = None

    def get_error_message(self):
        return self.error_message

    def update_error_message(self):
        self.error_message = None
