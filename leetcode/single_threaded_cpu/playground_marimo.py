import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_order, run_get_order
    from solution import Solution

    return Solution, assert_get_order, run_get_order


@app.cell
def _():
    # Example test case
    tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
    expected = [0, 2, 3, 1]
    return expected, tasks


@app.cell
def _(Solution, run_get_order, tasks):
    result = run_get_order(Solution, tasks)
    result
    return (result,)


@app.cell
def _(assert_get_order, expected, result):
    assert_get_order(result, expected)
    return


if __name__ == "__main__":
    app.run()
