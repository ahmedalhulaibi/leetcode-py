import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_of_atoms, run_count_of_atoms
    from solution import Solution

    return Solution, assert_count_of_atoms, run_count_of_atoms


@app.cell
def _():
    # Example test case
    formula = "H2O"
    expected = "H2O"
    return expected, formula


@app.cell
def _(Solution, formula, run_count_of_atoms):
    result = run_count_of_atoms(Solution, formula)
    result
    return (result,)


@app.cell
def _(assert_count_of_atoms, expected, result):
    assert_count_of_atoms(result, expected)
    return


if __name__ == "__main__":
    app.run()
