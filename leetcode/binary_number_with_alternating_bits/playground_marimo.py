import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_has_alternating_bits, run_has_alternating_bits
    from solution import Solution

    return Solution, assert_has_alternating_bits, run_has_alternating_bits


@app.cell
def _():
    # Example test case
    n = 5
    expected = True
    return expected, n


@app.cell
def _(Solution, n, run_has_alternating_bits):
    result = run_has_alternating_bits(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_has_alternating_bits, expected, result):
    assert_has_alternating_bits(result, expected)
    return


if __name__ == "__main__":
    app.run()
