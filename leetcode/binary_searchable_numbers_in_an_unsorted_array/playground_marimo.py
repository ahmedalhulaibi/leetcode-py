import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_binary_searchable_numbers, run_binary_searchable_numbers
    from solution import Solution

    return (
        Solution,
        assert_binary_searchable_numbers,
        run_binary_searchable_numbers,
    )


@app.cell
def _():
    # Example test case
    nums = [-1, 5, 2]
    expected = 1
    return expected, nums


@app.cell
def _(Solution, nums, run_binary_searchable_numbers):
    result = run_binary_searchable_numbers(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_binary_searchable_numbers, expected, result):
    assert_binary_searchable_numbers(result, expected)
    return


if __name__ == "__main__":
    app.run()
