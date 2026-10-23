import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_apply_operations, run_apply_operations
    from solution import Solution

    return Solution, assert_apply_operations, run_apply_operations


@app.cell
def _():
    # Example test case
    nums = [1, 2, 2, 1, 1, 0]
    expected = [1, 4, 2, 0, 0, 0]
    return expected, nums


@app.cell
def _(Solution, nums, run_apply_operations):
    result = run_apply_operations(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_apply_operations, expected, result):
    assert_apply_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
