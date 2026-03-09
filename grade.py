#!/usr/bin/env python3
"""
grade.py  —  Autograder for hw01-starting-with-sql

Runs each q[N].sql file, normalizes and hashes the result set, then
compares against EXPECTED_HASHES.  Writes results.json and prints a
per-question ✅ / ❌ summary.

Usage:
    python grade.py
"""

import hashlib
import json
import os
import sys
from decimal import Decimal

import psycopg2

# ---------------------------------------------------------------------------
# Database connection (matches docker-compose.yml and autograder.yml)
# ---------------------------------------------------------------------------
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "manga",
    "user": "admin",
    "password": "admin",
}

# ---------------------------------------------------------------------------
# Fill in the SHA-256 hashes produced by generate_hashes.py.
# Leave as empty strings until you have run generate_hashes.py.
# ---------------------------------------------------------------------------
EXPECTED_HASHES = {
    1:  "569bb3154fadd1f9ee8a27ba7d0f647add44fd29134577732341d444efe97194",
    2:  "a50a5adb845c71af8edbcc1a5369b0f96c51f3e6d9dce96c283d8072336b02c8",
    3:  "0d12cace13cc709ab9bab2cf0356df4e955a163f615ce20261ed10bb97c3f8d5",
    4:  "69f7bd4f63fc9a5f2bf97eee80c7cb06ec89b012e6645a2643f5f5f135215f61",
    5:  "e4fc6b1f3891309374c42224181c620adf0103bcc99c4a5a1378e12bc01dea2f",
    6:  "58eeb2776229c6c4b4d1a04c957bbf419a3694e9c1e5edff0fd742985cbfac0c",
    7:  "a6a88888e8376871d7fee21ff9f4823eb3f2ead2c153bef0e81cce9f4bd44ac6",
    8:  "51024ea6ffd0bf498f422a20bbe6070340a914dc7791812ce742285bfa3e6d2a",
    9:  "e975710b8c28ff29face4db9e06dedd6e6844175d6a2e8654d0e5a9ee33dada7",
    10: "d32c5fdd3ab139f280885b65781ce623d4831220fd8c56ccdaa85ab8e5ea29e6",
    11: "cebf84fd85381eb5a4a90d6ba221cb00f2743e8f28e14c24e4e5d0d2b4cc0cf4",
    12: "12c583fe6b12d881c365f935ac7b9f3c7f7f68cc21358b2dcb56ad5564c8a06f",
    13: "1b565de690b6b4153ee9bc5cf7d0e9270b90ee37faf4d449bf25d87fc5075235",
    14: "4832284b76d17179a02002f1248b0ece4f29be78f3744bd41ec037e7fa302196",
    15: "40de0e93cf573b64f9559d2ef79442dd665f088bf1967c0d90175ac4e5a5a985",
    16: "6ebac86413005a0ab072ea411db85c69d09d006c1d306c92d5c7348ead4e2aa3",
    17: "270b2b465adc486fc26f7bd9a1541d4a049b79a6a2ffa4e193f4f1765822b9e6",
    18: "2c9566408f473b7854f6f6b87e348b6aec834b2bf580531dc0b311d5233818f2",
    19: "de1a099960717a92f652e0d4cbd4c1ac74ec3fbfa2a2ac654119435a3140a922",
    20: "5116319bcda66ea109c2350dbb6d474e31b24b3fcd7dac22ab1f7e9fec724a27",
}

# Questions where row ORDER matters (must have correct ORDER BY).
ORDERED_QUESTIONS = [1, 4, 6, 10, 12, 14, 16, 17, 18, 20]

POINTS_PER_QUESTION = 5
TOTAL_QUESTIONS = 20


# ---------------------------------------------------------------------------
# Normalization helpers  (must stay identical to generate_hashes.py)
# ---------------------------------------------------------------------------

def normalize_value(val):
    """Normalize a single cell value for consistent hashing."""
    if val is None:
        return None
    if isinstance(val, (float, Decimal)):
        return round(float(val), 4)
    return val


def normalize_results(rows, ordered=False):
    """Normalize a list of result tuples for consistent hashing."""
    normalized = [
        tuple(normalize_value(v) for v in row)
        for row in rows
    ]
    if not ordered:
        normalized.sort(
            key=lambda row: ['' if v is None else str(v) for v in row]
        )
    return normalized


def hash_result(rows):
    """Return SHA-256 hex digest of the canonical string of normalized rows."""
    canonical = str(rows)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# SQL file runner
# ---------------------------------------------------------------------------

def run_sql_file(cur, filepath):
    """
    Read, strip, and execute a SQL file.
    Returns fetched rows or raises an exception.
    """
    with open(filepath, "r") as f:
        sql = f.read().strip()

    # Remove comment-only lines to detect truly empty files
    non_comment = "\n".join(
        line for line in sql.splitlines()
        if line.strip() and not line.strip().startswith("--")
    ).strip()

    if not non_comment:
        raise ValueError("File contains no executable SQL")

    # psycopg2 does not accept a trailing semicolon in execute()
    sql_exec = non_comment.rstrip(";").strip()
    cur.execute(sql_exec)
    return cur.fetchall()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    results = {}
    total_score = 0

    try:
        conn = psycopg2.connect(**DB_CONFIG)
    except Exception as exc:
        print(f"ERROR: Could not connect to database: {exc}", file=sys.stderr)
        sys.exit(1)

    cur = conn.cursor()

    print("=" * 60)
    print("hw01-starting-with-sql  |  Autograder")
    print("=" * 60)

    for q_num in range(1, TOTAL_QUESTIONS + 1):
        filepath = f"q{q_num:02d}.sql"
        expected = EXPECTED_HASHES.get(q_num, "")
        ordered = q_num in ORDERED_QUESTIONS

        try:
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"{filepath} not found")

            rows = run_sql_file(cur, filepath)
            conn.rollback()  # Discard any accidental writes

            normalized = normalize_results(rows, ordered=ordered)
            digest = hash_result(normalized)

            if expected and digest == expected:
                icon = "✅"
                score = POINTS_PER_QUESTION
                q_status = "pass"
            else:
                icon = "❌"
                score = 0
                q_status = "fail"

            results[str(q_num)] = {"score": score, "status": q_status}

        except Exception as exc:
            try:
                conn.rollback()
            except Exception:
                pass
            icon = "❌"
            score = 0
            results[str(q_num)] = {
                "score": score,
                "status": "error",
                "message": str(exc),
            }
            print(f"  Q{q_num:02d}: {icon}  ERROR — {exc}")
            continue

        total_score += score
        print(f"  Q{q_num:02d}: {icon}  ({score}/{POINTS_PER_QUESTION} pts)")

    cur.close()
    conn.close()

    max_score = TOTAL_QUESTIONS * POINTS_PER_QUESTION
    print("=" * 60)
    print(f"  Total: {total_score}/{max_score} pts")
    print("=" * 60)

    output = {
        "total_score": total_score,
        "max_score": max_score,
        "questions": results,
    }

    with open("results.json", "w") as f:
        json.dump(output, f, indent=2)

    print("Results saved to results.json")


if __name__ == "__main__":
    main()
