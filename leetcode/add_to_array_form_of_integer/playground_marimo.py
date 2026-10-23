import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_add_to_array_form, run_add_to_array_form
    from solution import Solution

    return Solution, assert_add_to_array_form, run_add_to_array_form


@app.cell
def _():
    # Example test case
    num = [1, 2, 0, 0]
    k = 34
    expected = [1, 2, 3, 4]
    return expected, k, num


@app.cell
def _(Solution, k, num, run_add_to_array_form):
    result = run_add_to_array_form(Solution, num, k)
    result
    return (result,)


@app.cell
def _(assert_add_to_array_form, expected, result):
    assert_add_to_array_form(result, expected)
    return


if __name__ == "__main__":
    app.run()
