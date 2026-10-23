import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_divide_array_into_equal_pairs, run_divide_array_into_equal_pairs
    from solution import Solution

    return (
        Solution,
        assert_divide_array_into_equal_pairs,
        run_divide_array_into_equal_pairs,
    )


@app.cell
def _():
    # Example test case
    nums = [3, 2, 3, 2, 2, 2]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_divide_array_into_equal_pairs):
    result = run_divide_array_into_equal_pairs(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_divide_array_into_equal_pairs, expected, result):
    assert_divide_array_into_equal_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
