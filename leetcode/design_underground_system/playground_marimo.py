import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_underground_system_operations, run_underground_system_operations
    from solution import UndergroundSystem

    return (
        UndergroundSystem,
        assert_underground_system_operations,
        run_underground_system_operations,
    )


@app.cell
def _():
    # Example test case
    operations = [
        "UndergroundSystem",
        "check_in",
        "check_in",
        "check_in",
        "check_out",
        "check_out",
        "check_out",
        "get_average_time",
    ]
    inputs = [
        [],
        [45, "Leyton", 3],
        [32, "Paradise", 8],
        [27, "Leyton", 10],
        [45, "Waterloo", 15],
        [27, "Waterloo", 20],
        [32, "Cambridge", 22],
        ["Paradise", "Cambridge"],
    ]
    expected = [None, None, None, None, None, None, None, 14.0]
    return expected, inputs, operations


@app.cell
def _(
    UndergroundSystem,
    inputs,
    operations,
    run_underground_system_operations,
):
    result, system = run_underground_system_operations(UndergroundSystem, operations, inputs)
    print(result)
    system
    return (result,)


@app.cell
def _(assert_underground_system_operations, expected, result):
    assert_underground_system_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
