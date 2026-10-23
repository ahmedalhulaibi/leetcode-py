import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_identical_pairs, run_num_identical_pairs
    from solution import Solution

    return Solution, assert_num_identical_pairs, run_num_identical_pairs


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 1, 1, 3]
    expected = 4
    return expected, nums


@app.cell
def _(Solution, nums, run_num_identical_pairs):
    result = run_num_identical_pairs(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_num_identical_pairs, expected, result):
    assert_num_identical_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
