import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_dest_city, run_dest_city
    from solution import Solution

    return Solution, assert_dest_city, run_dest_city


@app.cell
def _():
    # Example test case
    paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    expected = "Sao Paulo"
    return expected, paths


@app.cell
def _(Solution, paths, run_dest_city):
    result = run_dest_city(Solution, paths)
    result
    return (result,)


@app.cell
def _(assert_dest_city, expected, result):
    assert_dest_city(result, expected)
    return


if __name__ == "__main__":
    app.run()
