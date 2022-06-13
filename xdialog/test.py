#!/usr/bin/env python3

import xdialog

from typing import Iterable

def _test():
    print("Beginning test!")

    # Opening Files
    print("Close this.")
    assert xdialog.open_file("Close This!", [("Text File", "*.txt")]) == ''
    print("Select a file.")
    assert len(xdialog.open_file("Select a file", [("Text File", "*.txt"), ("Python File", "*.py")])) > 0
    print("Select multiple files.")
    assert isinstance(xdialog.open_file("Select multiple files.", multiple=True), Iterable)

    # Saving Files
    print("Close this.")
    assert xdialog.save_file("Close This!") == ''
    print("Save to a file.")
    assert len(xdialog.save_file("Select a file to save to", [("Text File", "*.txt")])) > 0

    # Opening a directory
    print("Close this.")
    assert xdialog.directory("Close This!") == ''
    print("Select a directory.")
    assert len(xdialog.directory("Select a directory")) > 0

    # Messages
    xdialog.info("INFO", "Close this box. It should be an info box.")
    xdialog.warning("WARNING", "Close this box. It should be a warning box.")
    xdialog.error("ERROR", "Close this box. It should be an error box.")

    # Questions
    assert xdialog.yesno("YesNo", "Close This! (If you can't, click No)") == xdialog.NO
    assert xdialog.yesno("YesNo", "Click Yes") == xdialog.YES
    assert xdialog.yesno("YesNo", "Click No") == xdialog.NO

    assert xdialog.yesnocancel("YesNoCancel", "Close This! (If you can't, click Cancel)") == xdialog.CANCEL
    assert xdialog.yesnocancel("YesNoCancel", "Click Yes") == xdialog.YES
    assert xdialog.yesnocancel("YesNoCancel", "Click No") == xdialog.NO
    assert xdialog.yesnocancel("YesNoCancel", "Click Cancel") == xdialog.CANCEL

    assert xdialog.retrycancel("RetryCancel", "Close This! (If you can't, click Cancel)") == xdialog.CANCEL
    assert xdialog.retrycancel("RetryCancel", "Click Retry") == xdialog.RETRY
    assert xdialog.retrycancel("RetryCancel", "Click Cancel") == xdialog.CANCEL

    assert xdialog.okcancel("OkCancel", "Close This! (If you can't, click Cancel)") == xdialog.CANCEL
    assert xdialog.okcancel("OkCancel", "Click Ok") == xdialog.OK
    assert xdialog.okcancel("OkCancel", "Click Cancel") == xdialog.CANCEL

    print("Test successful!")