from tkinter import *

def calculate_total(initial_investment, interest_rate, additional_monthly_investment, investment_length, investment_length_type):
    investment_total = float(initial_investment)
    if investment_length_type == "Months":
        months = 0
        while months < int(investment_length):
            investment_total += float(additional_monthly_investment)
            investment_total = investment_total + ((investment_total * (float(interest_rate) / 100)) / 12)
            months += 1
        return round(investment_total, 2)
    years = 0
    while years < int(investment_length):
        investment_total += (float(additional_monthly_investment) * 12)
        investment_total = investment_total + (investment_total * (float(interest_rate) / 100))
        years += 1
    return '{0:.2f}'.format(investment_total)
    
    

def calculate_compound_interest(initial_investment, interest_rate, additional_monthly_investment, investment_length_months, investment_length_years, target):
    months = 0
    investment_total = 0
    if investment_length_months is not None and investment_length_months != '':
        investment_total = calculate_total(initial_investment, interest_rate, additional_monthly_investment, investment_length_months, "Months")
    if investment_length_years is not None and investment_length_years != '':
        investment_total = calculate_total(initial_investment, interest_rate, additional_monthly_investment, investment_length_years, "Years")
    target['state'] = 'normal'
    target.insert(0, str(investment_total))
    target['state'] = 'disabled'

if __name__ == "__main__":
    tk = Tk()
    tk.title("Compound Interest Calculator")
    tk.minsize(width=500, height=300)
    tk.maxsize(width=500, height=300)
    L1 = Label(tk, text = "Initial Investment")
    L1.grid(row = 0, column = 0)
    E1 = Entry(tk, bd = 2)
    E1.grid(row = 0, column = 1, pady = 2)
    L2 = Label(tk, text = "Interest Rate(APY)")
    L2.grid(row = 1, column = 0, pady = 2)
    E2 = Entry(tk, bd = 2)
    E2.grid(row = 1, column = 1, pady = 2)
    L3 = Label(tk, text = "Investment Length(Months)")
    L3.grid(row = 2, column = 0, pady = 2)
    E3 = Entry(tk, bd = 2)
    E3.grid(row = 2, column = 1, pady = 2)
    L4 = Label(tk, text = "Investment Length(Years)")
    L4.grid(row = 3, column = 0, pady = 2)
    E4 = Entry(tk, bd = 2)
    E4.grid(row = 3, column = 1, pady = 2)
    L5 = Label(tk, text = "Additional Monthly Investment")
    L5.grid(row = 4, column = 0, pady = 2)
    E5 = Entry(tk, bd = 2)
    E5.grid(row = 4, column = 1, pady = 2)
    L6 = Label(tk, text = "Total After Compound Interest")
    L6.grid(row = 5, column = 0, pady = 2)
    E6 = Entry(tk, state = DISABLED)
    E6.grid(row = 5, column = 1, pady = 2)

    B1 = Button(tk, text = "Calculate", command = lambda: calculate_compound_interest(E1.get(), E2.get(), E5.get(), E3.get(), E4.get(), E6))
    B1.grid(row = 6, column = 4, pady = 2)
    tk.mainloop()