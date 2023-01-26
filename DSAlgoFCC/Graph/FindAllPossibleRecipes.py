# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients.
# The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i].
# Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.
# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.
# Return a list of all the recipes that you can create. You may return the answer in any order.
# Note that two recipes may contain each other in their ingredients.

def dfs_recipe(recipe, recipe_ing_graph, supply_dict, visited, rec_stack,possible_recipes):
    visited.add(recipe)
    rec_stack.add(recipe)

    for ing in recipe_ing_graph[recipe]:
        if ing not in visited:
            if ing not in supply_dict.keys():
                if ing in recipe_ing_graph.keys():
                    if dfs_recipe(ing, recipe_ing_graph, supply_dict, visited, rec_stack,possible_recipes):
                        return True
                else:
                    return True
        elif ing in rec_stack:
            return True
    rec_stack.remove(recipe)
    supply_dict[recipe] = 'True'
    possible_recipes.add(recipe)
    return False


def findAllRecipes(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    recipe_ing_graph = {}
    for recipe_no in range(len(recipes)):
        recipe = recipes[recipe_no]
        for ing in ingredients[recipe_no]:
            if recipe in recipe_ing_graph.keys():
                recipe_ing_graph[recipe].append(ing)
            else:
                recipe_ing_graph[recipe] = [ing]

    supply_dict = {}
    for ing in supplies:
        supply_dict[ing] = 'True'

    rec_stack = set()
    visited = set()
    possible_recipes = set()
    for recipe in recipes:
        if recipe in recipe_ing_graph.keys() and recipe not in visited:
            dfs_recipe(recipe, recipe_ing_graph, supply_dict, visited, rec_stack,possible_recipes)

    return list(possible_recipes)


if __name__ == '__main__':
    recipes = ["ju","fzjnm","x","e","zpmcz","h","q"]
    ingredients = [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]]
    supplies = ["f","hveml","cpivl","d"]
    print(findAllRecipes(recipes, ingredients, supplies))
