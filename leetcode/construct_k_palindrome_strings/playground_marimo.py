import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_construct, run_can_construct
    from solution import Solution

    return Solution, assert_can_construct, run_can_construct


@app.cell
def _():
    # Example test case
    s = "annabelle"
    k = 2
    expected = True
    return expected, k, s


@app.cell
def _(Solution, k, run_can_construct, s):
    result = run_can_construct(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_can_construct, expected, result):
    assert_can_construct(result, expected)
    return


if __name__ == "__main__":
    app.run()
