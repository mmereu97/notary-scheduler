"""Unde stau datele programatorului.

Pe calculatorul de dezvoltare, codul și datele stau separat:

    <rădăcină>/
    ├── Project/   codul (GitHub)
    └── Data/      notarial_scheduler.db, document_types.json, window_settings.json,
                   interventii_AAAA_LL.log, notarial_scheduler.lock (NU urcă pe GitHub)

Ca .exe (în birou) comportamentul e cel dintotdeauna: datele stau în folderul din
care pornește programul, ca toate stațiile să lucreze pe aceeași bază din rețea.
Dacă lângă .exe există un folder Data, se folosește acela.
Variabila de mediu NOTARIAT_DATA_DIR mută datele oriunde.
"""
import os
import sys

FROZEN = getattr(sys, "frozen", False)
CODE_DIR = os.path.dirname(sys.executable) if FROZEN else os.path.dirname(os.path.abspath(__file__))


def _data_dir() -> str:
    if os.environ.get("NOTARIAT_DATA_DIR"):
        return os.environ["NOTARIAT_DATA_DIR"]
    if FROZEN:
        beside_exe = os.path.join(CODE_DIR, "Data")
        return beside_exe if os.path.isdir(beside_exe) else os.getcwd()
    return os.path.join(os.path.dirname(CODE_DIR), "Data")


DATA_DIR = _data_dir()
os.makedirs(DATA_DIR, exist_ok=True)


def data_file(name: str) -> str:
    return os.path.join(DATA_DIR, name)
