import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_mutation, run_min_mutation
    from solution import Solution

    return Solution, assert_min_mutation, run_min_mutation


@app.cell
def _():
    # Example test case
    start_gene = "AACCGGTT"
    end_gene = "AACCGGTA"
    bank = ["AACCGGTA"]
    expected = 1
    return bank, end_gene, expected, start_gene


@app.cell
def _(Solution, bank, end_gene, run_min_mutation, start_gene):
    result = run_min_mutation(Solution, start_gene, end_gene, bank)
    result
    return (result,)


@app.cell
def _(assert_min_mutation, expected, result):
    assert_min_mutation(result, expected)
    return


if __name__ == "__main__":
    app.run()
