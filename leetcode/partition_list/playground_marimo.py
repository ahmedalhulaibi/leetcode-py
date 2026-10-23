import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_partition, run_partition
    from solution import Solution

    return Solution, assert_partition, run_partition


@app.cell
def _():
    # Example test case
    head_list = [1, 4, 3, 2, 5, 2]
    x = 3
    expected_list = [1, 2, 2, 4, 3, 5]
    return expected_list, head_list, x


@app.cell
def _(Solution, head_list, run_partition, x):
    result = run_partition(Solution, head_list, x)
    result
    return (result,)


@app.cell
def _(assert_partition, expected_list, result):
    assert_partition(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
