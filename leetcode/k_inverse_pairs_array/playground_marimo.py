import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_k_inverse_pairs, run_k_inverse_pairs
    from solution import Solution

    return Solution, assert_k_inverse_pairs, run_k_inverse_pairs


@app.cell
def _():
    # Example test case
    n = 3
    k = 1
    expected = 2
    return expected, k, n


@app.cell
def _(Solution, k, n, run_k_inverse_pairs):
    result = run_k_inverse_pairs(Solution, n, k)
    result
    return (result,)


@app.cell
def _(assert_k_inverse_pairs, expected, result):
    assert_k_inverse_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
