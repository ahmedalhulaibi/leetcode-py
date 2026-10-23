import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_132pattern, run_find_132pattern
    from solution import Solution

    return Solution, assert_find_132pattern, run_find_132pattern


@app.cell
def _():
    # Example test case
    nums = [3, 1, 4, 2]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_find_132pattern):
    result = run_find_132pattern(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_132pattern, expected, result):
    assert_find_132pattern(result, expected)
    return


if __name__ == "__main__":
    app.run()
