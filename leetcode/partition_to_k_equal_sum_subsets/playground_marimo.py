import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_partition_k_subsets, run_can_partition_k_subsets
    from solution import Solution

    return (
        Solution,
        assert_can_partition_k_subsets,
        run_can_partition_k_subsets,
    )


@app.cell
def _():
    # Example test case
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    expected = True
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_can_partition_k_subsets):
    result = run_can_partition_k_subsets(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_can_partition_k_subsets, expected, result):
    assert_can_partition_k_subsets(result, expected)
    return


if __name__ == "__main__":
    app.run()
