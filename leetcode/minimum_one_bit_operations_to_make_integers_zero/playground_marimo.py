import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_one_bit_operations, run_minimum_one_bit_operations
    from solution import Solution

    return (
        Solution,
        assert_minimum_one_bit_operations,
        run_minimum_one_bit_operations,
    )


@app.cell
def _():
    # Example test case
    n = 6
    expected = 4
    return expected, n


@app.cell
def _(Solution, n, run_minimum_one_bit_operations):
    result = run_minimum_one_bit_operations(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_minimum_one_bit_operations, expected, result):
    assert_minimum_one_bit_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
