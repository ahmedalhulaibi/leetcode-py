import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_check_possibility, run_check_possibility
    from solution import Solution

    return Solution, assert_check_possibility, run_check_possibility


@app.cell
def _():
    # Example test case
    nums = [4, 2, 3]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_check_possibility):
    result = run_check_possibility(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_check_possibility, expected, result):
    assert_check_possibility(result, expected)
    return


if __name__ == "__main__":
    app.run()
