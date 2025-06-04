from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Category, Recipe, Ingredient, Step

engine = create_engine('sqlite:///db/smartspoon.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed_categories():
    session.query(Category).delete()
    categories = [
        Category(name='Dessert'),
        Category(name='Main Course'),
        Category(name='Appetizer'),
        Category(name='Breakfast'),
    ]
    session.add_all(categories)
    session.commit()
    print("Seeded Categories")

def seed_recipes():
    session.query(Recipe).delete()
    # Fetch categories for foreign key assignment
    dessert = session.query(Category).filter_by(name='Dessert').first()
    main_course = session.query(Category).filter_by(name='Main Course').first()

    recipes = [
        Recipe(name='Chocolate Cake', description='Delicious chocolate cake', category_id=dessert.id if dessert else None),
        Recipe(name='Grilled Chicken', description='Spicy grilled chicken', category_id=main_course.id if main_course else None),
    ]
    session.add_all(recipes)
    session.commit()
    print("Seeded Recipes")

def seed_ingredients_and_steps():
    session.query(Step).delete()
    session.query(Ingredient).delete()
    # Fetch recipes for foreign key assignment
    chocolate_cake = session.query(Recipe).filter_by(name='Chocolate Cake').first()
    grilled_chicken = session.query(Recipe).filter_by(name='Grilled Chicken').first()

    ingredients = [
        Ingredient(name='Flour', quantity='2 cups', recipe_id=chocolate_cake.id if chocolate_cake else None),
        Ingredient(name='Cocoa powder', quantity='1 cup', recipe_id=chocolate_cake.id if chocolate_cake else None),
        Ingredient(name='Sugar', quantity='1.5 cups', recipe_id=chocolate_cake.id if chocolate_cake else None),
        Ingredient(name='Chicken breast', quantity='500 grams', recipe_id=grilled_chicken.id if grilled_chicken else None),
        Ingredient(name='Chili powder', quantity='2 tbsp', recipe_id=grilled_chicken.id if grilled_chicken else None),
    ]

    steps = [
        Step(step_number=1, description='Preheat oven to 350F', recipe_id=chocolate_cake.id if chocolate_cake else None),
        Step(step_number=2, description='Mix dry ingredients', recipe_id=chocolate_cake.id if chocolate_cake else None),
        Step(step_number=3, description='Bake for 30 minutes', recipe_id=chocolate_cake.id if chocolate_cake else None),
        Step(step_number=1, description='Marinate chicken with spices', recipe_id=grilled_chicken.id if grilled_chicken else None),
        Step(step_number=2, description='Grill chicken for 15 minutes', recipe_id=grilled_chicken.id if grilled_chicken else None),
    ]

    session.add_all(ingredients + steps)
    session.commit()
    print("Seeded Ingredients and Steps")

def main():
    seed_categories()
    seed_recipes()
    seed_ingredients_and_steps()
    print("Database seeding completed!")

# if __name__ == '__main__':
#     main()
