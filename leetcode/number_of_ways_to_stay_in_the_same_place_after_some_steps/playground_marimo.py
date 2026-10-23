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
    steps = 3
    arr_len = 2
    expected = 4
    return arr_len, expected, steps


@app.cell
def _(Solution, arr_len, run_num_ways, steps):
    result = run_num_ways(Solution, steps, arr_len)
    result
    return (result,)


@app.cell
def _(assert_num_ways, expected, result):
    assert_num_ways(result, expected)
    return


if __name__ == "__main__":
    app.run()
