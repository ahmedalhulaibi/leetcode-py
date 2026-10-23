import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_add_operators, run_add_operators
    from solution import Solution

    return Solution, assert_add_operators, run_add_operators


@app.cell
def _():
    # Example test case
    num = "123"
    target = 6
    expected = ["1*2*3", "1+2+3"]
    return expected, num, target


@app.cell
def _(Solution, num, run_add_operators, target):
    result = run_add_operators(Solution, num, target)
    result
    return (result,)


@app.cell
def _(assert_add_operators, expected, result):
    assert_add_operators(result, expected)
    return


if __name__ == "__main__":
    app.run()
