# xdialog
A cross-platform wrapper for native dialogs written entirely in python.
It's also designed to be portable and lightweight (it only uses the standard library).

You can install xdialog through pip...

```
pip install xdialog
```

Or you can copy and paste the xdialog folder into the root of your project if pip isn't available; this is possible because xdialog only uses modules in the standard library.

Here's how xdialog determines what dialogs to use:

- On Windows, xdialog uses the built-in ctypes module to interface directly with system dialogs.
- On MacOS, it uses AppleScript to interface directly with system dialogs.
- On Linux and other systems, it uses the `yad` command, the `zenity` command, or defaults to Tkinter if neither are available.

## Notes

`yad`, `zenity`, and AppleScript provide easy access to password/input prompts, color pickers, and a few more useful things from the command line, while Windows makes it more difficult to access these (it requires using ctypes to mimic C++ code). It could be possible to rebind tk's dialogs on Windows into python, but for now these functions will not be implemented.

## Usage

```python
import xdialog

# For opening files (returns either Iterable[str], or str, which is empty on failure)
# MacOS doesn't support filetypes fully and just disables picking any filetypes not listed
xdialog.open_file("Title Here", filetypes=[("Text Files", "*.txt")], multiple=True)
# For saving files (returns str, which is empty on failure)
# MacOS doesn't support filetypes fully and uses the first type as the default filename instead
xdialog.save_file("Title Here", filetypes=[("Text File", "*.txt")])
# For selecting a directory (returns str, which is empty on failure)
xdialog.directory("Title Here")

# Shows an info message box
xdialog.info("Title Here", "This is some info")
# Shows a warning message box
xdialog.warning("Title Here", "This is a warning")
# Shows an error message box
xdialog.error("Title Here", "This is an error")

# Other dialogs are also available:
# They can return xdialog.YES, xdialog.NO, xdialog.CANCEL, xdialog.RETRY, or xdialog.OK.
xdialog.yesno("Title Here", "Yes, or No?")
xdialog.yesnocancel("Title Here", "Do you want to read from this file?")
xdialog.retrycancel("Title Here", "Failure, do you want to retry?")
xdialog.okcancel("Title Here", "Someone did something bad on social media.")
```

## Contact

Contact me on [Discord](https://discord.gg/pBFqEcXvW5) and support me on [Ko-Fi](https://ko-fi.com/mathgeniuszach)!
