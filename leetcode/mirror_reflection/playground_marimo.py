import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_mirror_reflection, run_mirror_reflection
    from solution import Solution

    return Solution, assert_mirror_reflection, run_mirror_reflection


@app.cell
def _():
    # Example test case
    p = 2
    q = 1
    expected = 2
    return expected, p, q


@app.cell
def _(Solution, p, q, run_mirror_reflection):
    result = run_mirror_reflection(Solution, p, q)
    result
    return (result,)


@app.cell
def _(assert_mirror_reflection, expected, result):
    assert_mirror_reflection(result, expected)
    return


if __name__ == "__main__":
    app.run()
