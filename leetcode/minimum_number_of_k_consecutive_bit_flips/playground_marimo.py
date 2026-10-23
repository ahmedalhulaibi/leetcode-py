import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_k_bit_flips, run_min_k_bit_flips
    from solution import Solution

    return Solution, assert_min_k_bit_flips, run_min_k_bit_flips


@app.cell
def _():
    # Example test case
    nums = [0, 1, 0]
    k = 1
    expected = 2
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_min_k_bit_flips):
    result = run_min_k_bit_flips(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_min_k_bit_flips, expected, result):
    assert_min_k_bit_flips(result, expected)
    return


if __name__ == "__main__":
    app.run()
