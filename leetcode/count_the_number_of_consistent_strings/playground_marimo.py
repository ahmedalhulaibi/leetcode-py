import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_consistent_strings, run_count_consistent_strings
    from solution import Solution

    return (
        Solution,
        assert_count_consistent_strings,
        run_count_consistent_strings,
    )


@app.cell
def _():
    # Example test case
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    expected = 2
    return allowed, expected, words


@app.cell
def _(Solution, allowed, run_count_consistent_strings, words):
    result = run_count_consistent_strings(Solution, allowed, words)
    result
    return (result,)


@app.cell
def _(assert_count_consistent_strings, expected, result):
    assert_count_consistent_strings(result, expected)
    return


if __name__ == "__main__":
    app.run()
