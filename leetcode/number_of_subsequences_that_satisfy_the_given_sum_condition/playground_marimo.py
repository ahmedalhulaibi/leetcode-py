import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_subseq, run_num_subseq
    from solution import Solution

    return Solution, assert_num_subseq, run_num_subseq


@app.cell
def _():
    # Example test case
    nums = [3, 5, 6, 7]
    target = 9
    expected = 4
    return expected, nums, target


@app.cell
def _(Solution, nums, run_num_subseq, target):
    result = run_num_subseq(Solution, nums, target)
    result
    return (result,)


@app.cell
def _(assert_num_subseq, expected, result):
    assert_num_subseq(result, expected)
    return


if __name__ == "__main__":
    app.run()
