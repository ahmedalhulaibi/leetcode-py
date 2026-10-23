import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_bits, run_count_bits
    from solution import Solution

    return Solution, assert_count_bits, run_count_bits


@app.cell
def _():
    # Example test case
    n = 2
    expected = [0, 1, 1]
    return expected, n


@app.cell
def _(Solution, n, run_count_bits):
    result = run_count_bits(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_count_bits, expected, result):
    assert_count_bits(result, expected)
    return


if __name__ == "__main__":
    app.run()
