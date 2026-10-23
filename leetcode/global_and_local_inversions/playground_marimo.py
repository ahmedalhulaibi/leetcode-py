import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_ideal_permutation, run_is_ideal_permutation
    from solution import Solution

    return Solution, assert_is_ideal_permutation, run_is_ideal_permutation


@app.cell
def _():
    # Example test case
    nums = [1, 0, 2]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_is_ideal_permutation):
    result = run_is_ideal_permutation(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_is_ideal_permutation, expected, result):
    assert_is_ideal_permutation(result, expected)
    return


if __name__ == "__main__":
    app.run()
