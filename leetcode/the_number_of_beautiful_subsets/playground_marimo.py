import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_beautiful_subsets, run_beautiful_subsets
    from solution import Solution

    return Solution, assert_beautiful_subsets, run_beautiful_subsets


@app.cell
def _():
    # Example test case
    nums: list[int] = [2, 4, 6]
    k = 2
    expected = 4
    return expected, k, nums


@app.cell
def _(Solution, k, nums: list[int], run_beautiful_subsets):
    result = run_beautiful_subsets(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_beautiful_subsets, expected, result):
    assert_beautiful_subsets(result, expected)
    return


if __name__ == "__main__":
    app.run()
