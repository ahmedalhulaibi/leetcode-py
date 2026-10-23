import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_subarrays_with_k_distinct, run_subarrays_with_k_distinct
    from solution import Solution

    return (
        Solution,
        assert_subarrays_with_k_distinct,
        run_subarrays_with_k_distinct,
    )


@app.cell
def _():
    # Example test case
    nums = [1, 2, 1, 2, 3]
    k = 2
    expected = 7
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_subarrays_with_k_distinct):
    result = run_subarrays_with_k_distinct(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_subarrays_with_k_distinct, expected, result):
    assert_subarrays_with_k_distinct(result, expected)
    return


if __name__ == "__main__":
    app.run()
