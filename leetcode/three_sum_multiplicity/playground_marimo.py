import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_three_sum_multiplicity, run_three_sum_multiplicity
    from solution import Solution

    return Solution, assert_three_sum_multiplicity, run_three_sum_multiplicity


@app.cell
def _():
    # Example test case
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    target = 8
    expected = 20
    return arr, expected, target


@app.cell
def _(Solution, arr, run_three_sum_multiplicity, target):
    result = run_three_sum_multiplicity(Solution, arr, target)
    result
    return (result,)


@app.cell
def _(assert_three_sum_multiplicity, expected, result):
    assert_three_sum_multiplicity(result, expected)
    return


if __name__ == "__main__":
    app.run()
