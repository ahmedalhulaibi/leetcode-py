import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_common_prefix, run_longest_common_prefix
    from solution import Solution

    return Solution, assert_longest_common_prefix, run_longest_common_prefix


@app.cell
def _():
    # Example test case
    strs = ["flower", "flow", "flight"]
    expected = "fl"
    return expected, strs


@app.cell
def _(Solution, run_longest_common_prefix, strs):
    result = run_longest_common_prefix(Solution, strs)
    result
    return (result,)


@app.cell
def _(assert_longest_common_prefix, expected, result):
    assert_longest_common_prefix(result, expected)
    return


if __name__ == "__main__":
    app.run()
