import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_monotone_increasing_digits, run_monotone_increasing_digits
    from solution import Solution

    return (
        Solution,
        assert_monotone_increasing_digits,
        run_monotone_increasing_digits,
    )


@app.cell
def _():
    # Example test case
    n = 332
    expected = 299
    return expected, n


@app.cell
def _(Solution, n, run_monotone_increasing_digits):
    result = run_monotone_increasing_digits(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_monotone_increasing_digits, expected, result):
    assert_monotone_increasing_digits(result, expected)
    return


if __name__ == "__main__":
    app.run()
