import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_the_longest_substring, run_find_the_longest_substring
    from solution import Solution

    return (
        Solution,
        assert_find_the_longest_substring,
        run_find_the_longest_substring,
    )


@app.cell
def _():
    # Example test case
    s = "leetcodeisgreat"
    expected = 5
    return expected, s


@app.cell
def _(Solution, run_find_the_longest_substring, s):
    result = run_find_the_longest_substring(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_find_the_longest_substring, expected, result):
    assert_find_the_longest_substring(result, expected)
    return


if __name__ == "__main__":
    app.run()
