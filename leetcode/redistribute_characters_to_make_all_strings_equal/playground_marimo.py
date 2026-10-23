import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_make_equal, run_make_equal
    from solution import Solution

    return Solution, assert_make_equal, run_make_equal


@app.cell
def _():
    # Example test case
    words: list[str] = ["abc", "aabc", "bc"]
    expected = True
    return expected, words


@app.cell
def _(Solution, run_make_equal, words: list[str]):
    result = run_make_equal(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_make_equal, expected, result):
    assert_make_equal(result, expected)
    return


if __name__ == "__main__":
    app.run()
