import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_merge_alternately, run_merge_alternately
    from solution import Solution

    return Solution, assert_merge_alternately, run_merge_alternately


@app.cell
def _():
    # Example test case
    word1 = "abc"
    word2 = "pqr"
    expected = "apbqcr"
    return expected, word1, word2


@app.cell
def _(Solution, run_merge_alternately, word1, word2):
    result = run_merge_alternately(Solution, word1, word2)
    result
    return (result,)


@app.cell
def _(assert_merge_alternately, expected, result):
    assert_merge_alternately(result, expected)
    return


if __name__ == "__main__":
    app.run()
