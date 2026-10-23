import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_plus_one, run_plus_one
    from solution import Solution

    return Solution, assert_plus_one, run_plus_one


@app.cell
def _():
    # Example test case
    digits = [1, 2, 3]
    expected = [1, 2, 4]
    return digits, expected


@app.cell
def _(Solution, digits, run_plus_one):
    result = run_plus_one(Solution, digits)
    result
    return (result,)


@app.cell
def _(assert_plus_one, expected, result):
    assert_plus_one(result, expected)
    return


if __name__ == "__main__":
    app.run()
