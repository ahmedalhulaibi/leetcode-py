import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_repeated_substring_pattern, run_repeated_substring_pattern
    from solution import Solution

    return (
        Solution,
        assert_repeated_substring_pattern,
        run_repeated_substring_pattern,
    )


@app.cell
def _():
    # Example test case
    s = "abab"
    expected = True
    return expected, s


@app.cell
def _(Solution, run_repeated_substring_pattern, s):
    result = run_repeated_substring_pattern(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_repeated_substring_pattern, expected, result):
    assert_repeated_substring_pattern(result, expected)
    return


if __name__ == "__main__":
    app.run()
