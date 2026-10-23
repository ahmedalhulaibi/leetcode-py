import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_smallest_distance_pair, run_smallest_distance_pair
    from solution import Solution

    return Solution, assert_smallest_distance_pair, run_smallest_distance_pair


@app.cell
def _():
    # Example test case
    nums = [1, 3, 1]
    k = 1
    expected = 0
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_smallest_distance_pair):
    result = run_smallest_distance_pair(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_smallest_distance_pair, expected, result):
    assert_smallest_distance_pair(result, expected)
    return


if __name__ == "__main__":
    app.run()
