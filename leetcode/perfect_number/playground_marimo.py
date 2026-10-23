import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_check_perfect_number, run_check_perfect_number
    from solution import Solution

    return Solution, assert_check_perfect_number, run_check_perfect_number


@app.cell
def _():
    # Example test case
    num = 28
    expected = True
    return expected, num


@app.cell
def _(Solution, num, run_check_perfect_number):
    result = run_check_perfect_number(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_check_perfect_number, expected, result):
    assert_check_perfect_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
