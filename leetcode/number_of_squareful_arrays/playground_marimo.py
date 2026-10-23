import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_squareful_perms, run_num_squareful_perms
    from solution import Solution

    return Solution, assert_num_squareful_perms, run_num_squareful_perms


@app.cell
def _():
    # Example test case
    nums = [1, 17, 8]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_num_squareful_perms):
    result = run_num_squareful_perms(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_num_squareful_perms, expected, result):
    assert_num_squareful_perms(result, expected)
    return


if __name__ == "__main__":
    app.run()
