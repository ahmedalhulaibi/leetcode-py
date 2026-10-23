import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_pushes, run_minimum_pushes
    from solution import Solution

    return Solution, assert_minimum_pushes, run_minimum_pushes


@app.cell
def _():
    # Example test case
    word = "abcde"
    expected = 5
    return expected, word


@app.cell
def _(Solution, run_minimum_pushes, word):
    result = run_minimum_pushes(Solution, word)
    result
    return (result,)


@app.cell
def _(assert_minimum_pushes, expected, result):
    assert_minimum_pushes(result, expected)
    return


if __name__ == "__main__":
    app.run()
