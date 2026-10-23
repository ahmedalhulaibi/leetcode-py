import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_abbreviation, run_min_abbreviation
    from solution import Solution

    return Solution, assert_min_abbreviation, run_min_abbreviation


@app.cell
def _():
    # Example test case
    target = "apple"
    dictionary = ["blade"]
    return dictionary, target


@app.cell
def _(Solution, dictionary, run_min_abbreviation, target):
    result = run_min_abbreviation(Solution, target, dictionary)
    result
    return (result,)


@app.cell
def _(assert_min_abbreviation, dictionary, result, target):
    assert_min_abbreviation(result, target, dictionary)
    return


if __name__ == "__main__":
    app.run()
