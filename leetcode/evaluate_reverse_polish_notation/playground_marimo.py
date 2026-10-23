import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_eval_rpn, run_eval_rpn
    from solution import Solution

    return Solution, assert_eval_rpn, run_eval_rpn


@app.cell
def _():
    # Example test case
    tokens = ["2", "1", "+", "3", "*"]
    expected = 9
    return expected, tokens


@app.cell
def _(Solution, run_eval_rpn, tokens):
    result = run_eval_rpn(Solution, tokens)
    result
    return (result,)


@app.cell
def _(assert_eval_rpn, expected, result):
    assert_eval_rpn(result, expected)
    return


if __name__ == "__main__":
    app.run()
