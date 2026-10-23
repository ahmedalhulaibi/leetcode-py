import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_super_egg_drop, run_super_egg_drop
    from solution import Solution

    return Solution, assert_super_egg_drop, run_super_egg_drop


@app.cell
def _():
    # Example test case
    k = 2
    n = 6
    expected = 3
    return expected, k, n


@app.cell
def _(Solution, k, n, run_super_egg_drop):
    result = run_super_egg_drop(Solution, k, n)
    result
    return (result,)


@app.cell
def _(assert_super_egg_drop, expected, result):
    assert_super_egg_drop(result, expected)
    return


if __name__ == "__main__":
    app.run()
