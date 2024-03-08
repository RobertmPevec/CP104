"""
------------------------------------------------------------------------
Lab 7, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-02-22'
------------------------------------------------------------------------
"""


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0
    rate /= 100
    while current < target:
        current *= (rate + 1)
        years += 1
    return years


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    numbers = []
    total = 0
    last_total = 0
    while total >= last_total:
        last_total = total
        value = float(input("Enter a number: "))
        numbers.append(value)
        total += value
    del numbers[-1]
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    return minimum, maximum, total, average


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    total_expenses = 0
    expense = 69
    while expense != 0:
        expense = float(input("Enter an expense (0 to quit): "))
        total_expenses += expense
    balance = available - total_expenses
    if total_expenses > available:
        status = "Deficit"
    elif total_expenses < available:
        status = "Surplus"
    else:
        status = "Balance"
    return float(total_expenses), float(balance), status


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the highest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    while 0 == 0:
        value = int(input(f"Enter a value between {low} and {high}: "))
        if value > high:
            print("Value entered is too high")
        elif value < low:
            print("Value entered is too low")
        else:
            break
    return value


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    TOTAL_EMPLOYEES = 0
    NET_WAGES = 0
    OVERTIME_RATE = 1.5
    HOURS = 40
    TAX_RATE = 0.03625
    while 0 == 0:
        employee_id = int(input("Employee ID: "))
        if employee_id == 0:
            break
        hourly_rate = float(input("Hourly wage rate: "))
        hours_worked = float(input("Hours worked: "))
        if hours_worked > 40:
            OVERTIME = hours_worked - HOURS
            net_pay = (OVERTIME * (hourly_rate * OVERTIME_RATE)) + (HOURS * hourly_rate)
            net_pay -= net_pay * TAX_RATE
            print(f"Net pay for employee {employee_id}: ${net_pay:,.2f}")
        elif HOURS >= hours_worked >= 0:
            net_pay = (hours_worked * hourly_rate)
            net_pay -= net_pay * TAX_RATE
        else:
            raise ValueError("Enter a positive value for hours worked.")
        NET_WAGES += net_pay
        TOTAL_EMPLOYEES += 1
    average_salary = NET_WAGES / TOTAL_EMPLOYEES
    return round(NET_WAGES, 2), round(average_salary, 2)
