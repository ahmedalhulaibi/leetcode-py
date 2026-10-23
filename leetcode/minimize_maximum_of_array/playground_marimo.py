import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimize_array_value, run_minimize_array_value
    from solution import Solution

    return Solution, assert_minimize_array_value, run_minimize_array_value


@app.cell
def _():
    # Example test case
    nums = [3, 7, 1, 6]
    expected = 5
    return expected, nums


@app.cell
def _(Solution, nums, run_minimize_array_value):
    result = run_minimize_array_value(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_minimize_array_value, expected, result):
    assert_minimize_array_value(result, expected)
    return


if __name__ == "__main__":
    app.run()
