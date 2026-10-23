import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sum_even_after_queries, run_sum_even_after_queries
    from solution import Solution

    return Solution, assert_sum_even_after_queries, run_sum_even_after_queries


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    expected = [8, 6, 2, 4]
    return expected, nums, queries


@app.cell
def _(Solution, nums, queries, run_sum_even_after_queries):
    result = run_sum_even_after_queries(Solution, nums, queries)
    result
    return (result,)


@app.cell
def _(assert_sum_even_after_queries, expected, result):
    assert_sum_even_after_queries(result, expected)
    return


if __name__ == "__main__":
    app.run()
