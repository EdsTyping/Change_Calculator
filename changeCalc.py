"""Change calculator."""
from decimal import Decimal
import sys


def initialChange():
    """Initialize change counter."""
    amt_given = input('How much money was given in dollars? ')
    item_price = input('What was the total price? ')
    float_change_amount = float(amt_given) - float(item_price)
    change_amount = Decimal(float_change_amount)
    change = round(change_amount, 2)
    print('Change to give back: $' + str(change) + '\n')
    amount = change*100

    D = 100  # dollars, fives, tens, twenties, quarters, dimes, nickels,pennies
    F = 500
    T = 10000
    TW = 20000
    q = 25
    d = 10
    n = 5
    p = 1

    D_count = 0
    F_count = 0
    T_count = 0
    TW_count = 0
    q_count = 0
    d_count = 0
    n_count = 0
    p_count = 0

    while amount - TW >= 0:
        amount -= TW
        TW_count += 1
    while amount - T >= 0:
        amount -= T
        T_count += 1
    while amount - F >= 0:
        amount -= F
        F_count += 1
    while amount - D >= 0:
        amount -= D
        D_count += 1
    while amount - q >= 0:
        amount -= q
        q_count += 1
    while amount - d >= 0:
        amount -= d
        d_count += 1
    while amount - n >= 0:
        amount -= n
        n_count += 1
    while amount - p >= 0:
        amount -= p
        p_count += 1

    money = {
            'Singles': D_count, 'Fives': F_count,
            'Tens': T_count, 'Twenty': TW_count,
            'Quarters': q_count, 'Dimes': d_count,
            'Nickels': n_count, 'Pennies': p_count
            }
    for k, v in money.items():
        print(k + ': ' + str(v))

    moreTransactions()


def moreTransactions():
    """Loop again if user wants."""
    msg = input('\nIs there another transaction? (y/n)\n')
    if msg == 'y':
        initialChange()
    else:
        sys.exit()


initialChange()
