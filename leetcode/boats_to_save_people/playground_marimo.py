import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_rescue_boats, run_num_rescue_boats
    from solution import Solution

    return Solution, assert_num_rescue_boats, run_num_rescue_boats


@app.cell
def _():
    # Example test case
    people = [3, 2, 2, 1]
    limit = 3
    expected = 3
    return expected, limit, people


@app.cell
def _(Solution, limit, people, run_num_rescue_boats):
    result = run_num_rescue_boats(Solution, people, limit)
    result
    return (result,)


@app.cell
def _(assert_num_rescue_boats, expected, result):
    assert_num_rescue_boats(result, expected)
    return


if __name__ == "__main__":
    app.run()
