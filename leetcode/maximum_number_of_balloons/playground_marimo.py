import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_number_of_balloons, run_max_number_of_balloons
    from solution import Solution

    return Solution, assert_max_number_of_balloons, run_max_number_of_balloons


@app.cell
def _():
    # Example test case
    text = "loonbalxballpoon"
    expected = 2
    return expected, text


@app.cell
def _(Solution, run_max_number_of_balloons, text):
    result = run_max_number_of_balloons(Solution, text)
    result
    return (result,)


@app.cell
def _(assert_max_number_of_balloons, expected, result):
    assert_max_number_of_balloons(result, expected)
    return


if __name__ == "__main__":
    app.run()
