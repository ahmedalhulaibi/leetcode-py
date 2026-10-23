import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_partition, run_can_partition
    from solution import Solution

    return Solution, assert_can_partition, run_can_partition


@app.cell
def _():
    # Example test case
    nums = [1, 5, 11, 5]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_can_partition):
    result = run_can_partition(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_can_partition, expected, result):
    assert_can_partition(result, expected)
    return


if __name__ == "__main__":
    app.run()
