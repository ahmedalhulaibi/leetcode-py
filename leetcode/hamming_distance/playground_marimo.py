import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_hamming_distance, run_hamming_distance
    from solution import Solution

    return Solution, assert_hamming_distance, run_hamming_distance


@app.cell
def _():
    # Example test case
    x = 1
    y = 4
    expected = 2
    return expected, x, y


@app.cell
def _(Solution, run_hamming_distance, x, y):
    result = run_hamming_distance(Solution, x, y)
    result
    return (result,)


@app.cell
def _(assert_hamming_distance, expected, result):
    assert_hamming_distance(result, expected)
    return


if __name__ == "__main__":
    app.run()
