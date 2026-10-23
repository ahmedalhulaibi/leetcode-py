import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_sum_after_partitioning, run_max_sum_after_partitioning
    from solution import Solution

    return (
        Solution,
        assert_max_sum_after_partitioning,
        run_max_sum_after_partitioning,
    )


@app.cell
def _():
    # Example test case
    arr = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    expected = 84
    return arr, expected, k


@app.cell
def _(Solution, arr, k, run_max_sum_after_partitioning):
    result = run_max_sum_after_partitioning(Solution, arr, k)
    result
    return (result,)


@app.cell
def _(assert_max_sum_after_partitioning, expected, result):
    assert_max_sum_after_partitioning(result, expected)
    return


if __name__ == "__main__":
    app.run()
