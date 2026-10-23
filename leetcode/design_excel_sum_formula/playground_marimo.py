import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_excel_sum_formula, run_excel_sum_formula
    from solution import Excel

    return Excel, assert_excel_sum_formula, run_excel_sum_formula


@app.cell
def _():
    # Example test case
    operations = ["Excel", "set", "sum", "set", "get"]
    inputs = [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
    expected = [None, None, 4, None, 6]
    return expected, inputs, operations


@app.cell
def _(Excel, inputs, operations, run_excel_sum_formula):
    result, excel = run_excel_sum_formula(Excel, operations, inputs)
    print(result)
    excel
    return (result,)


@app.cell
def _(assert_excel_sum_formula, expected, result):
    assert_excel_sum_formula(result, expected)
    return


if __name__ == "__main__":
    app.run()
