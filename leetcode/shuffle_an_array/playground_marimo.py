import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shuffle_operations, run_shuffle_operations
    from solution import Solution

    return Solution, assert_shuffle_operations, run_shuffle_operations


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3]
    operations = ["Solution", "shuffle", "reset", "shuffle"]
    expected = [None, [1, 2, 3], None]
    return expected, nums, operations


@app.cell
def _(Solution, nums, operations, run_shuffle_operations):
    result, obj = run_shuffle_operations(Solution, nums, operations)
    print(result)
    obj
    return (result,)


@app.cell
def _(assert_shuffle_operations, expected, nums, result):
    assert_shuffle_operations(result, expected, nums)
    return


if __name__ == "__main__":
    app.run()
