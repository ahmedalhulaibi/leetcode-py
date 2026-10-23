import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_rotate_steps, run_find_rotate_steps
    from solution import Solution

    return Solution, assert_find_rotate_steps, run_find_rotate_steps


@app.cell
def _():
    # Example test case
    ring = "godding"
    key = "gd"
    expected = 4
    return expected, key, ring


@app.cell
def _(Solution, key, ring, run_find_rotate_steps):
    result = run_find_rotate_steps(Solution, ring, key)
    result
    return (result,)


@app.cell
def _(assert_find_rotate_steps, expected, result):
    assert_find_rotate_steps(result, expected)
    return


if __name__ == "__main__":
    app.run()
