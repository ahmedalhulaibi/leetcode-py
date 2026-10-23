import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_min, run_find_min
    from solution import Solution

    return Solution, assert_find_min, run_find_min


@app.cell
def _():
    # Example test case
    nums: list[int] = [3, 4, 5, 1, 2]
    expected: int = 1
    return expected, nums


@app.cell
def _(Solution, nums: list[int], run_find_min):
    result = run_find_min(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_min, expected: int, result):
    assert_find_min(result, expected)
    return


if __name__ == "__main__":
    app.run()
