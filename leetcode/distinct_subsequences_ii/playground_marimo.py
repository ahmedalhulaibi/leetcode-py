import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_distinct_subseq_ii, run_distinct_subseq_ii
    from solution import Solution

    return Solution, assert_distinct_subseq_ii, run_distinct_subseq_ii


@app.cell
def _():
    # Example test case
    s = "abc"
    expected = 7
    return expected, s


@app.cell
def _(Solution, run_distinct_subseq_ii, s):
    result = run_distinct_subseq_ii(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_distinct_subseq_ii, expected, result):
    assert_distinct_subseq_ii(result, expected)
    return


if __name__ == "__main__":
    app.run()
