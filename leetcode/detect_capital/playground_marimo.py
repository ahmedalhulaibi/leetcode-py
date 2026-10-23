import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_detect_capital_use, run_detect_capital_use
    from solution import Solution

    return Solution, assert_detect_capital_use, run_detect_capital_use


@app.cell
def _():
    # Example test case
    word = "USA"
    expected = True
    return expected, word


@app.cell
def _(Solution, run_detect_capital_use, word):
    result = run_detect_capital_use(Solution, word)
    result
    return (result,)


@app.cell
def _(assert_detect_capital_use, expected, result):
    assert_detect_capital_use(result, expected)
    return


if __name__ == "__main__":
    app.run()
