import csv

def read_inventory():
    reorder_items = []

    try:
        with open("inventory.csv",mode="r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                item_name=row["item_name"]
                current_quantity=int(row["current_quantity"])
                reorder_threshold=int(row["reorder_threshold"])

                if current_quantity < reorder_threshold:
                    reorder_items.append({"item_name":item_name, "current_quantity":current_quantity,"reorder_threshold":reorder_threshold})
    except(FileNotFoundError):
        print("Error: inventory.csv not found")
        return[]
    return reorder_items



def display_report(reorder_items):
    print("\n Items that need reordering \n")

    if not reorder_items:
        print("No items need reordering.")
        return
    
    for item in reorder_items:
        print(f"Item name            :{item['item_name']}")
        print(f"Current Quantity     :{item['current_quantity']}")
        print(f"Reorder Threshold    :{item['reorder_threshold']}")
        print("Status               :Need Reorder")
        print("-"*40)

def save_report(reorder_items):
    fieldnames= ["item_name", "current_quantity", "reorder_threshold"]

    with open("restock_report.csv", mode="w", newline="") as report:
        writer=csv.DictWriter(report, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(reorder_items)
    print("\n Restock report saved successfully as 'restock_report.csv'")

def main():
    items=read_inventory()
    display_report(items)
    save_report(items)

if __name__=="__main__":
    main()
