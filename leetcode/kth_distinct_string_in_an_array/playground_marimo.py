import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_kth_distinct, run_kth_distinct
    from solution import Solution

    return Solution, assert_kth_distinct, run_kth_distinct


@app.cell
def _():
    # Example test case
    arr = ["d", "b", "c", "b", "c", "a"]
    k = 2
    expected = "a"
    return arr, expected, k


@app.cell
def _(Solution, arr, k, run_kth_distinct):
    result = run_kth_distinct(Solution, arr, k)
    result
    return (result,)


@app.cell
def _(assert_kth_distinct, expected, result):
    assert_kth_distinct(result, expected)
    return


if __name__ == "__main__":
    app.run()
