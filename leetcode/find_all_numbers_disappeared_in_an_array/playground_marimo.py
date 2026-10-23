import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_disappeared_numbers, run_find_disappeared_numbers
    from solution import Solution

    return (
        Solution,
        assert_find_disappeared_numbers,
        run_find_disappeared_numbers,
    )


@app.cell
def _():
    # Example test case
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    expected = [5, 6]
    return expected, nums


@app.cell
def _(Solution, nums, run_find_disappeared_numbers):
    result = run_find_disappeared_numbers(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_disappeared_numbers, expected, result):
    assert_find_disappeared_numbers(result, expected)
    return


if __name__ == "__main__":
    app.run()
