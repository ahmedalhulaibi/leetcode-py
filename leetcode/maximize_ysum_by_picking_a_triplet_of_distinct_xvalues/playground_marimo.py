import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_sum_distinct_triplet, run_max_sum_distinct_triplet
    from solution import Solution

    return (
        Solution,
        assert_max_sum_distinct_triplet,
        run_max_sum_distinct_triplet,
    )


@app.cell
def _():
    # Example test case
    x = [1, 2, 1, 3, 2]
    y = [5, 3, 4, 6, 2]
    expected = 14
    return expected, x, y


@app.cell
def _(Solution, run_max_sum_distinct_triplet, x, y):
    result = run_max_sum_distinct_triplet(Solution, x, y)
    result
    return (result,)


@app.cell
def _(assert_max_sum_distinct_triplet, expected, result):
    assert_max_sum_distinct_triplet(result, expected)
    return


if __name__ == "__main__":
    app.run()
