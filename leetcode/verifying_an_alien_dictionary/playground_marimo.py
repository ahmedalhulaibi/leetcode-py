import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_alien_sorted, run_is_alien_sorted
    from solution import Solution

    return Solution, assert_is_alien_sorted, run_is_alien_sorted


@app.cell
def _():
    # Example test case
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    expected = True
    return expected, order, words


@app.cell
def _(Solution, order, run_is_alien_sorted, words):
    result = run_is_alien_sorted(Solution, words, order)
    result
    return (result,)


@app.cell
def _(assert_is_alien_sorted, expected, result):
    assert_is_alien_sorted(result, expected)
    return


if __name__ == "__main__":
    app.run()
