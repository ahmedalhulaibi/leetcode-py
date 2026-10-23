import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_satisfied, run_max_satisfied
    from solution import Solution

    return Solution, assert_max_satisfied, run_max_satisfied


@app.cell
def _():
    # Example test case
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes = 3
    expected = 16
    return customers, expected, grumpy, minutes


@app.cell
def _(Solution, customers, grumpy, minutes, run_max_satisfied):
    result = run_max_satisfied(Solution, customers, grumpy, minutes)
    result
    return (result,)


@app.cell
def _(assert_max_satisfied, expected, result):
    assert_max_satisfied(result, expected)
    return


if __name__ == "__main__":
    app.run()
