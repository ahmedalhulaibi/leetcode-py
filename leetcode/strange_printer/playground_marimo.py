import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_strange_printer, run_strange_printer
    from solution import Solution

    return Solution, assert_strange_printer, run_strange_printer


@app.cell
def _():
    # Example test case
    s = "aaabbb"
    expected = 2
    return expected, s


@app.cell
def _(Solution, run_strange_printer, s):
    result = run_strange_printer(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_strange_printer, expected, result):
    assert_strange_printer(result, expected)
    return


if __name__ == "__main__":
    app.run()
