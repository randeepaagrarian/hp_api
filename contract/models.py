from datetime import datetime
from dateutil.relativedelta import relativedelta

class Contract():
    def __init__(self, capital, installments, installment_interval, rate, initiation_date, method):
        self.capital = int(capital)
        self.installments = int(installments)
        self.installment_interval = int(installment_interval)
        self.rate = float(rate)
        self.initiation_date = datetime.strptime(initiation_date, '%Y-%m-%d')
        self.method = method

        self.installment_capital = round(self.capital / self.installments, 2)
        self.schedule = []

    def add_to_schedule(self, installment_capital, installment_interest, due_date):
        self.schedule.append({
            "capital": installment_capital,
            "interest": installment_interest,
            "default_interest": 0,
            "due_date": due_date
        })

    def balance_capital(self):
        schedule_capital_total = self.installment_capital * self.installments
        capital_difference = round(self.capital - schedule_capital_total, 2)
        self.schedule[-1]['capital'] = round(float(self.schedule[-1]['capital']) + capital_difference, 2)

    def straight_line(self):
        real_rate = self.rate * 0.01
        interest = (real_rate / 12) * self.installment_interval * self.installments * self.capital
        installment_interest = round(interest / self.installments, 2)
        for x in range(self.installments):
            self.initiation_date += relativedelta(months=self.installment_interval)
            self.add_to_schedule(self.installment_capital, installment_interest, self.initiation_date.strftime('%Y-%m-%d %H:%M:%S'))
        

    def reducing_balance(self):
        installment_interest_rate = (self.rate / (12 / self.installment_interval)) * 0.01
        for x in range(self.installments):
            self.initiation_date += relativedelta(months=self.installment_interval)
            self.add_to_schedule(self.installment_capital, round((self.capital - (self.installment_capital * x)) * installment_interest_rate, 2), self.initiation_date.strftime('%Y-%m-%d %H:%M:%S'))

    def get_schedule(self):
        if self.method == 'S':
            self.straight_line()
        elif self.method == 'R':
            self.reducing_balance()
        self.balance_capital()
        return self.schedule
        