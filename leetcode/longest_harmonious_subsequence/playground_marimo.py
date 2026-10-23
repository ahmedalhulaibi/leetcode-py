import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_lhs, run_find_lhs
    from solution import Solution

    return Solution, assert_find_lhs, run_find_lhs


@app.cell
def _():
    # Example test case
    nums: list[int] = [1, 3, 2, 2, 5, 2, 3, 7]
    expected = 5
    return expected, nums


@app.cell
def _(Solution, nums: list[int], run_find_lhs):
    result = run_find_lhs(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_lhs, expected, result):
    assert_find_lhs(result, expected)
    return


if __name__ == "__main__":
    app.run()
