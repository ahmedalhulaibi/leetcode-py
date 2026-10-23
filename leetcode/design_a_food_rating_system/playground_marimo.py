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
    # 2353. Design a Food Rating System

    **Medium** · Array, Hash Table, String, Design, Heap (Priority Queue), Ordered Set

    Design a food rating system that can do the following:

    - Modify the rating of a food item listed in the system.
    - Return the highest-rated food item for a type of cuisine in the system.

    Implement the `FoodRatings` class:

    - `FoodRatings(String[] foods, String[] cuisines, int[] ratings)` Initializes the system. The food items are described by `foods`, `cuisines`, and `ratings`, all of which have a length of `n`.
        - `foods[i]` is the name of the `i`th food,
        - `cuisines[i]` is the type of cuisine of the `i`th food, and
        - `ratings[i]` is the initial rating of the `i`th food.
    - `void changeRating(String food, int newRating)` Changes the rating of the food item with the name `food`.
    - `String highestRated(String cuisine)` Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the **lexicographically smaller** name.

    Note that a string `x` is lexicographically smaller than string `y` if `x` comes before `y` in dictionary order, that is, either `x` is a prefix of `y`, or if `i` is the first position such that `x[i] != y[i]`, then `x[i]` comes before `y[i]` in alphabetic order.

    ## Examples

    ```
    Input
    ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
    [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
    Output
    [null, "kimchi", "ramen", null, "sushi", null, "ramen"]

    Explanation
    foodRatings.highestRated("korean"); // return "kimchi"
    // "kimchi" is the highest rated korean food with a rating of 9.
    foodRatings.highestRated("japanese"); // return "ramen"
    // "ramen" is the highest rated japanese food with a rating of 14.
    foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
    foodRatings.highestRated("japanese"); // return "sushi"
    foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
    foodRatings.highestRated("japanese"); // return "ramen"
    // Both "sushi" and "ramen" have a rating of 16.
    // However, "ramen" is lexicographically smaller than "sushi".
    ```

    ## Constraints

    - `1 <= n <= 2 * 10^4`
    - `n == foods.length == cuisines.length == ratings.length`
    - `1 <= foods[i].length, cuisines[i].length <= 10`
    - `foods[i]`, `cuisines[i]` consist of lowercase English letters.
    - `1 <= ratings[i] <= 10^8`
    - All the strings in `foods` are **distinct**.
    - `food` will be the name of a food item in the system across all calls to `changeRating`.
    - `cuisine` will be a type of cuisine of **at least one** food item in the system across all calls to `highestRated`.
    - At most `2 * 10^4` calls **in total** will be made to `changeRating` and `highestRated`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class FoodRatings:

        def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]) -> None:
            raise NotImplementedError('Implement __init__')

        def change_rating(self, food: str, new_rating: int) -> None:
            raise NotImplementedError('Implement change_rating')

        def highest_rated(self, cuisine: str) -> str:
            raise NotImplementedError('Implement highest_rated')

    practice_exports = {'FoodRatings': FoodRatings}
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
