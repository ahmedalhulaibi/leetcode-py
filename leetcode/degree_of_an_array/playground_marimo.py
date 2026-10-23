import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_shortest_sub_array, run_find_shortest_sub_array
    from solution import Solution

    return (
        Solution,
        assert_find_shortest_sub_array,
        run_find_shortest_sub_array,
    )


@app.cell
def _():
    # Example test case
    nums = [1, 2, 2, 3, 1]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_find_shortest_sub_array):
    result = run_find_shortest_sub_array(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_shortest_sub_array, expected, result):
    assert_find_shortest_sub_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
