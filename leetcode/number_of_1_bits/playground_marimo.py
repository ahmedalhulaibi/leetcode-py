import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_hamming_weight, run_hamming_weight
    from solution import Solution

    return Solution, assert_hamming_weight, run_hamming_weight


@app.cell
def _():
    # Example test case
    n = 11
    expected = 3
    return expected, n


@app.cell
def _(Solution, n, run_hamming_weight):
    result = run_hamming_weight(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_hamming_weight, expected, result):
    assert_hamming_weight(result, expected)
    return


if __name__ == "__main__":
    app.run()
