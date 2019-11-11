
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.

inventory = {
"rope" : 1,
"torch" : 6
}

added = ['Sword', 'Axe', 'Shield', 'Torch', 'Knife', 'Lighter']
removed = ['Knife', 'Torch', 'Apple', 'Apple', 'Lighter', 'Orange']



def display_inventory(inventory):
    for item, count in inventory.items():
        print(f"{item}: {count}")
    


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


def remove_from_inventory(inventory, removed_items):
    for i in removed:
        if i in inventory:
            try:
                inventory[i] -= 1
            except inventory <= 0:
                del inventory

def sort_dictionary(inventory,rev):
    inventory = sorted(inventory.items(), key=lambda k: k[1], reverse=rev)
    inventory = dict(inventory)
    return inventory



def print_table(inventory, order):


    item_title = "item name"
    count_title = "count"
    dash = " | "
    dash_char = '-'
    max_width_item = max([len(str(item)) for item in inventory.keys()] + [len(item_title)])
    max_width_count = max([len(str(count)) for count in inventory.values()] + [len(count_title)])
    horizontal_line = dash_char * (max_width_item + max_width_count + len(dash))
   
   
    print(horizontal_line)
    print(f"{item_title:>{max_width_item}}{dash}{count_title:>{max_width_count}}")
    print(horizontal_line)

    if order == "count,asc":
        inventory_items = sorted(inventory.items(), lambda tuple: tuple[1], reverse=False)
    elif order == "count,desc":
        inventory_items = sorted(inventory.items(), lambda tuple: tuple[1], reverse=True)
    else:
        inventory_items = inventory.items()

    for item, count in inventory_items:
        print(f"{item:>{max_width_item}}{dash}{count:>{max_width_count}}")

    print(horizontal_line)

def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename) as file:
        for line in file:
            items_to_add = line.split(',')
            add_to_inventory(inventory, items_to_add)


def export_inventory(inventory, filename="export_inventory.csv"):
    outputs = []
    for item, count in invenotry.items():
        for i in range(count):
            outputs.append(item)

    outputs_with_commas = ',',join(outputs)

    with open(filename, "w") as file:
        file.write(outputs_with_commas)
    