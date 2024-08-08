inventory = [["apple", 50,0,75],
    ["banana", 100,0,50],
    ["Orange", 75,0,80], ]

def update_inventory(inventory,item_name,quantity_sold):
    for item in inventory:
        if item_name == item[0]:
            item(1)= item(1)-quantity_sold
            
def calculate_total_value(inventory):
    pass
def find_most_expensive(inventory):
    pass
def sdd_item(inventroy, item_name, quantity,prices):
    pass
update_inventory(inventory, "banana", 20)
print(inventory)
    