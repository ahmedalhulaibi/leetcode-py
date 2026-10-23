import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_plus_one, run_plus_one
    from solution import Solution

    return Solution, assert_plus_one, run_plus_one


@app.cell
def _():
    # Example test case
    head_vals = [1, 2, 3]
    expected_vals = [1, 2, 4]
    return expected_vals, head_vals


@app.cell
def _(Solution, head_vals, run_plus_one):
    result = run_plus_one(Solution, head_vals)
    result
    return (result,)


@app.cell
def _(assert_plus_one, expected_vals, result):
    assert_plus_one(result, expected_vals)
    return


if __name__ == "__main__":
    app.run()
