import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_all_recipes, run_find_all_recipes
    from solution import Solution

    return Solution, assert_find_all_recipes, run_find_all_recipes


@app.cell
def _():
    # Example test case
    recipes = ["bread", "sandwich"]
    ingredients = [["yeast", "flour"], ["bread", "meat"]]
    supplies = ["yeast", "flour", "meat"]
    expected = ["bread", "sandwich"]
    return expected, ingredients, recipes, supplies


@app.cell
def _(Solution, ingredients, recipes, run_find_all_recipes, supplies):
    result = run_find_all_recipes(Solution, recipes, ingredients, supplies)
    print(result)
    result
    return (result,)


@app.cell
def _(assert_find_all_recipes, expected, result):
    assert_find_all_recipes(result, expected)
    return


if __name__ == "__main__":
    app.run()
