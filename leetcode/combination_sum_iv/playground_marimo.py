import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_combination_sum4, run_combination_sum4
    from solution import Solution

    return Solution, assert_combination_sum4, run_combination_sum4


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3]
    target = 4
    expected = 7
    return expected, nums, target


@app.cell
def _(Solution, nums, run_combination_sum4, target):
    result = run_combination_sum4(Solution, nums, target)
    result
    return (result,)


@app.cell
def _(assert_combination_sum4, expected, result):
    assert_combination_sum4(result, expected)
    return


if __name__ == "__main__":
    app.run()
