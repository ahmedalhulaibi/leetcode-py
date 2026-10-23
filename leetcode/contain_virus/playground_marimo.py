import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_contain_virus, run_contain_virus
    from solution import Solution

    return Solution, assert_contain_virus, run_contain_virus


@app.cell
def _():
    # Example test case
    is_infected = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    expected = 10
    return expected, is_infected


@app.cell
def _(Solution, is_infected, run_contain_virus):
    result = run_contain_virus(Solution, is_infected)
    result
    return (result,)


@app.cell
def _(assert_contain_virus, expected, result):
    assert_contain_virus(result, expected)
    return


if __name__ == "__main__":
    app.run()
