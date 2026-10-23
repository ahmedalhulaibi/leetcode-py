import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_least_ops_express_target, run_least_ops_express_target
    from solution import Solution

    return (
        Solution,
        assert_least_ops_express_target,
        run_least_ops_express_target,
    )


@app.cell
def _():
    # Example test case
    x = 3
    target = 19
    expected = 5
    return expected, target, x


@app.cell
def _(Solution, run_least_ops_express_target, target, x):
    result = run_least_ops_express_target(Solution, x, target)
    result
    return (result,)


@app.cell
def _(assert_least_ops_express_target, expected, result):
    assert_least_ops_express_target(result, expected)
    return


if __name__ == "__main__":
    app.run()
