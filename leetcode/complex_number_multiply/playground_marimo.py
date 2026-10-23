import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_complex_number_multiply, run_complex_number_multiply
    from solution import Solution

    return (
        Solution,
        assert_complex_number_multiply,
        run_complex_number_multiply,
    )


@app.cell
def _():
    # Example test case
    num1 = "1+1i"
    num2 = "1+1i"
    expected = "0+2i"
    return expected, num1, num2


@app.cell
def _(Solution, num1, num2, run_complex_number_multiply):
    result = run_complex_number_multiply(Solution, num1, num2)
    result
    return (result,)


@app.cell
def _(assert_complex_number_multiply, expected, result):
    assert_complex_number_multiply(result, expected)
    return


if __name__ == "__main__":
    app.run()
