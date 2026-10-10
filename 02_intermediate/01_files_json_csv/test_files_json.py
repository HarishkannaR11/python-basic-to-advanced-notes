import json

from files_json import csv_to_json, word_count


def test_word_count(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("The cat. The dog!\nthe END, end?")
    assert word_count(p) == {"the": 3, "cat": 1, "dog": 1, "end": 2}


def test_word_count_empty(tmp_path):
    p = tmp_path / "empty.txt"
    p.write_text("")
    assert word_count(p) == {}


def test_csv_to_json(tmp_path):
    src = tmp_path / "in.csv"
    dst = tmp_path / "out.json"
    src.write_text("symbol,price\nAAPL,190.5\nMSFT,410.2\n")
    assert csv_to_json(src, dst) == 2
    assert json.loads(dst.read_text()) == [
        {"symbol": "AAPL", "price": "190.5"},
        {"symbol": "MSFT", "price": "410.2"},
    ]
