import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_total_fruit, run_total_fruit
    from solution import Solution

    return Solution, assert_total_fruit, run_total_fruit


@app.cell
def _():
    # Example test case
    fruits = [1, 2, 3, 2, 2]
    expected = 4
    return expected, fruits


@app.cell
def _(Solution, fruits, run_total_fruit):
    result = run_total_fruit(Solution, fruits)
    result
    return (result,)


@app.cell
def _(assert_total_fruit, expected, result):
    assert_total_fruit(result, expected)
    return


if __name__ == "__main__":
    app.run()
