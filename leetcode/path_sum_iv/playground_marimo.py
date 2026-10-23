import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_path_sum, run_path_sum
    from solution import Solution

    return Solution, assert_path_sum, run_path_sum


@app.cell
def _():
    # Example test case
    nums: list[int] = [113, 215, 221]
    expected = 12
    return expected, nums


@app.cell
def _(Solution, nums: list[int], run_path_sum):
    result = run_path_sum(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_path_sum, expected, result):
    assert_path_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
