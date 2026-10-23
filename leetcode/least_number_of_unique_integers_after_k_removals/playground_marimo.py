import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_least_num_of_unique_ints, run_find_least_num_of_unique_ints
    from solution import Solution

    return (
        Solution,
        assert_find_least_num_of_unique_ints,
        run_find_least_num_of_unique_ints,
    )


@app.cell
def _():
    # Example test case
    arr = [5, 5, 4]
    k = 1
    expected = 1
    return arr, expected, k


@app.cell
def _(Solution, arr, k, run_find_least_num_of_unique_ints):
    result = run_find_least_num_of_unique_ints(Solution, arr, k)
    result
    return (result,)


@app.cell
def _(assert_find_least_num_of_unique_ints, expected, result):
    assert_find_least_num_of_unique_ints(result, expected)
    return


if __name__ == "__main__":
    app.run()
