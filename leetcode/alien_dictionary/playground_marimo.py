import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_alien_order, run_alien_order
    from solution import Solution

    return Solution, assert_alien_order, run_alien_order


@app.cell
def _():
    # Example test case
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    expected = "wertf"
    return expected, words


@app.cell
def _(Solution, run_alien_order, words):
    result = run_alien_order(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_alien_order, expected, result):
    assert_alien_order(result, expected)
    return


if __name__ == "__main__":
    app.run()
