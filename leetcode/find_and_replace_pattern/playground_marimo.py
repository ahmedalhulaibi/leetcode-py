import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_and_replace_pattern, run_find_and_replace_pattern
    from solution import Solution

    return (
        Solution,
        assert_find_and_replace_pattern,
        run_find_and_replace_pattern,
    )


@app.cell
def _():
    # Example test case
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    expected = ["mee", "aqq"]
    return expected, pattern, words


@app.cell
def _(Solution, pattern, run_find_and_replace_pattern, words):
    result = run_find_and_replace_pattern(Solution, words, pattern)
    result
    return (result,)


@app.cell
def _(assert_find_and_replace_pattern, expected, result):
    assert_find_and_replace_pattern(result, expected)
    return


if __name__ == "__main__":
    app.run()
