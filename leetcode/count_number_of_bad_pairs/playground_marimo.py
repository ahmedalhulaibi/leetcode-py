import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_bad_pairs, run_count_bad_pairs
    from solution import Solution

    return Solution, assert_count_bad_pairs, run_count_bad_pairs


@app.cell
def _():
    # Example test case
    nums: list[int] = [4, 1, 3, 3]
    expected = 5
    return expected, nums


@app.cell
def _(Solution, nums: list[int], run_count_bad_pairs):
    result = run_count_bad_pairs(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_count_bad_pairs, expected, result):
    assert_count_bad_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
