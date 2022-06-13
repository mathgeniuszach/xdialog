# xdialog
A cross-platform python wrapper for native dialogs.

You can install xdialog through pip...

```
pip install xdialog
```

Or you can copy and paste the xdialog folder into the root of your project if pip isn't available.

Here's how xdialog determines what dialogs to use:

- On Windows, xdialog uses the built-in ctypes module to interface directly with system dialogs.
- On Linux, it uses the `zenity` command, or defaults to Tkinter if `zenity` is not available.
- On other systems like MacOS, it defaults to Tkinter. If someone can implement native dialogs on MacOS, that would be appreciated :)

## Usage

```python
import xdialog

# For opening files (returns either Iterable[str], or str, which is empty on failure)
xdialog.open_file("Title Here", filters=[("Text Files", "*.txt")], multiple=True)
# For saving files (returns str, which is empty on failure)
xdialog.save_file("Title Here", filters=[("Text File", "*.txt")])
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



