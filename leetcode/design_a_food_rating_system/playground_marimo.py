import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_food_ratings, run_food_ratings
    from solution import FoodRatings

    return FoodRatings, assert_food_ratings, run_food_ratings


@app.cell
def _():
    # Example test case
    operations = ["FoodRatings", "highest_rated", "highest_rated", "change_rating", "highest_rated"]
    inputs = [
        [["kimchi", "miso"], ["korean", "japanese"], [9, 12]],
        [["korean"]],
        [["japanese"]],
        [["miso", 15]],
        [["japanese"]],
    ]
    expected = [None, "kimchi", "miso", None, "miso"]
    return expected, inputs, operations


@app.cell
def _(FoodRatings, inputs, operations, run_food_ratings):
    result, system = run_food_ratings(FoodRatings, operations, inputs)
    print(result)
    system
    return (result,)


@app.cell
def _(assert_food_ratings, expected, result):
    assert_food_ratings(result, expected)
    return


if __name__ == "__main__":
    app.run()
