import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_numbers_with_unique_digits, run_count_numbers_with_unique_digits
    from solution import Solution

    return (
        Solution,
        assert_count_numbers_with_unique_digits,
        run_count_numbers_with_unique_digits,
    )


@app.cell
def _():
    # Example test case
    n = 2
    expected = 91
    return expected, n


@app.cell
def _(Solution, n, run_count_numbers_with_unique_digits):
    result = run_count_numbers_with_unique_digits(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_count_numbers_with_unique_digits, expected, result):
    assert_count_numbers_with_unique_digits(result, expected)
    return


if __name__ == "__main__":
    app.run()
