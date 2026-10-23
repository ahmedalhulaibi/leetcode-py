import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_rotate_function, run_max_rotate_function
    from solution import Solution

    return Solution, assert_max_rotate_function, run_max_rotate_function


@app.cell
def _():
    # Example test case
    nums = [4, 3, 2, 6]
    expected = 26
    return expected, nums


@app.cell
def _(Solution, nums, run_max_rotate_function):
    result = run_max_rotate_function(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_max_rotate_function, expected, result):
    assert_max_rotate_function(result, expected)
    return


if __name__ == "__main__":
    app.run()
