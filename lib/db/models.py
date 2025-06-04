from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
# Naming convention for Alembic compatibility
Base = declarative_base()

# Ingredient model# Recipe model
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Relationships
    category = relationship('Category', back_populates='recipes')
    ingredients = relationship('Ingredient', back_populates='recipe', cascade='all, delete-orphan')
    steps = relationship('Step', back_populates='recipe', cascade='all, delete-orphan')

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(String)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    # Relationship
    recipe = relationship('Recipe', back_populates='ingredients')

# Category model
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relationship
    recipes = relationship('Recipe', back_populates='category')

# Step model
class Step(Base):
    __tablename__ = 'steps'

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    step_number = Column(Integer)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    # Relationship
    recipe = relationship('Recipe', back_populates='steps')


if __name__ =='__main__':
    pass
engine = create_engine('sqlite:///smartspoon.db') 
Base.metadata.create_all(engine)
