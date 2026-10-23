import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_additive_number, run_is_additive_number
    from solution import Solution

    return Solution, assert_is_additive_number, run_is_additive_number


@app.cell
def _():
    # Example test case
    num = "112358"
    expected = True
    return expected, num


@app.cell
def _(Solution, num, run_is_additive_number):
    result = run_is_additive_number(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_is_additive_number, expected, result):
    assert_is_additive_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
