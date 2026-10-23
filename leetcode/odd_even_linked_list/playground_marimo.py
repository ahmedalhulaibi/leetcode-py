import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_odd_even_list, run_odd_even_list
    from solution import Solution

    return Solution, assert_odd_even_list, run_odd_even_list


@app.cell
def _():
    # Example test case
    head_list = [1, 2, 3, 4, 5]
    expected = [1, 3, 5, 2, 4]
    return expected, head_list


@app.cell
def _(Solution, head_list, run_odd_even_list):
    result = run_odd_even_list(Solution, head_list)
    result
    return (result,)


@app.cell
def _(assert_odd_even_list, expected, result):
    assert_odd_even_list(result, expected)
    return


if __name__ == "__main__":
    app.run()
