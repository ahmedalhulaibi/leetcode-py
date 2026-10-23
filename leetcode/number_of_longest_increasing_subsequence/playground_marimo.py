import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_number_of_lis, run_find_number_of_lis
    from solution import Solution

    return Solution, assert_find_number_of_lis, run_find_number_of_lis


@app.cell
def _():
    # Example test case
    nums = [1, 3, 5, 4, 7]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_find_number_of_lis):
    result = run_find_number_of_lis(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_number_of_lis, expected, result):
    assert_find_number_of_lis(result, expected)
    return


if __name__ == "__main__":
    app.run()
