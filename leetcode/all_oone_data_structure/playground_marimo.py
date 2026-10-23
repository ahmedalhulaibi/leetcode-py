import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_all_one, run_all_one
    from solution import AllOne

    return AllOne, assert_all_one, run_all_one


@app.cell
def _():
    # Example test case
    operations = [
        "AllOne",
        "inc",
        "inc",
        "get_max_key",
        "get_min_key",
        "inc",
        "get_max_key",
        "get_min_key",
    ]
    inputs = [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
    expected = [None, None, None, "hello", "hello", None, "hello", "leet"]
    return expected, inputs, operations


@app.cell
def _(AllOne, inputs, operations, run_all_one):
    result, all_one = run_all_one(AllOne, operations, inputs)
    print(result)
    all_one
    return (result,)


@app.cell
def _(assert_all_one, expected, result):
    assert_all_one(result, expected)
    return


if __name__ == "__main__":
    app.run()
