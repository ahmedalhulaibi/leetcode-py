import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_target_sum_ways, run_find_target_sum_ways
    from solution import Solution

    return Solution, assert_find_target_sum_ways, run_find_target_sum_ways


@app.cell
def _():
    # Example test case
    nums = [1, 1, 1, 1, 1]
    target = 3
    expected = 5
    return expected, nums, target


@app.cell
def _(Solution, nums, run_find_target_sum_ways, target):
    result = run_find_target_sum_ways(Solution, nums, target)
    result
    return (result,)


@app.cell
def _(assert_find_target_sum_ways, expected, result):
    assert_find_target_sum_ways(result, expected)
    return


if __name__ == "__main__":
    app.run()
