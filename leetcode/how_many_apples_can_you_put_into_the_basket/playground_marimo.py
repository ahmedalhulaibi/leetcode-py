import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_number_of_apples, run_max_number_of_apples
    from solution import Solution

    return Solution, assert_max_number_of_apples, run_max_number_of_apples


@app.cell
def _():
    # Example test case
    weight = [100, 200, 150, 1000]
    expected = 4
    return expected, weight


@app.cell
def _(Solution, run_max_number_of_apples, weight):
    result = run_max_number_of_apples(Solution, weight)
    result
    return (result,)


@app.cell
def _(assert_max_number_of_apples, expected, result):
    assert_max_number_of_apples(result, expected)
    return


if __name__ == "__main__":
    app.run()
