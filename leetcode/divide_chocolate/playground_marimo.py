import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximize_sweetness, run_maximize_sweetness
    from solution import Solution

    return Solution, assert_maximize_sweetness, run_maximize_sweetness


@app.cell
def _():
    # Example test case
    sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 5
    expected = 6
    return expected, k, sweetness


@app.cell
def _(Solution, k, run_maximize_sweetness, sweetness):
    result = run_maximize_sweetness(Solution, sweetness, k)
    result
    return (result,)


@app.cell
def _(assert_maximize_sweetness, expected, result):
    assert_maximize_sweetness(result, expected)
    return


if __name__ == "__main__":
    app.run()
