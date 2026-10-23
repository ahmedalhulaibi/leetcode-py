import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_consecutive_numbers_sum, run_consecutive_numbers_sum
    from solution import Solution

    return (
        Solution,
        assert_consecutive_numbers_sum,
        run_consecutive_numbers_sum,
    )


@app.cell
def _():
    # Example test case
    n = 9
    expected = 3
    return expected, n


@app.cell
def _(Solution, n, run_consecutive_numbers_sum):
    result = run_consecutive_numbers_sum(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_consecutive_numbers_sum, expected, result):
    assert_consecutive_numbers_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
