import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_lexical_order, run_lexical_order
    from solution import Solution

    return Solution, assert_lexical_order, run_lexical_order


@app.cell
def _():
    # Example test case
    n = 13
    expected = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
    return expected, n


@app.cell
def _(Solution, n, run_lexical_order):
    result = run_lexical_order(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_lexical_order, expected, result):
    assert_lexical_order(result, expected)
    return


if __name__ == "__main__":
    app.run()
