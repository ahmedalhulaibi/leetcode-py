import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_crack_safe, run_crack_safe
    from solution import Solution

    return Solution, assert_crack_safe, run_crack_safe


@app.cell
def _():
    # Example test case
    n = 2
    k = 2
    expected = (2, 2)
    return expected, k, n


@app.cell
def _(Solution, k, n, run_crack_safe):
    result = run_crack_safe(Solution, n, k)
    result
    return (result,)


@app.cell
def _(assert_crack_safe, expected, result):
    assert_crack_safe(result, expected)
    return


if __name__ == "__main__":
    app.run()
