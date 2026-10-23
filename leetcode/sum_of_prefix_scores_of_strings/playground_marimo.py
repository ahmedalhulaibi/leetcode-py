import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sum_prefix_scores, run_sum_prefix_scores
    from solution import Solution

    return Solution, assert_sum_prefix_scores, run_sum_prefix_scores


@app.cell
def _():
    # Example test case
    words = ["abc", "ab", "bc", "b"]
    expected = [5, 4, 3, 2]
    return expected, words


@app.cell
def _(Solution, run_sum_prefix_scores, words):
    result = run_sum_prefix_scores(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_sum_prefix_scores, expected, result):
    assert_sum_prefix_scores(result, expected)
    return


if __name__ == "__main__":
    app.run()
