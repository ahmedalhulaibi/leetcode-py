import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_guess_majority, run_guess_majority
    from solution import Solution

    return Solution, assert_guess_majority, run_guess_majority


@app.cell
def _():
    # Example test case
    nums = [0, 0, 1, 0, 1, 1, 1, 1]
    expected = 5
    return expected, nums


@app.cell
def _(Solution, nums, run_guess_majority):
    result = run_guess_majority(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_guess_majority, expected, nums, result):
    assert_guess_majority(result, expected, nums)
    return


if __name__ == "__main__":
    app.run()
