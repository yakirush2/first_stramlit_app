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

# Display the menu using a loop
for item, description in menu.items():
    st.subheader(item)
    st.write(description)

