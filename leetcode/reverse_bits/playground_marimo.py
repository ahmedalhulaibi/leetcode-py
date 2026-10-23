import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse_bits, run_reverse_bits
    from solution import Solution

    return Solution, assert_reverse_bits, run_reverse_bits


@app.cell
def _():
    # Example test case
    n: int = 43261596
    expected: int = 964176192
    return expected, n


@app.cell
def _(Solution, n: int, run_reverse_bits):
    result = run_reverse_bits(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_reverse_bits, expected: int, result):
    assert_reverse_bits(result, expected)
    return


if __name__ == "__main__":
    app.run()
