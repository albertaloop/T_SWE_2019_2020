# AlbertaLoop GUI
**Note**: This is currently a work-in-progress

The pod UI is written in PyQt, which allows for easy hierarchical and modular organization. This is just a front-end representation of the interface, built using **Qt Creator**. The signals and actions need to be coded by hand moving forward, to allow the button presses to work, and further actions to take place.

## Screenshots and GIFS
### **Checkpoint 1**: Basic layout and tabs created
*Mode* tab:

![alt text](screenshots/mode.v1.png "Mode tab")

*Battery* tab:

![alt text](screenshots/battery.v1.png "Battery tab")

*Misc.* tab:

![alt text](screenshots/misc.v1.png "Misc. tab")

*Health Test* tab:

![alt text](screenshots/healthtest.v1.png "Health test tab")

*Navigation* tab:

![alt text](screenshots/nav.v1.png "Navigation tab")


## Build Process
The interface is created using **Qt Creator**, which produces a .ui file. To convert the .ui file into python code, use the following command in the terminal:
```
pyuic5 <.ui file> -o <python filename>
```
This will translate the .ui file into a .py file, and if you run the python program, it should produce the same design that was worked on within Qt Creator.

**Note**: The translation from the .ui to .py file only generates the class definitions. In order for the interface to "show" when you run the python program, the following needs to be added to the generated file:

Add the following imports (to the **top** of the file):
```
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
```

Add the following code to the **end** of the file:
```
app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())
```

## Information Yet to be added
As this is still a work in progress, information that is yet to be added to the interface is listed below:

* Quality logo/icons to use
* Font style to use
* Pod path visualization
* Simulation
* Health Test (functionality)
* Configuration sliders/input


## References
A list of useful references and documents that were useful while building the interface:

* [MIT Final Report](http://web.mit.edu/mopg/www/papers/MITHyperloop_FinalReport_2017_public.pdf)

