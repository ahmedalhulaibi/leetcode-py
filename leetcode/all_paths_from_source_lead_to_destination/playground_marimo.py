import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_leads_to_destination, run_leads_to_destination
    from solution import Solution

    return Solution, assert_leads_to_destination, run_leads_to_destination


@app.cell
def _():
    # Example test case
    n = 4
    edges = [[0, 1], [0, 3], [1, 2], [2, 1]]
    source = 0
    destination = 3
    expected = False
    return destination, edges, expected, n, source


@app.cell
def _(Solution, destination, edges, n, run_leads_to_destination, source):
    result = run_leads_to_destination(Solution, n, edges, source, destination)
    result
    return (result,)


@app.cell
def _(assert_leads_to_destination, expected, result):
    assert_leads_to_destination(result, expected)
    return


if __name__ == "__main__":
    app.run()
