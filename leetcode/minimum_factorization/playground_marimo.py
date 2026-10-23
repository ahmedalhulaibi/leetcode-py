import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_smallest_factorization, run_smallest_factorization
    from solution import Solution

    return Solution, assert_smallest_factorization, run_smallest_factorization


@app.cell
def _():
    # Example test case
    num = 48
    expected = 68
    return expected, num


@app.cell
def _(Solution, num, run_smallest_factorization):
    result = run_smallest_factorization(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_smallest_factorization, expected, result):
    assert_smallest_factorization(result, expected)
    return


if __name__ == "__main__":
    app.run()
