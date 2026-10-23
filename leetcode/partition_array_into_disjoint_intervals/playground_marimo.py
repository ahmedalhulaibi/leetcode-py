import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_partition_disjoint, run_partition_disjoint
    from solution import Solution

    return Solution, assert_partition_disjoint, run_partition_disjoint


@app.cell
def _():
    # Example test case
    nums = [5, 0, 3, 8, 6]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_partition_disjoint):
    result = run_partition_disjoint(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_partition_disjoint, expected, result):
    assert_partition_disjoint(result, expected)
    return


if __name__ == "__main__":
    app.run()
