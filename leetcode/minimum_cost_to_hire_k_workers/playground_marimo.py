import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_mincost_to_hire_workers, run_mincost_to_hire_workers
    from solution import Solution

    return (
        Solution,
        assert_mincost_to_hire_workers,
        run_mincost_to_hire_workers,
    )


@app.cell
def _():
    # Example test case
    quality = [10, 20, 5]
    wage = [70, 50, 30]
    k = 2
    expected = 105.0
    return expected, k, quality, wage


@app.cell
def _(Solution, k, quality, run_mincost_to_hire_workers, wage):
    result = run_mincost_to_hire_workers(Solution, quality, wage, k)
    result
    return (result,)


@app.cell
def _(assert_mincost_to_hire_workers, expected, result):
    assert_mincost_to_hire_workers(result, expected)
    return


if __name__ == "__main__":
    app.run()
