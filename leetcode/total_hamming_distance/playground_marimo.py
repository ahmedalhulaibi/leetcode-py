import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_total_hamming_distance, run_total_hamming_distance
    from solution import Solution

    return Solution, assert_total_hamming_distance, run_total_hamming_distance


@app.cell
def _():
    # Example test case
    nums = [4, 14, 2]
    expected = 6
    return expected, nums


@app.cell
def _(Solution, nums, run_total_hamming_distance):
    result = run_total_hamming_distance(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_total_hamming_distance, expected, result):
    assert_total_hamming_distance(result, expected)
    return


if __name__ == "__main__":
    app.run()
