import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_pancake_sort, run_pancake_sort
    from solution import Solution

    return Solution, assert_pancake_sort, run_pancake_sort


@app.cell
def _():
    # Example test case
    arr = [3, 2, 4, 1]
    expected = [1, 2, 3, 4]
    return arr, expected


@app.cell
def _(Solution, arr, run_pancake_sort):
    result = run_pancake_sort(Solution, arr)
    result
    return (result,)


@app.cell
def _(arr, assert_pancake_sort, expected, result):
    assert_pancake_sort(result, arr, expected)
    return


if __name__ == "__main__":
    app.run()
