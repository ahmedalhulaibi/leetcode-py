import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_lexicographically_smallest_array, run_lexicographically_smallest_array
    from solution import Solution

    return (
        Solution,
        assert_lexicographically_smallest_array,
        run_lexicographically_smallest_array,
    )


@app.cell
def _():
    # Example test case
    nums = [1, 5, 3, 9, 8]
    limit = 2
    expected = [1, 3, 5, 8, 9]
    return expected, limit, nums


@app.cell
def _(Solution, limit, nums, run_lexicographically_smallest_array):
    result = run_lexicographically_smallest_array(Solution, nums, limit)
    result
    return (result,)


@app.cell
def _(assert_lexicographically_smallest_array, expected, result):
    assert_lexicographically_smallest_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
