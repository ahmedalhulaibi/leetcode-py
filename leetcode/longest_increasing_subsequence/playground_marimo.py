import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_length_of_lis, run_length_of_lis
    from solution import Solution

    return Solution, assert_length_of_lis, run_length_of_lis


@app.cell
def _():
    # Example test case
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    expected = 4
    return expected, nums


@app.cell
def _(Solution, nums, run_length_of_lis):
    result = run_length_of_lis(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_length_of_lis, expected, result):
    assert_length_of_lis(result, expected)
    return


if __name__ == "__main__":
    app.run()
