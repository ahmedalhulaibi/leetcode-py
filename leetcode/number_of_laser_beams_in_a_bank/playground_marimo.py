import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_of_beams, run_number_of_beams
    from solution import Solution

    return Solution, assert_number_of_beams, run_number_of_beams


@app.cell
def _():
    # Example test case
    bank = ["011001", "000000", "010100", "001000"]
    expected = 8
    return bank, expected


@app.cell
def _(Solution, bank, run_number_of_beams):
    result = run_number_of_beams(Solution, bank)
    result
    return (result,)


@app.cell
def _(assert_number_of_beams, expected, result):
    assert_number_of_beams(result, expected)
    return


if __name__ == "__main__":
    app.run()
