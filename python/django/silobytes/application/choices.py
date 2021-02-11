STATUS_OPEN = 'open'
STATUS_FINISHED = 'finished'

STATUS_CHOICES = (
    (STATUS_OPEN, 'Open'),
    (STATUS_FINISHED, 'Finished'),
)


CREDIT_CARD = 'credit-card'
DEBIT_CARD = 'debit-card'
MONEY = 'money'
DEPOSIT = 'deposit'
TRANSFER = 'transfer'
CHECK = 'check'

PAYMENT_METHOD_CHOICES = (
    (MONEY, 'Money'),
    (CREDIT_CARD, 'Credit Card'),
    (DEBIT_CARD, 'Debit Card'),
    (DEPOSIT, 'Deposit'),
    (TRANSFER, 'Transfer'),
    (CHECK, 'Bank Check'),
)
