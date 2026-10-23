import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_reorder_doubled, run_can_reorder_doubled
    from solution import Solution

    return Solution, assert_can_reorder_doubled, run_can_reorder_doubled


@app.cell
def _():
    # Example test case
    arr = [3, 1, 3, 6]
    expected = False
    return arr, expected


@app.cell
def _(Solution, arr, run_can_reorder_doubled):
    result = run_can_reorder_doubled(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_can_reorder_doubled, expected, result):
    assert_can_reorder_doubled(result, expected)
    return


if __name__ == "__main__":
    app.run()
