import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_triangle_number, run_triangle_number
    from solution import Solution

    return Solution, assert_triangle_number, run_triangle_number


@app.cell
def _():
    # Example test case
    nums = [2, 2, 3, 4]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_triangle_number):
    result = run_triangle_number(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_triangle_number, expected, result):
    assert_triangle_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
