"""Fractional Knapsack"""

import json

def fkn(items, max_weight):
    """
    Fractional Knapsack
    find the greatest value that can be obtained
    from a given items

    Params:
    items -- array of item of type
    {
        w: <total weight>,
        v: <total value>
    }

    W -- maximum weight that can be contained in the
    knapsack

    Returns:
    maximum value that can be obtained
    """

    # Calculate the value per unit weight
    for item in items:
        item["unit_value"] = item["v"]/item["w"] * 1.0

    # Sort items by unit value
    sorted_items = sorted(items, key=lambda k: k["unit_value"], reverse=True)
    print(sorted_items)

    knapsack = {
        "weight": 0,
        "value": 0,
        "contents": []
    }

    # Fill the knapsack with items
    for item in sorted_items:
        # Exit condition
        # Check if the knapsack is already full
        if knapsack["weight"] == max_weight:
            break

        # Add the maximum possible weight of the current item
        amount = min(item["w"], max_weight - knapsack["weight"])
        knapsack["weight"] += amount
        knapsack["contents"].append({
            "item": item,
            "amount": amount
        })
        knapsack["value"] += amount * item["unit_value"]

    return knapsack


def test():
    """ Test function """
    items = [
        {
            "w": 4,
            "v": 20
        },
        {
            "w": 3,
            "v": 18
        },
        {
            "w": 2,
            "v": 14
        },
    ]

    max_value = 7

    knapsack = fkn(items, max_value)
    print(json.dumps(knapsack, indent=2))

if __name__ == "__main__":
    test()
