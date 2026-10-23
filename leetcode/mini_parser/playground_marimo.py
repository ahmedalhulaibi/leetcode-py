import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_mini_parser, run_mini_parser
    from solution import Solution

    return Solution, assert_mini_parser, run_mini_parser


@app.cell
def _():
    # Example test case
    s = "324"
    expected = 324
    return expected, s


@app.cell
def _(Solution, run_mini_parser, s):
    result = run_mini_parser(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_mini_parser, expected, result):
    assert_mini_parser(result, expected)
    return


if __name__ == "__main__":
    app.run()
