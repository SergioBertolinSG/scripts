
This requires python3, pyqt5 and Qt creator to modify the interface.

Install steps required (OS X):

xcode-select --install
brew install python3
pip3 install -r requirements.txt


**Development**
To compile .ui files do

```
pyuic5 -o ui_oc_populator.py oc_populator.ui
```

**Use**

```
python3 oc_populator.py &
```



