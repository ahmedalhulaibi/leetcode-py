import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_matching_subseq, run_num_matching_subseq
    from solution import Solution

    return Solution, assert_num_matching_subseq, run_num_matching_subseq


@app.cell
def _():
    # Example test case
    s = "abcde"
    words = ["a", "bb", "acd", "ace"]
    expected = 3
    return expected, s, words


@app.cell
def _(Solution, run_num_matching_subseq, s, words):
    result = run_num_matching_subseq(Solution, s, words)
    result
    return (result,)


@app.cell
def _(assert_num_matching_subseq, expected, result):
    assert_num_matching_subseq(result, expected)
    return


if __name__ == "__main__":
    app.run()
