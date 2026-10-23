import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_of_ways, run_number_of_ways
    from solution import Solution

    return Solution, assert_number_of_ways, run_number_of_ways


@app.cell
def _():
    # Example test case
    corridor = "SSPPSPS"
    expected = 3
    return corridor, expected


@app.cell
def _(Solution, corridor, run_number_of_ways):
    result = run_number_of_ways(Solution, corridor)
    result
    return (result,)


@app.cell
def _(assert_number_of_ways, expected, result):
    assert_number_of_ways(result, expected)
    return


if __name__ == "__main__":
    app.run()
