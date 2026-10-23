import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_unique_binary_string, run_find_unique_binary_string
    from solution import Solution

    return (
        Solution,
        assert_find_unique_binary_string,
        run_find_unique_binary_string,
    )


@app.cell
def _():
    # Example test case
    nums = ["01", "10"]
    expected = "11"
    return expected, nums


@app.cell
def _(Solution, nums, run_find_unique_binary_string):
    result = run_find_unique_binary_string(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_unique_binary_string, expected, result):
    assert_find_unique_binary_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
