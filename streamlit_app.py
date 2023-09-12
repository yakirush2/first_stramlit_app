import streamlit

streamlit.title ('My Parents New Healthy Diner')

# Define the menu items and their descriptions
menu = {
    "Salad": "Fresh greens, tomatoes, cucumbers, and a balsamic vinaigrette dressing.",
    "Grilled Chicken Breast": "Tender grilled chicken breast with a side of steamed vegetables.",
    "Quinoa Bowl": "A nutritious bowl with quinoa, mixed vegetables, and a tahini sauce.",
    "Fruit Salad": "A medley of seasonal fruits for a refreshing dessert.",
    "Green Smoothie": "A healthy blend of spinach, banana, and almond milk.",
}

# Print the menu
print("Healthy Food Menu:")
print("-----------------")

for item, description in menu.items():
    print(f"{item}: {description}")

# Prompt the user for their choice
user_choice = input("\nPlease enter the name of the dish you'd like to order: ")

# Check if the user's choice is on the menu
if user_choice in menu:
    print(f"You have selected {user_choice}. Enjoy your meal!")
else:
    print("Sorry, that item is not on the menu. Please choose something from the menu.")
