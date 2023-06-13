# VS Code Training
As taken on LinkedIn Learning in June 2023: https://www.linkedin.com/learning/visual-studio-code-productivity-tips/access-the-sample-code-on-github?resume=false

Instructor: Walt Ritscher

GH with code: https://github.com/WaltRitscher/VsCodeTips

## Notes

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



### Finding what you need:

#### Go to + Peek Definition
- By right-clicking on an object or function in code, you can access `Go to Definition` and `Peek Definition`. This will show you the file where that object or function is defined. Very helpful!
- This also works for built-in objects or objects loaded from libraries.

![image](media/vscode_gotodefinition.png)


#### Find all references
- By selecting this option from the right-click menu, you can find all places where an object or function is referenced in **any open files.**