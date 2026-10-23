import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_search, run_search
    from solution import Solution

    return Solution, assert_search, run_search


@app.cell
def _():
    # Example test case
    secret = [-1, 0, 3, 5, 9, 12]
    target = 9
    expected = 4
    return expected, secret, target


@app.cell
def _(Solution, run_search, secret, target):
    result = run_search(Solution, secret, target)
    result
    return (result,)


@app.cell
def _(assert_search, expected, result):
    assert_search(result, expected)
    return


if __name__ == "__main__":
    app.run()
