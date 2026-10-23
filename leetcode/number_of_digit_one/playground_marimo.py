import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_digit_one, run_count_digit_one
    from solution import Solution

    return Solution, assert_count_digit_one, run_count_digit_one


@app.cell
def _():
    # Example test case
    n: int = 13
    expected: int = 6
    return expected, n


@app.cell
def _(Solution, n: int, run_count_digit_one):
    result = run_count_digit_one(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_count_digit_one, expected: int, result):
    assert_count_digit_one(result, expected)
    return


if __name__ == "__main__":
    app.run()
