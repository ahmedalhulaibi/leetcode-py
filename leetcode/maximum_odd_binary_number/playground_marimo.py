import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_odd_binary_number, run_maximum_odd_binary_number
    from solution import Solution

    return (
        Solution,
        assert_maximum_odd_binary_number,
        run_maximum_odd_binary_number,
    )


@app.cell
def _():
    # Example test case
    s = "0101"
    expected = "1001"
    return expected, s


@app.cell
def _(Solution, run_maximum_odd_binary_number, s):
    result = run_maximum_odd_binary_number(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_maximum_odd_binary_number, expected, result):
    assert_maximum_odd_binary_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
