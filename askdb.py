# askdb.py

import sqlite3 as db

with db.connect('ask.db') as conn:
    c = conn.cursor()

    # Get Warning Words (eg kill, death, sad, ...)
    c.execute("SELECT WORD, WEIGHT FROM WARNING_WORDS")
    warnings = dict(c.fetchall())

    # Get Ignore (eg I, is, the, it, ...)
    # want a [] at end
    c.execute("SELECT WORD FROM IGNORES")
    ignores = []
    for r in c.fetchall():
        ignores.append(r[0])
