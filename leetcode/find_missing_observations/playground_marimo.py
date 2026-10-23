import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_missing_rolls, run_missing_rolls
    from solution import Solution

    return Solution, assert_missing_rolls, run_missing_rolls


@app.cell
def _():
    # Example test case
    rolls = [3, 2, 4, 3]
    mean = 4
    n = 2
    expected = [6, 6]
    return expected, mean, n, rolls


@app.cell
def _(Solution, mean, n, rolls, run_missing_rolls):
    result = run_missing_rolls(Solution, rolls, mean, n)
    result
    return (result,)


@app.cell
def _(assert_missing_rolls, expected, result):
    assert_missing_rolls(result, expected)
    return


if __name__ == "__main__":
    app.run()
