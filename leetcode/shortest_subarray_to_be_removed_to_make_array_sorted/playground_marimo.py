import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_length_of_shortest_subarray, run_find_length_of_shortest_subarray
    from solution import Solution

    return (
        Solution,
        assert_find_length_of_shortest_subarray,
        run_find_length_of_shortest_subarray,
    )


@app.cell
def _():
    # Example test case
    arr = [1, 2, 3, 10, 4, 2, 3, 5]
    expected = 3
    return arr, expected


@app.cell
def _(Solution, arr, run_find_length_of_shortest_subarray):
    result = run_find_length_of_shortest_subarray(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_find_length_of_shortest_subarray, expected, result):
    assert_find_length_of_shortest_subarray(result, expected)
    return


if __name__ == "__main__":
    app.run()
