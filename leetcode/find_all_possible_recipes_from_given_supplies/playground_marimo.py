# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo==0.25.2", "leetcode-py-sdk[practice]==0.0.0"]
# [tool.uv.sources]
# leetcode-py-sdk = { path = "../..", editable = true }
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from leetcode_py.practice import run_practice_tests

    return mo, run_practice_tests


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # 2115. Find All Possible Recipes from Given Supplies

    **Medium** · Array, Hash Table, String, Graph Theory, Topological Sort, Directed Acyclic Graph

    You have information about `n` different recipes. You are given a string array `recipes` and a 2D string array `ingredients`. The `i`th recipe has the name `recipes[i]`, and you can **create** it if you have **all** the needed ingredients from `ingredients[i]`. A recipe can also be an ingredient for **other** recipes, i.e., `ingredients[i]` may contain a string that is in `recipes`.

    You are also given a string array `supplies` containing all the ingredients that you initially have, and you have an infinite supply of all of them.

    Return *a list of all the recipes that you can create.* You may return the answer in **any order**.

    Note that two recipes may contain each other in their ingredients.

    ## Examples

    ```
    Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
    Output: ["bread"]
    Explanation:
    We can create "bread" since we have the ingredients "yeast" and "flour".
    ```

    ```
    Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
    Output: ["bread","sandwich"]
    Explanation:
    We can create "bread" since we have the ingredients "yeast" and "flour".
    We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
    ```

    ```
    Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
    Output: ["bread","sandwich","burger"]
    Explanation:
    We can create "bread" since we have the ingredients "yeast" and "flour".
    We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
    We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
    ```

    ## Constraints

    - `n == recipes.length == ingredients.length`
    - `1 <= n <= 100`
    - `1 <= ingredients[i].length, supplies.length <= 100`
    - `1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10`
    - `recipes[i]`, `ingredients[i][j]`, and `supplies[k]` consist only of lowercase English letters.
    - All the values of `recipes` and `supplies` combined are unique.
    - Each `ingredients[i]` does not contain any duplicate values.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_all_recipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
            raise NotImplementedError('Implement find_all_recipes')

    practice_exports = {'Solution': Solution}
    return (practice_exports,)


@app.cell(hide_code=True)
def _(mo):
    run_tests = mo.ui.run_button(label="Run tests")
    run_tests
    return (run_tests,)


@app.cell(hide_code=True)
def _(mo, practice_exports, run_practice_tests, run_tests):
    mo.stop(not run_tests.value, mo.md("Implement your solution, then run the tests."))
    test_result = run_practice_tests(mo.notebook_dir(), practice_exports)
    mo.vstack([
        mo.md(f"**{test_result.passed} passed · {test_result.failed} failed · "
              f"{test_result.skipped} skipped**"),
        mo.md("**All tests passed.**" if test_result.exit_code == 0 else "**Tests are not passing yet.**"),
        mo.accordion({"Test output": mo.plain_text(test_result.output)}),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Notes

    Record your approach, complexity, and edge cases here.
    """)
    return


if __name__ == "__main__":
    app.run()
