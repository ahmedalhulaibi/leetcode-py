import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_partition, run_partition
    from solution import Solution

    return Solution, assert_partition, run_partition


@app.cell
def _():
    # Example test case
    s = "aab"
    expected = [["a", "a", "b"], ["aa", "b"]]
    return expected, s


@app.cell
def _(Solution, run_partition, s):
    result = run_partition(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_partition, expected, result):
    assert_partition(result, expected)
    return


if __name__ == "__main__":
    app.run()
