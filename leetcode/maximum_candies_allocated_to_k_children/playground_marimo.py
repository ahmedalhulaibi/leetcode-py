import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_candies, run_maximum_candies
    from solution import Solution

    return Solution, assert_maximum_candies, run_maximum_candies


@app.cell
def _():
    # Example test case
    candies = [5, 8, 6]
    k = 3
    expected = 5
    return candies, expected, k


@app.cell
def _(Solution, candies, k, run_maximum_candies):
    result = run_maximum_candies(Solution, candies, k)
    result
    return (result,)


@app.cell
def _(assert_maximum_candies, expected, result):
    assert_maximum_candies(result, expected)
    return


if __name__ == "__main__":
    app.run()
