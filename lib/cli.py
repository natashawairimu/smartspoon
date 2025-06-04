from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.models import Recipe, Ingredient, Category, Step

engine = create_engine('sqlite:///smartspoon.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_recipe():
    recipe_name = input("Enter the recipe name: ").strip()
    if not recipe_name:
        print("\033[35mRecipe name cannot be empty.\033[0m")
        return
    existing_recipe = session.query(Recipe).filter_by(name=recipe_name).first()
    if existing_recipe:
        print("\033[35mRecipe already exists.\033[0m")
        return
    category_name = input("Enter category name: ").strip()
    if not category_name:
        print("\033[35mCategory name cannot be empty.\033[0m")
        return
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
        session.commit()
    new_recipe = Recipe(name=recipe_name, category=category)
    session.add(new_recipe)
    session.commit()
    print(f"\033[32mRecipe '{recipe_name}' added successfully under category '{category_name}'.\033[0m")

def add_ingredient():
    recipe_name = input("Enter the recipe name to add an ingredient to: ").strip()
    recipe = session.query(Recipe).filter_by(name=recipe_name).first()
    if not recipe:
        print("\033[35mRecipe not found.\033[0m")
        return
    ingredient_name = input("Enter ingredient name: ").strip()
    quantity = input("Enter quantity (e.g., 2 cups): ").strip()
    ingredient = Ingredient(name=ingredient_name, quantity=quantity, recipe=recipe)
    session.add(ingredient)
    session.commit()
    print(f"\033[32mAdded ingredient '{ingredient_name}' to '{recipe_name}'.\033[0m")

def add_step():
    recipe_name = input("Enter the recipe name to add a step to: ").strip()
    recipe = session.query(Recipe).filter_by(name=recipe_name).first()
    if not recipe:
        print("\033[35mRecipe not found.\033[0m")
        return
    try:
        step_number = int(input("Enter step number: "))
    except ValueError:
        print("\033[35mInvalid step number.\033[0m")
        return
    description = input("Enter step description: ").strip()
    if not description:
        print("\033[35mStep description cannot be empty.\033[0m")
        return
    step = Step(step_number=step_number, description=description, recipe=recipe)
    session.add(step)
    session.commit()
    print(f"\033[32mAdded step {step_number} to '{recipe_name}'.\033[0m")

def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("\033[33mNo recipes found.\033[0m")
        return
    for recipe in recipes:
        print(f"\n\033[1;34mRecipe: {recipe.name} (Category: {recipe.category.name if recipe.category else 'None'})\033[0m")
        print("  Ingredients:")
        for ingredient in recipe.ingredients:
            print(f"    - {ingredient.quantity} {ingredient.name}")
        print("  Steps:")
        for step in sorted(recipe.steps, key=lambda s: s.step_number):
            print(f"    {step.step_number}. {step.description}")

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add Recipe")
        print("2. Add Ingredient")
        print("3. Add Step")
        print("4. View All Recipes")
        print("5. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_recipe()
        elif choice == "2":
            add_ingredient()
        elif choice == "3":
            add_step()
        elif choice == "4":
            view_all_recipes()
        elif choice == "5":
            print("\033[36mGoodbye!\033[0m")
            break
        else:
            print("\033[35mInvalid choice. Please enter 1-5.\033[0m")

if __name__ == "__main__":
    main()
