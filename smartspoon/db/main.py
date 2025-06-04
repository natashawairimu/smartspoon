from models import Recipe
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

# Setup database connection and session
engine = create_engine('sqlite:///smartspoon.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def add_recipe():
    name = input("Enter recipe name: ").strip()
    if not name:
        print("\033[91mRecipe name cannot be empty.\033[0m")  # Bright Red
        return

    existing = session.query(Recipe).filter_by(name=name).first()
    if existing:
        print("\033[93mRecipe already exists.\033[0m")  # Bright Yellow
        return

    recipe = Recipe(name=name)
    session.add(recipe)
    session.commit()
    print("\033[92mRecipe added successfully!\033[0m")  # Bright Green

def view_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("\033[93mNo recipes found.\033[0m")  # Bright Yellow
        return
    print("\033[94mRecipes:\033[0m")  # Bright Blue
    data = [(r.id, r.name) for r in recipes]
    print(tabulate(data, headers=["ID", "Name"], tablefmt="pretty"))

def main_menu():
    while True:
        print("\nSmartSpoon Recipe Manager")
        print("1. Add Recipe")
        print("2. View All Recipes")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_recipe()
        elif choice == "2":
            view_recipes()
        elif choice == "0":
            print("\033[92mGoodbye!\033[0m")  # Bright Green
            break
        else:
            print("\033[91mInvalid choice, please try again.\033[0m")  # Bright Red

if __name__ == "__main__":
    from models import Base
    Base.metadata.create_all(engine)
    main_menu()
