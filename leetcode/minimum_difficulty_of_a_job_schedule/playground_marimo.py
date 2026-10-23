import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_difficulty, run_min_difficulty
    from solution import Solution

    return Solution, assert_min_difficulty, run_min_difficulty


@app.cell
def _():
    # Example test case
    job_difficulty = [6, 5, 4, 3, 2, 1]
    d = 2
    expected = 7
    return d, expected, job_difficulty


@app.cell
def _(Solution, d, job_difficulty, run_min_difficulty):
    result = run_min_difficulty(Solution, job_difficulty, d)
    result
    return (result,)


@app.cell
def _(assert_min_difficulty, expected, result):
    assert_min_difficulty(result, expected)
    return


if __name__ == "__main__":
    app.run()
