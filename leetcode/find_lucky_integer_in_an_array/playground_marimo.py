import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_lucky, run_find_lucky
    from solution import Solution

    return Solution, assert_find_lucky, run_find_lucky


@app.cell
def _():
    # Example test case
    arr = [2, 2, 3, 4]
    expected = 2
    return arr, expected


@app.cell
def _(Solution, arr, run_find_lucky):
    result = run_find_lucky(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_find_lucky, expected, result):
    assert_find_lucky(result, expected)
    return


if __name__ == "__main__":
    app.run()
