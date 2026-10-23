import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_size, run_minimum_size
    from solution import Solution

    return Solution, assert_minimum_size, run_minimum_size


@app.cell
def _():
    # Example test case
    nums = [9]
    max_operations = 2
    expected = 3
    return expected, max_operations, nums


@app.cell
def _(Solution, max_operations, nums, run_minimum_size):
    result = run_minimum_size(Solution, nums, max_operations)
    result
    return (result,)


@app.cell
def _(assert_minimum_size, expected, result):
    assert_minimum_size(result, expected)
    return


if __name__ == "__main__":
    app.run()
