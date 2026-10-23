import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_top_k_frequent, run_top_k_frequent
    from solution import Solution

    return Solution, assert_top_k_frequent, run_top_k_frequent


@app.cell
def _():
    # Example test case
    words: list[str] = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    expected: list[str] = ["i", "love"]
    return expected, k, words


@app.cell
def _(Solution, k, run_top_k_frequent, words: list[str]):
    result = run_top_k_frequent(Solution, words, k)
    result
    return (result,)


@app.cell
def _(assert_top_k_frequent, expected: list[str], result):
    assert_top_k_frequent(result, expected)
    return


if __name__ == "__main__":
    app.run()
