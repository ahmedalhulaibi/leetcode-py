import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_ways, run_num_ways
    from solution import Solution

    return Solution, assert_num_ways, run_num_ways


@app.cell
def _():
    # Example test case
    n = 3
    k = 2
    expected = 6
    return expected, k, n


@app.cell
def _(Solution, k, n, run_num_ways):
    result = run_num_ways(Solution, n, k)
    result
    return (result,)


@app.cell
def _(assert_num_ways, expected, result):
    assert_num_ways(result, expected)
    return


if __name__ == "__main__":
    app.run()
