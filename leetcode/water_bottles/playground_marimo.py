import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_water_bottles, run_num_water_bottles
    from solution import Solution

    return Solution, assert_num_water_bottles, run_num_water_bottles


@app.cell
def _():
    # Example test case
    num_bottles = 9
    num_exchange = 3
    expected = 13
    return expected, num_bottles, num_exchange


@app.cell
def _(Solution, num_bottles, num_exchange, run_num_water_bottles):
    result = run_num_water_bottles(Solution, num_bottles, num_exchange)
    result
    return (result,)


@app.cell
def _(assert_num_water_bottles, expected, result):
    assert_num_water_bottles(result, expected)
    return


if __name__ == "__main__":
    app.run()
