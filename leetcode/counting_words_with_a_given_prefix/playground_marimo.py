import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_prefix_count, run_prefix_count
    from solution import Solution

    return Solution, assert_prefix_count, run_prefix_count


@app.cell
def _():
    # Example test case
    words = ["pay", "attention", "practice", "attend"]
    pref = "at"
    expected = 2
    return expected, pref, words


@app.cell
def _(Solution, pref, run_prefix_count, words):
    result = run_prefix_count(Solution, words, pref)
    result
    return (result,)


@app.cell
def _(assert_prefix_count, expected, result):
    assert_prefix_count(result, expected)
    return


if __name__ == "__main__":
    app.run()
