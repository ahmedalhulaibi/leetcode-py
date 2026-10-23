import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_next_permutation, run_next_permutation
    from solution import Solution

    return Solution, assert_next_permutation, run_next_permutation


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3]
    expected = [1, 3, 2]
    return expected, nums


@app.cell
def _(Solution, nums, run_next_permutation):
    result = run_next_permutation(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_next_permutation, expected, result):
    assert_next_permutation(result, expected)
    return


if __name__ == "__main__":
    app.run()
