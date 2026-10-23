import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_multiply, run_multiply
    from solution import Solution

    return Solution, assert_multiply, run_multiply


@app.cell
def _():
    # Example test case
    num1 = "123"
    num2 = "456"
    expected = "56088"
    return expected, num1, num2


@app.cell
def _(Solution, num1, num2, run_multiply):
    result = run_multiply(Solution, num1, num2)
    result
    return (result,)


@app.cell
def _(assert_multiply, expected, result):
    assert_multiply(result, expected)
    return


if __name__ == "__main__":
    app.run()
