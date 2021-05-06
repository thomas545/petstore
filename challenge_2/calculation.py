from collections import OrderedDict


def sort_same_bidders(data_sorted):
    new_bidders = []

    for bid, val in data_sorted.items():
        max_val = max(data_sorted.values())
        if val == max_val:
            new_bidders.append(bid)
    new_bidders.sort()
    return new_bidders


def add_other_bidders(data_sorted, bidders):
    new_bidders = sort_same_bidders(data_sorted)
    for bidding in bidders:
        if bidding not in new_bidders:
            new_bidders.append(bidding)
    return new_bidders


def calculate_paid_values(bidders):
    if not isinstance(bidders, dict):
        raise ValueError("Bidders must be a dict")

    if bidders is None or bidders == {}:
        return "No Winners"

    data_sorted = dict(
        OrderedDict(reversed(sorted(bidders.items(), key=lambda kv: (kv[1], kv[0]))))
    )
    results = {}
    index = 0

    bidders = list(data_sorted.keys())
    amounts = list(data_sorted.values())
    amounts.pop(0)
    new_bidders = add_other_bidders(data_sorted, bidders)

    for bidder in new_bidders:
        if index > len(amounts) - 1:
            results[bidder] = "Lost"
            break
        results[bidder] = amounts[index]

        index += 1

    return results
