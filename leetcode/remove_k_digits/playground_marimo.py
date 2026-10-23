import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_k_digits, run_remove_k_digits
    from solution import Solution

    return Solution, assert_remove_k_digits, run_remove_k_digits


@app.cell
def _():
    # Example test case
    num = "1432219"
    k = 3
    expected = "1219"
    return expected, k, num


@app.cell
def _(Solution, k, num, run_remove_k_digits):
    result = run_remove_k_digits(Solution, num, k)
    result
    return (result,)


@app.cell
def _(assert_remove_k_digits, expected, result):
    assert_remove_k_digits(result, expected)
    return


if __name__ == "__main__":
    app.run()
