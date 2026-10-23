import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_rabbits, run_num_rabbits
    from solution import Solution

    return Solution, assert_num_rabbits, run_num_rabbits


@app.cell
def _():
    # Example test case
    answers = [1, 1, 2]
    expected = 5
    return answers, expected


@app.cell
def _(Solution, answers, run_num_rabbits):
    result = run_num_rabbits(Solution, answers)
    result
    return (result,)


@app.cell
def _(assert_num_rabbits, expected, result):
    assert_num_rabbits(result, expected)
    return


if __name__ == "__main__":
    app.run()
