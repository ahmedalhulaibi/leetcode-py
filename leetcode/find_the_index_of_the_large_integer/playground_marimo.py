import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_index, run_get_index
    from solution import Solution

    return Solution, assert_get_index, run_get_index


@app.cell
def _():
    # Example test case
    arr = [7, 7, 7, 7, 10, 7, 7, 7]
    expected = 4
    return arr, expected


@app.cell
def _(Solution, arr, run_get_index):
    result = run_get_index(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_get_index, expected, result):
    assert_get_index(result, expected)
    return


if __name__ == "__main__":
    app.run()
