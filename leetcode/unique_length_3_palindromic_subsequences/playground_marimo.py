import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_palindromic_subsequence, run_count_palindromic_subsequence
    from solution import Solution

    return (
        Solution,
        assert_count_palindromic_subsequence,
        run_count_palindromic_subsequence,
    )


@app.cell
def _():
    # Example test case
    s = "aabca"
    expected = 3
    return expected, s


@app.cell
def _(Solution, run_count_palindromic_subsequence, s):
    result = run_count_palindromic_subsequence(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_count_palindromic_subsequence, expected, result):
    assert_count_palindromic_subsequence(result, expected)
    return


if __name__ == "__main__":
    app.run()
