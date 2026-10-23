import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_number_operations, run_min_number_operations
    from solution import Solution

    return Solution, assert_min_number_operations, run_min_number_operations


@app.cell
def _():
    # Example test case
    target = [1, 2, 3, 2, 1]
    expected = 3
    return expected, target


@app.cell
def _(Solution, run_min_number_operations, target):
    result = run_min_number_operations(Solution, target)
    result
    return (result,)


@app.cell
def _(assert_min_number_operations, expected, result):
    assert_min_number_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
