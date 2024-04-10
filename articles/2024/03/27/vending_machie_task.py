def min_coins_for_change(denominations, target):
    result = ""
    for denomination in denominations[::-1]:
        num, target = divmod(target, denomination)
        if num:
            if result:
                result += " + "
            result += f"{num}x{denomination}"
    if target != 0:
        return -1
    return result
 


denominations = [1, 5, 10]
target_change = 12
print(min_coins_for_change(denominations, target_change))

denominations = [1, 7, 15]
target_change = 21
print(min_coins_for_change(denominations, target_change))