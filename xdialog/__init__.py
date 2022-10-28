import platform
import subprocess

from .constants import *
from .test import _test
from typing import Iterable, Union, Tuple

__all__ = [
    "open_file", "save_file", "directory",
    "info", "warning", "error",
    "yesno", "yesnocancel", "retrycancel", "okcancel",
    "YES", "NO", "CANCEL", "RETRY", "OK"
]

SYSTEM = platform.system()

# Find the best dialog for this platform. Default to tkinter.
# Using import keyword instead of __import__ for extra compatibility.
def get_dialogs():
    if SYSTEM == 'Windows':
        from . import windows_dialogs
        return windows_dialogs
    else:
        def cmd_exists(cmd):
            proc = subprocess.Popen(('which', cmd), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=False)
            proc.communicate()
            return not proc.returncode
        
        if cmd_exists('zenity'):
            from . import zenity_dialogs
            return zenity_dialogs
    
    try:
        from . import tk_dialogs
        return tk_dialogs
    except ModuleNotFoundError: pass
    
    raise ModuleNotFoundError('No dialog type is supported on this machine. Install tkinter to guarantee dialogs.')



dialogs = get_dialogs()

def open_file(title: str = None, filetypes: Iterable[Tuple[str, str]] = [("All Files", "*")], multiple: bool = False) -> Union[str, Iterable[str]]:
    '''Shows a dialog box for selecting one or more files to be opened.

    Arguments:
        title: Text to show on the header of the dialog box.
            Omitting it has system-dependent results.

        filetypes: A list of tuples specifying which filetypes to show.
            The first string is a readable name of that filetype, and
            the second string is one or more glob (e.g., * or *.txt) expression.

            Each glob in the second string is separated by spaces.

            Each tuple will appear in a dropdown of file types to select from.
            If this argument is not specified, all file types are visible.

        multiple: If True, multiple files may be selected. If False, only one file may be selected.

    Returns:
        If `multiple` is True, an iterable of selected files or an empty iterable.
        If `multiple` is False, the file that was selected or an empty string.
    '''
    return dialogs.open_file(title, filetypes, multiple)

def save_file(title: str = None, filetypes: Iterable[Tuple[str, str]] = [("All Files", "*")]) -> str:
    '''Shows a dialog box for selecting one or more files to be opened.

    Arguments:
        title: Text to show on the header of the dialog box.
            Omitting it has system-dependent results.

        filetypes: A list of tuples specifying which filetypes to show.
            The first string is a readable name of that filetype, and
            the second string is one or more glob (e.g., * or *.txt) expression.

            Each glob in the second string is separated by spaces.

            Each tuple will appear in a dropdown of file types to select from.
            If this argument is not specified, all file types are visible.

    Returns:
        The file that was selected or an empty string.
    '''
    return dialogs.save_file(title, filetypes)

def directory(title: str = None) -> str:
    '''Shows a dialog box for selecting a directory. The directory must exist to be selected.

    Arguments:
        title: Text to show on the header of the dialog box.
            Omitting it has system-dependent results.

    Returns:
        The directory that was selected or an empty string.
    '''
    return dialogs.directory(title)

def info(title: str = None, message: str = '') -> None:
    '''Shows an info dialog box.

    Arguments:
        title: Text to show on the header of the dialog box.
            Omitting it has system-dependent results.

        message: Text to show in the middle of the dialog box.
    '''
    dialogs.info(title, message)

def warning(title: str = None, message: str = '') -> None:
    '''Shows a warning dialog box.

    Arguments:
        title: Text to show on the header of the dialog box.
            Omitting it has system-dependent results.
        
        message: Text to show in the middle of the dialog box.
    '''
    dialogs.warning(title, message)

def error(title: str = None, message: str = '') -> None:
    '''Shows an error dialog box.

    Arguments:
        title: Text to show on the header of the dialog box.
            Omitting it has system-dependent results.
        
        message: Text to show in the middle of the dialog box.
    '''
    dialogs.error(title, message)

def yesno(title: str = None, message: str = '') -> int:
    '''Shows a question dialog box with the buttons "Yes" and "No".

    Arguments:
        title: Text to show on the header of the dialog box.
            Omitting it has system-dependent results.
        
        message: Text to show in the middle of the dialog box.
    
    Returns:
        `xdialog.YES` or `xdialog.NO`. Closing the box results in `xdialog.NO`.
    '''
    return dialogs.yesno(title, message)

def yesnocancel(title: str = None, message: str = '') -> int:
    '''Shows a question dialog box with the buttons "Yes", "No", and "Cancel".

    Arguments:
        title: Text to show on the header of the dialog box.
            Omitting it has system-dependent results.
        
        message: Text to show in the middle of the dialog box.
    
    Returns:
        `xdialog.YES`, `xdialog.NO`, or `xdialog.CANCEL`. Closing the box results in `xdialog.CANCEL`.
    '''
    return dialogs.yesnocancel(title, message)

def retrycancel(title: str = None, message: str = '') -> int:
    '''Shows a question dialog box with the buttons "Retry" and "Cancel".

    Arguments:
        title: Text to show on the header of the dialog box.
            Omitting it has system-dependent results.
        
        message: Text to show in the middle of the dialog box.
    
    Returns:
        `xdialog.RETRY` or `xdialog.CANCEL`. Closing the box results in `xdialog.CANCEL`.
    '''
    return dialogs.retrycancel(title, message)

def okcancel(title: str = None, message: str = '') -> int:
    '''Shows a question dialog box with the buttons "Ok" and "Cancel".

    Arguments:
        title: Text to show on the header of the dialog box.
            Omitting it has system-dependent results.
        
        message: Text to show in the middle of the dialog box.
    
    Returns:
        `xdialog.OK` or `xdialog.CANCEL`. Closing the box results in `xdialog.CANCEL`.
    '''
    return dialogs.okcancel(title, message)