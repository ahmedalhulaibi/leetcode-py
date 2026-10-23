import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_pairs, run_find_pairs
    from solution import Solution

    return Solution, assert_find_pairs, run_find_pairs


@app.cell
def _():
    # Example test case
    nums = [3, 1, 4, 1, 5]
    k = 2
    expected = 2
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_find_pairs):
    result = run_find_pairs(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_find_pairs, expected, result):
    assert_find_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
