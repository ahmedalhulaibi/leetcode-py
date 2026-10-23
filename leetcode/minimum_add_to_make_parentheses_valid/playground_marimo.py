import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_add_to_make_valid, run_min_add_to_make_valid
    from solution import Solution

    return Solution, assert_min_add_to_make_valid, run_min_add_to_make_valid


@app.cell
def _():
    # Example test case
    s = "())"
    expected = 1
    return expected, s


@app.cell
def _(Solution, run_min_add_to_make_valid, s):
    result = run_min_add_to_make_valid(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_min_add_to_make_valid, expected, result):
    assert_min_add_to_make_valid(result, expected)
    return


if __name__ == "__main__":
    app.run()
