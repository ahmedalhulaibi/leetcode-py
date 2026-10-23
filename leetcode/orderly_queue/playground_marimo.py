import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_orderly_queue, run_orderly_queue
    from solution import Solution

    return Solution, assert_orderly_queue, run_orderly_queue


@app.cell
def _():
    # Example test case
    s = "cba"
    k = 1
    expected = "acb"
    return expected, k, s


@app.cell
def _(Solution, k, run_orderly_queue, s):
    result = run_orderly_queue(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_orderly_queue, expected, result):
    assert_orderly_queue(result, expected)
    return


if __name__ == "__main__":
    app.run()
