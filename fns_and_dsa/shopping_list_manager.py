def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            addItem = input("Enter the item to add: ").strip()
            shopping_list.append(addItem)
            print(f"Item added. You have {len(shopping_list)} in your basket")
            print()
            pass
        elif choice == '2':
            # Prompt for and remove an item
            rmitem = input("Please enter name of item you want to remove: ").strip()
            if rmitem in shopping_list:
                    shopping_list.remove(rmitem)
                    print(f"Item removed. You have {len(shopping_list)} in your basket")
                    print()
            else: print("Item is not in your list")
            print()
            pass
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            print(f"You have {len(shopping_list)} in your basket")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()