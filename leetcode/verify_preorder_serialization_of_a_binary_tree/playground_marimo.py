import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_valid_serialization, run_is_valid_serialization
    from solution import Solution

    return Solution, assert_is_valid_serialization, run_is_valid_serialization


@app.cell
def _():
    # Example test case
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    expected = True
    return expected, preorder


@app.cell
def _(Solution, preorder, run_is_valid_serialization):
    result = run_is_valid_serialization(Solution, preorder)
    result
    return (result,)


@app.cell
def _(assert_is_valid_serialization, expected, result):
    assert_is_valid_serialization(result, expected)
    return


if __name__ == "__main__":
    app.run()
