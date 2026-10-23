import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_first_missing_positive, run_first_missing_positive
    from solution import Solution

    return Solution, assert_first_missing_positive, run_first_missing_positive


@app.cell
def _():
    # Example test case
    nums: list[int] = [1, 2, 0]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums: list[int], run_first_missing_positive):
    result = run_first_missing_positive(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_first_missing_positive, expected, result):
    assert_first_missing_positive(result, expected)
    return


if __name__ == "__main__":
    app.run()
