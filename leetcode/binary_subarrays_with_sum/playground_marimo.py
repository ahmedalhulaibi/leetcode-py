import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_subarrays_with_sum, run_num_subarrays_with_sum
    from solution import Solution

    return Solution, assert_num_subarrays_with_sum, run_num_subarrays_with_sum


@app.cell
def _():
    # Example test case
    nums = [1, 0, 1, 0, 1]
    goal = 2
    expected = 4
    return expected, goal, nums


@app.cell
def _(Solution, goal, nums, run_num_subarrays_with_sum):
    result = run_num_subarrays_with_sum(Solution, nums, goal)
    result
    return (result,)


@app.cell
def _(assert_num_subarrays_with_sum, expected, result):
    assert_num_subarrays_with_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
