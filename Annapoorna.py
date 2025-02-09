import ast

def min_menu_items(preferences):
    all_items = set(item for items in preferences.values() for item in items)
    remaining_customers = set(preferences.keys())
    menu_count = 0

    while remaining_customers:
        best_item = None
        max_covered = 0
        coverage_map = {}

        for item in all_items:
            covered_customers = {c for c in remaining_customers if item in preferences[c]}
            coverage_map[item] = covered_customers

            if len(covered_customers) > max_covered:
                max_covered = len(covered_customers)
                best_item = item

        if best_item is None:
            break

        menu_count += 1
        remaining_customers -= coverage_map[best_item]
        all_items.remove(best_item)

    return menu_count

n = int(input().strip())
m = int(input().strip()) 
preferences = {}

for i in range(m):
    prefs = ast.literal_eval(input().strip())
    preferences[i] = prefs

result = min_menu_items(preferences)
print(result)
