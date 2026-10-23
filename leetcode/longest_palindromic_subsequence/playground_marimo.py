import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_palindrome_subseq, run_longest_palindrome_subseq
    from solution import Solution

    return (
        Solution,
        assert_longest_palindrome_subseq,
        run_longest_palindrome_subseq,
    )


@app.cell
def _():
    # Example test case
    s = "bbbab"
    expected = 4
    return expected, s


@app.cell
def _(Solution, run_longest_palindrome_subseq, s):
    result = run_longest_palindrome_subseq(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_longest_palindrome_subseq, expected, result):
    assert_longest_palindrome_subseq(result, expected)
    return


if __name__ == "__main__":
    app.run()
