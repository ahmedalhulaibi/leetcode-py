import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_time_from_digits, run_largest_time_from_digits
    from solution import Solution

    return (
        Solution,
        assert_largest_time_from_digits,
        run_largest_time_from_digits,
    )


@app.cell
def _():
    # Example test case
    arr = [1, 2, 3, 4]
    expected = "23:41"
    return arr, expected


@app.cell
def _(Solution, arr, run_largest_time_from_digits):
    result = run_largest_time_from_digits(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_largest_time_from_digits, expected, result):
    assert_largest_time_from_digits(result, expected)
    return


if __name__ == "__main__":
    app.run()
