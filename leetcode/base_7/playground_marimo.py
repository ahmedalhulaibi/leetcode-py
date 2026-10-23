import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_convert_to_base_7, run_convert_to_base_7
    from solution import Solution

    return Solution, assert_convert_to_base_7, run_convert_to_base_7


@app.cell
def _():
    # Example test case
    num = 100
    expected = "202"
    return expected, num


@app.cell
def _(Solution, num, run_convert_to_base_7):
    result = run_convert_to_base_7(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_convert_to_base_7, expected, result):
    assert_convert_to_base_7(result, expected)
    return


if __name__ == "__main__":
    app.run()
