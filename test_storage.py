import json
import tempfile
from pathlib import Path

import storage

original_file = storage.DATA_FILE

with tempfile.TemporaryDirectory() as folder:
    storage.DATA_FILE = Path(folder) / "transactions.json"

    try:
        # A missing file should give an empty list.
        assert storage.load_transactions() == []

        # Saving and loading should preserve the data.
        sample = [
            {
                "id": "TEST001",
                "date": "2026-11-25",
                "kind": "expense",
                "category": "food",
                "amount": 5.0,
                "currency": "EUR"
            }
        ]

        storage.save_transactions(sample)
        assert storage.load_transactions() == sample

        # Damaged JSON should be rejected and left unchanged.
        storage.DATA_FILE.write_text(
            "broken JSON",
            encoding="utf-8"
        )

        try:
            storage.load_transactions()
        except ValueError:
            pass
        else:
            raise AssertionError("Damaged JSON was accepted.")

        assert storage.DATA_FILE.read_text(
            encoding="utf-8"
        ) == "broken JSON"

    finally:
        storage.DATA_FILE = original_file

print("All 3 storage tests passed.")