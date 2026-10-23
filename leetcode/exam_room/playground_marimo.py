import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_exam_room, run_exam_room
    from solution import ExamRoom

    return ExamRoom, assert_exam_room, run_exam_room


@app.cell
def _():
    # Example test case
    operations = ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
    inputs = [[10], [], [], [], [], [4], []]
    expected = [None, 0, 9, 4, 2, None, 5]
    return expected, inputs, operations


@app.cell
def _(ExamRoom, inputs, operations, run_exam_room):
    result, room = run_exam_room(ExamRoom, operations, inputs)
    print(result)
    room
    return (result,)


@app.cell
def _(assert_exam_room, expected, result):
    assert_exam_room(result, expected)
    return


if __name__ == "__main__":
    app.run()
