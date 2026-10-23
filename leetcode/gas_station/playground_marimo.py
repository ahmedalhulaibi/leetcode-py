import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_complete_circuit, run_can_complete_circuit
    from solution import Solution

    return Solution, assert_can_complete_circuit, run_can_complete_circuit


@app.cell
def _():
    # Example test case
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    expected = 3
    return cost, expected, gas


@app.cell
def _(Solution, cost, gas, run_can_complete_circuit):
    result = run_can_complete_circuit(Solution, gas, cost)
    result
    return (result,)


@app.cell
def _(assert_can_complete_circuit, expected, result):
    assert_can_complete_circuit(result, expected)
    return


if __name__ == "__main__":
    app.run()
