import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_ways_to_split_array, run_ways_to_split_array
    from solution import Solution

    return Solution, assert_ways_to_split_array, run_ways_to_split_array


@app.cell
def _():
    # Example test case
    nums = [10, 4, -8, 7]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_ways_to_split_array):
    result = run_ways_to_split_array(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_ways_to_split_array, expected, result):
    assert_ways_to_split_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
