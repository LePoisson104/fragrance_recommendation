import pandas as pd
import numpy as np

def unique_notes(df, note_columns):
    unique_notes = set()

    for column in note_columns:
        for value in df[column].dropna().unique():
            notes = value.split(",")

        for note in notes:
            note = note.strip().lower()

            if note:
                unique_notes.add(note)

    return unique_notes


def parse_note(value):
    if value is None or value == "":
        return []
    
    return [note.strip() for note in value.split(",")]

def encode(df, note_columns):
    notes = unique_notes(df, note_columns)
    note_to_index = {
        note: i
        for i, note in enumerate(notes)
    }
    vector = [0] * len(notes)
    for note in notes:
        if note in note_to_index:
            vector[note_to_index[note]] = 1
    return vector