import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse_pairs, run_reverse_pairs
    from solution import Solution

    return Solution, assert_reverse_pairs, run_reverse_pairs


@app.cell
def _():
    # Example test case
    nums = [1, 3, 2, 3, 1]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_reverse_pairs):
    result = run_reverse_pairs(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_reverse_pairs, expected, result):
    assert_reverse_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
