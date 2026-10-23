import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_valid_partition, run_valid_partition
    from solution import Solution

    return Solution, assert_valid_partition, run_valid_partition


@app.cell
def _():
    # Example test case
    nums: list[int] = [4, 4, 4, 5, 6]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums: list[int], run_valid_partition):
    result = run_valid_partition(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_valid_partition, expected, result):
    assert_valid_partition(result, expected)
    return


if __name__ == "__main__":
    app.run()
