import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_add_strings, run_add_strings
    from solution import Solution

    return Solution, assert_add_strings, run_add_strings


@app.cell
def _():
    # Example test case
    num1 = "11"
    num2 = "123"
    expected = "134"
    return expected, num1, num2


@app.cell
def _(Solution, num1, num2, run_add_strings):
    result = run_add_strings(Solution, num1, num2)
    result
    return (result,)


@app.cell
def _(assert_add_strings, expected, result):
    assert_add_strings(result, expected)
    return


if __name__ == "__main__":
    app.run()
