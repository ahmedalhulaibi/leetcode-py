import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_smallest_good_base, run_smallest_good_base
    from solution import Solution

    return Solution, assert_smallest_good_base, run_smallest_good_base


@app.cell
def _():
    # Example test case
    n = "13"
    expected = "3"
    return expected, n


@app.cell
def _(Solution, n, run_smallest_good_base):
    result = run_smallest_good_base(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_smallest_good_base, expected, result):
    assert_smallest_good_base(result, expected)
    return


if __name__ == "__main__":
    app.run()
