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
    nums = [0, 1, 1, 1, 0, 0]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_min_operations):
    result = run_min_operations(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_min_operations, expected, result):
    assert_min_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
