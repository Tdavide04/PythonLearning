class RecipeManager:
    def __init__(self) -> None:
        self.recipes: dict = {}

    def create_recipe(self, name: str, ingredients: list):
        
        if name not in self.recipes:
            self.recipes[name] = ingredients
            return self.recipes
        else:
            raise ValueError("La ricetta esiste già")
        
    def add_ingredient(self, recipe_name: str, ingredient: str):

        if recipe_name in self.recipes:
            self.recipes[recipe_name].append(ingredient)
            return self.recipes
        else:
            raise ValueError("La ricetta non eiste")
        
    def remove_ingredient(self, recipe_name, ingredient):

        if recipe_name in self.recipes:
            if ingredient in self.recipes[recipe_name]:
                self.recipes[recipe_name].remove(ingredient)
        return self.recipes
        
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient:str):

        if recipe_name in self.recipes:
            if old_ingredient in self.recipes[recipe_name]:
                if new_ingredient not in self.recipes[recipe_name]:
                    index = self.recipes[recipe_name].index(old_ingredient)
                    self.recipes[recipe_name][index] = new_ingredient
        
        return self.recipes
    
    def list_recipes(self):
        
        return list(self.recipes.keys())
    
    def list_ingredients(self, recipe_name):

        if recipe_name in self.recipes:
            return self.recipes[recipe_name]
    
    def search_recipe_by_ingredient(self, ingredient):

        found_recipes = {}
        for recipe_name, ingredients in self.recipes.items():
            if ingredient in ingredient:
                found_recipes[recipe_name] = ingredients
        
        if found_recipes:
            return found_recipes


manager = RecipeManager()

print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
print(manager.add_ingredient("Torta di mele", "Zucchero"))
print(manager.list_recipes()) # ['Torta di mele']
print(manager.list_ingredients("Torta di mele"))
print(manager.search_recipe_by_ingredient("Uova"))


