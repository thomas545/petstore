from collections import OrderedDict


def calculate_paid_values(bidders):
    if not isinstance(bidders, dict):
        raise ValueError("Bidders must be a dict")

    data_sorted = dict(
        OrderedDict(reversed(sorted(bidders.items(), key=lambda kv: (kv[1], kv[0]))))
    )
    results = {}
    index = 0

    bidders = list(data_sorted.keys())
    amounts = list(data_sorted.values())
    amounts.pop(0)

    for bidder in bidders:
        if index > len(amounts) - 1:
            results[bidder] = "Lost"
            break
        results[bidder] = amounts[index]

        index += 1

    return results
