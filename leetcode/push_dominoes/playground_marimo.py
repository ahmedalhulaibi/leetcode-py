import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_push_dominoes, run_push_dominoes
    from solution import Solution

    return Solution, assert_push_dominoes, run_push_dominoes


@app.cell
def _():
    # Example test case
    dominoes = "RR.L"
    expected = "RR.L"
    return dominoes, expected


@app.cell
def _(Solution, dominoes, run_push_dominoes):
    result = run_push_dominoes(Solution, dominoes)
    result
    return (result,)


@app.cell
def _(assert_push_dominoes, expected, result):
    assert_push_dominoes(result, expected)
    return


if __name__ == "__main__":
    app.run()
