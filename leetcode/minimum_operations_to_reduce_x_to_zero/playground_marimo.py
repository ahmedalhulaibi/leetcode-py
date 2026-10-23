import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_operations, run_min_operations
    from solution import Solution

    return Solution, assert_min_operations, run_min_operations


@app.cell
def _():
    # Example test case
    nums = [1, 1, 4, 2, 3]
    x = 5
    expected = 2
    return expected, nums, x


@app.cell
def _(Solution, nums, run_min_operations, x):
    result = run_min_operations(Solution, nums, x)
    result
    return (result,)


@app.cell
def _(assert_min_operations, expected, result):
    assert_min_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
