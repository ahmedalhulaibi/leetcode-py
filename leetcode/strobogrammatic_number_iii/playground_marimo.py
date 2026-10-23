import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_strobogrammatic_in_range, run_strobogrammatic_in_range
    from solution import Solution

    return (
        Solution,
        assert_strobogrammatic_in_range,
        run_strobogrammatic_in_range,
    )


@app.cell
def _():
    # Example test case
    low = "50"
    high = "100"
    expected = 3
    return expected, high, low


@app.cell
def _(Solution, high, low, run_strobogrammatic_in_range):
    result = run_strobogrammatic_in_range(Solution, low, high)
    result
    return (result,)


@app.cell
def _(assert_strobogrammatic_in_range, expected, result):
    assert_strobogrammatic_in_range(result, expected)
    return


if __name__ == "__main__":
    app.run()
