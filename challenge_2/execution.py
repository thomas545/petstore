import calculation

bidders = {
    "John Doe": 100,
    "John Smith": 500,
    "Sara Conor": 280,
    "Martin Fowler": 320,
    "Tom": 1000,
    "AThomas": 1000,
}
paid_amounts = calculation.calculate_paid_values(bidders)

print(paid_amounts)