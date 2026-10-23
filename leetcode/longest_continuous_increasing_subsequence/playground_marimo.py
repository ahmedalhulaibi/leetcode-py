import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_length_of_lcis, run_find_length_of_lcis
    from solution import Solution

    return Solution, assert_find_length_of_lcis, run_find_length_of_lcis


@app.cell
def _():
    # Example test case
    nums = [1, 3, 5, 4, 7]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_find_length_of_lcis):
    result = run_find_length_of_lcis(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_length_of_lcis, expected, result):
    assert_find_length_of_lcis(result, expected)
    return


if __name__ == "__main__":
    app.run()
