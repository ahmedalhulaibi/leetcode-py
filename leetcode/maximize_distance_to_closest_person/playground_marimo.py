import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_dist_to_closest, run_max_dist_to_closest
    from solution import Solution

    return Solution, assert_max_dist_to_closest, run_max_dist_to_closest


@app.cell
def _():
    # Example test case
    seats = [1, 0, 0, 0, 1, 0, 1]
    expected = 2
    return expected, seats


@app.cell
def _(Solution, run_max_dist_to_closest, seats):
    result = run_max_dist_to_closest(Solution, seats)
    result
    return (result,)


@app.cell
def _(assert_max_dist_to_closest, expected, result):
    assert_max_dist_to_closest(result, expected)
    return


if __name__ == "__main__":
    app.run()
