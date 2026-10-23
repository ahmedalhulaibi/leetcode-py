import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_flip_operations, run_flip_operations
    from solution import Solution

    return Solution, assert_flip_operations, run_flip_operations


@app.cell
def _():
    # Example test case
    m = 3
    n = 1
    operations = ["Solution", "flip", "flip", "flip", "reset", "flip"]
    expected = [None, None, None, None, None]
    return expected, m, n, operations


@app.cell
def _(Solution, m, n, operations, run_flip_operations):
    result, obj = run_flip_operations(Solution, m, n, operations)
    print(result)
    obj
    return (result,)


@app.cell
def _(assert_flip_operations, expected, m, n, result):
    assert_flip_operations(result, expected, m, n)
    return


if __name__ == "__main__":
    app.run()
