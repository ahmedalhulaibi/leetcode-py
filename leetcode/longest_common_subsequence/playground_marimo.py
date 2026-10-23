import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_common_subsequence, run_longest_common_subsequence
    from solution import Solution

    return (
        Solution,
        assert_longest_common_subsequence,
        run_longest_common_subsequence,
    )


@app.cell
def _():
    # Example test case
    text1 = "abcde"
    text2 = "ace"
    expected = 3
    return expected, text1, text2


@app.cell
def _(Solution, run_longest_common_subsequence, text1, text2):
    result = run_longest_common_subsequence(Solution, text1, text2)
    result
    return (result,)


@app.cell
def _(assert_longest_common_subsequence, expected, result):
    assert_longest_common_subsequence(result, expected)
    return


if __name__ == "__main__":
    app.run()
