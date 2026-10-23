import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_restaurant, run_find_restaurant
    from solution import Solution

    return Solution, assert_find_restaurant, run_find_restaurant


@app.cell
def _():
    # Example test case
    list1 = ["happy", "sad", "good"]
    list2 = ["sad", "happy", "good"]
    expected = ["sad", "happy"]
    return expected, list1, list2


@app.cell
def _(Solution, list1, list2, run_find_restaurant):
    result = run_find_restaurant(Solution, list1, list2)
    result
    return (result,)


@app.cell
def _(assert_find_restaurant, expected, result):
    assert_find_restaurant(result, expected)
    return


if __name__ == "__main__":
    app.run()
