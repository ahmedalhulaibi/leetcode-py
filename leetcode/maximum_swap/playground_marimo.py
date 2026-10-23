import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_swap, run_maximum_swap
    from solution import Solution

    return Solution, assert_maximum_swap, run_maximum_swap


@app.cell
def _():
    # Example test case
    num = 2736
    expected = 7236
    return expected, num


@app.cell
def _(Solution, num, run_maximum_swap):
    result = run_maximum_swap(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_maximum_swap, expected, result):
    assert_maximum_swap(result, expected)
    return


if __name__ == "__main__":
    app.run()
