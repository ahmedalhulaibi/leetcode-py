import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_partition_string, run_partition_string
    from solution import Solution

    return Solution, assert_partition_string, run_partition_string


@app.cell
def _():
    # Example test case
    s = "abacaba"
    expected = 4
    return expected, s


@app.cell
def _(Solution, run_partition_string, s):
    result = run_partition_string(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_partition_string, expected, result):
    assert_partition_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
