import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_buses_to_destination, run_num_buses_to_destination
    from solution import Solution

    return (
        Solution,
        assert_num_buses_to_destination,
        run_num_buses_to_destination,
    )


@app.cell
def _():
    # Example test case
    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6
    expected = 2
    return expected, routes, source, target


@app.cell
def _(Solution, routes, run_num_buses_to_destination, source, target):
    result = run_num_buses_to_destination(Solution, routes, source, target)
    result
    return (result,)


@app.cell
def _(assert_num_buses_to_destination, expected, result):
    assert_num_buses_to_destination(result, expected)
    return


if __name__ == "__main__":
    app.run()
