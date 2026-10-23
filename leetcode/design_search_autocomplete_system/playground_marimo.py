import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_autocomplete_system, run_autocomplete_system
    from solution import AutocompleteSystem

    return (
        AutocompleteSystem,
        assert_autocomplete_system,
        run_autocomplete_system,
    )


@app.cell
def _():
    # Example test case
    operations = ["AutocompleteSystem", "input", "input", "input", "input"]
    inputs = [
        [["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]],
        ["i"],
        [" "],
        ["a"],
        ["#"],
    ]
    expected = [
        None,
        ["i love you", "island", "i love leetcode"],
        ["i love you", "i love leetcode"],
        [],
        [],
    ]
    return expected, inputs, operations


@app.cell
def _(AutocompleteSystem, inputs, operations, run_autocomplete_system):
    result, system = run_autocomplete_system(AutocompleteSystem, operations, inputs)
    print(result)
    system
    return (result,)


@app.cell
def _(assert_autocomplete_system, expected, result):
    assert_autocomplete_system(result, expected)
    return


if __name__ == "__main__":
    app.run()
