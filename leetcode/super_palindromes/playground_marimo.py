import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_super_palindromes_in_range, run_super_palindromes_in_range
    from solution import Solution

    return (
        Solution,
        assert_super_palindromes_in_range,
        run_super_palindromes_in_range,
    )


@app.cell
def _():
    # Example test case
    left = "4"
    right = "1000"
    expected = 4
    return expected, left, right


@app.cell
def _(Solution, left, right, run_super_palindromes_in_range):
    result = run_super_palindromes_in_range(Solution, left, right)
    result
    return (result,)


@app.cell
def _(assert_super_palindromes_in_range, expected, result):
    assert_super_palindromes_in_range(result, expected)
    return


if __name__ == "__main__":
    app.run()
