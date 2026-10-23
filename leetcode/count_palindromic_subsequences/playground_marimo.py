import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_palindromic_subsequences, run_count_palindromic_subsequences
    from solution import Solution

    return (
        Solution,
        assert_count_palindromic_subsequences,
        run_count_palindromic_subsequences,
    )


@app.cell
def _():
    # Example test case
    s = "bccb"
    expected = 6
    return expected, s


@app.cell
def _(Solution, run_count_palindromic_subsequences, s):
    result = run_count_palindromic_subsequences(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_count_palindromic_subsequences, expected, result):
    assert_count_palindromic_subsequences(result, expected)
    return


if __name__ == "__main__":
    app.run()
