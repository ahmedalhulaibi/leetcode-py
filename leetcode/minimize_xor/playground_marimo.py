import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimize_xor, run_minimize_xor
    from solution import Solution

    return Solution, assert_minimize_xor, run_minimize_xor


@app.cell
def _():
    # Example test case
    num1 = 3
    num2 = 5
    expected = 3
    return expected, num1, num2


@app.cell
def _(Solution, num1, num2, run_minimize_xor):
    result = run_minimize_xor(Solution, num1, num2)
    result
    return (result,)


@app.cell
def _(assert_minimize_xor, expected, result):
    assert_minimize_xor(result, expected)
    return


if __name__ == "__main__":
    app.run()
