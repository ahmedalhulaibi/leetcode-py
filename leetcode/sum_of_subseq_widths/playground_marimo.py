import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sum_subseq_widths, run_sum_subseq_widths
    from solution import Solution

    return Solution, assert_sum_subseq_widths, run_sum_subseq_widths


@app.cell
def _():
    # Example test case
    nums = [2, 1, 3]
    expected = 6
    return expected, nums


@app.cell
def _(Solution, nums, run_sum_subseq_widths):
    result = run_sum_subseq_widths(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_sum_subseq_widths, expected, result):
    assert_sum_subseq_widths(result, expected)
    return


if __name__ == "__main__":
    app.run()
