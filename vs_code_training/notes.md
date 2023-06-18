# VS Code Training
As taken on LinkedIn Learning in June 2023: https://www.linkedin.com/learning/visual-studio-code-productivity-tips/access-the-sample-code-on-github?resume=false

Instructor: Walt Ritscher

GH with code: https://github.com/WaltRitscher/VsCodeTips

## Notes

### Find VS Code Commands (on Linux)
- `CTRL + SHIFT + P` gets the command palette - where you can run VS code commands
  - Note: Not sure exactly what lives here vs. settings yet
- `CTRL + ,` gets the settings menu

---

### Other extensions
- GitLens extension lets you see line-for-line the last time code was changed - and in what commit!
  - You can use this to look at changes since last commit (without git diff in terminal), find out who changed lines last, and more
  - See tutorial here: https://www.youtube.com/watch?v=UQPb73Zz9qk
- Code Spell Checker checks the spelling of your strings and comments

---

### Navigation

- use `CTRL + TAB` on Linux to switch between VS Code tabs

### Editing en masse
**Rename Symbol**
- In the right-click menu, you can choose `Rename symbol` to edit all instances of a symbol in the code where it is referenced.
- Note that this is a semi-intelligent function and it won't change symbols that exist outside of the same scope.
- On Linux: `F2`

**Change All Occurrences**
- If you want to change all instances across a file, you can instead select `Change all occurrences` - which makes no check of scope - it just matches and changes all occurrences.
- On Linux: `CTRL + F2`

---

### Auto-generating code:
- With HTML + CSS, you can use **Emmet notation** to generate HTML very fast. For example, `div>ul>li*3` creates 3 <li> elements nested in a <ul> element nested in a <div> element. [read more on Emmet notation](https://docs.emmet.io/cheat-sheet/)
-

---

### Useful shortcuts:
NOTE: You can add or change existing shortcuts by using [`CTRL + K` `CTRL + S`] (on Linux)

- `CTRL + P` lets you search for and open a file by name (no more using file explorer)
- `ALT + arrow keys` lets you move the current line (or any highlighted lines up or down in the code)

---

### Saving files
- **Auto Save** setting lets you set whether VSCode will auto-save your files for you after a time delay or after switching focus.

---

### Cleaning up code
- You can use the `Format Document` option from the right-click menu to format your document according to a certain standard
- On Linux: `CTRL + SHIFT + I`

Note that you can also turn on formatting as you type by going to settings and changing the "**Editor: format on type** option.

---

### Autocomplete
- You can change some auto-complete features in VS Code to speed up your typing. Including:
  - "**Editor: Auto Closing Brackets**" I prefer to have set to "beforeWhitespace" because it is a pain if it's making closing brackets everywhere.
  -

---

### Finding what code you need:

#### Go to + Peek Definition
- By right-clicking on an object or function in code, you can access `Go to Definition` and `Peek Definition`. This will show you the file where that object or function is defined. Very helpful!
- This also works for built-in objects or objects loaded from libraries.

![image](media/vscode_gotodefinition.png)


#### Find all references
- By selecting this option from the right-click menu, you can find all places where an object or function is referenced in **any open files.**