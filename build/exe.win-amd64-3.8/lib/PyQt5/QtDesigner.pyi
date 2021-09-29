# The PEP 484 type hints stub file for the QtDesigner module.
#
# Generated by SIP 5.3.0
#
# Copyright (c) 2020 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt5 import QtWidgets
from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QDesignerActionEditorInterface(QtWidgets.QWidget):

    def __init__(self, parent: QtWidgets.QWidget, flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...

    def setFormWindow(self, formWindow: 'QDesignerFormWindowInterface') -> None: ...
    def unmanageAction(self, action: QtWidgets.QAction) -> None: ...
    def manageAction(self, action: QtWidgets.QAction) -> None: ...
    def core(self) -> 'QDesignerFormEditorInterface': ...


class QAbstractFormBuilder(sip.simplewrapper):

    def __init__(self) -> None: ...

    def errorString(self) -> str: ...
    def workingDirectory(self) -> QtCore.QDir: ...
    def setWorkingDirectory(self, directory: QtCore.QDir) -> None: ...
    def save(self, dev: QtCore.QIODevice, widget: QtWidgets.QWidget) -> None: ...
    def load(self, device: QtCore.QIODevice, parent: typing.Optional[QtWidgets.QWidget] = ...) -> QtWidgets.QWidget: ...


class QDesignerFormEditorInterface(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def setActionEditor(self, actionEditor: QDesignerActionEditorInterface) -> None: ...
    def setObjectInspector(self, objectInspector: 'QDesignerObjectInspectorInterface') -> None: ...
    def setPropertyEditor(self, propertyEditor: 'QDesignerPropertyEditorInterface') -> None: ...
    def setWidgetBox(self, widgetBox: 'QDesignerWidgetBoxInterface') -> None: ...
    def actionEditor(self) -> QDesignerActionEditorInterface: ...
    def formWindowManager(self) -> 'QDesignerFormWindowManagerInterface': ...
    def objectInspector(self) -> 'QDesignerObjectInspectorInterface': ...
    def propertyEditor(self) -> 'QDesignerPropertyEditorInterface': ...
    def widgetBox(self) -> 'QDesignerWidgetBoxInterface': ...
    def topLevel(self) -> QtWidgets.QWidget: ...
    def extensionManager(self) -> 'QExtensionManager': ...


class QDesignerFormWindowInterface(QtWidgets.QWidget):

    class FeatureFlag(int): ...
    EditFeature = ... # type: 'QDesignerFormWindowInterface.FeatureFlag'
    GridFeature = ... # type: 'QDesignerFormWindowInterface.FeatureFlag'
    TabOrderFeature = ... # type: 'QDesignerFormWindowInterface.FeatureFlag'
    DefaultFeature = ... # type: 'QDesignerFormWindowInterface.FeatureFlag'

    class Feature(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QDesignerFormWindowInterface.Feature', 'QDesignerFormWindowInterface.FeatureFlag']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QDesignerFormWindowInterface.Feature') -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QDesignerFormWindowInterface.Feature': ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...

    def activateResourceFilePaths(self, paths: typing.Iterable[str]) -> typing.Tuple[int, str]: ...
    def formContainer(self) -> QtWidgets.QWidget: ...
    def activeResourceFilePaths(self) -> typing.List[str]: ...
    def checkContents(self) -> typing.List[str]: ...
    def objectRemoved(self, o: QtCore.QObject) -> None: ...
    def widgetRemoved(self, w: QtWidgets.QWidget) -> None: ...
    def changed(self) -> None: ...
    def activated(self, widget: QtWidgets.QWidget) -> None: ...
    def aboutToUnmanageWidget(self, widget: QtWidgets.QWidget) -> None: ...
    def widgetUnmanaged(self, widget: QtWidgets.QWidget) -> None: ...
    def widgetManaged(self, widget: QtWidgets.QWidget) -> None: ...
    def resourceFilesChanged(self) -> None: ...
    def geometryChanged(self) -> None: ...
    def selectionChanged(self) -> None: ...
    def featureChanged(self, f: typing.Union['QDesignerFormWindowInterface.Feature', 'QDesignerFormWindowInterface.FeatureFlag']) -> None: ...
    def fileNameChanged(self, fileName: str) -> None: ...
    def mainContainerChanged(self, mainContainer: QtWidgets.QWidget) -> None: ...
    def setFileName(self, fileName: str) -> None: ...
    def setGrid(self, grid: QtCore.QPoint) -> None: ...
    def selectWidget(self, widget: QtWidgets.QWidget, select: bool = ...) -> None: ...
    def clearSelection(self, update: bool = ...) -> None: ...
    def setDirty(self, dirty: bool) -> None: ...
    def setFeatures(self, f: typing.Union['QDesignerFormWindowInterface.Feature', 'QDesignerFormWindowInterface.FeatureFlag']) -> None: ...
    def unmanageWidget(self, widget: QtWidgets.QWidget) -> None: ...
    def manageWidget(self, widget: QtWidgets.QWidget) -> None: ...
    def removeResourceFile(self, path: str) -> None: ...
    def addResourceFile(self, path: str) -> None: ...
    def resourceFiles(self) -> typing.List[str]: ...
    def emitSelectionChanged(self) -> None: ...
    @typing.overload
    @staticmethod
    def findFormWindow(w: QtWidgets.QWidget) -> 'QDesignerFormWindowInterface': ...
    @typing.overload
    @staticmethod
    def findFormWindow(obj: QtCore.QObject) -> 'QDesignerFormWindowInterface': ...
    def isDirty(self) -> bool: ...
    def isManaged(self, widget: QtWidgets.QWidget) -> bool: ...
    def setMainContainer(self, mainContainer: QtWidgets.QWidget) -> None: ...
    def mainContainer(self) -> QtWidgets.QWidget: ...
    def grid(self) -> QtCore.QPoint: ...
    def cursor(self) -> 'QDesignerFormWindowCursorInterface': ...
    def core(self) -> QDesignerFormEditorInterface: ...
    def setIncludeHints(self, includeHints: typing.Iterable[str]) -> None: ...
    def includeHints(self) -> typing.List[str]: ...
    def setExportMacro(self, exportMacro: str) -> None: ...
    def exportMacro(self) -> str: ...
    def setPixmapFunction(self, pixmapFunction: str) -> None: ...
    def pixmapFunction(self) -> str: ...
    def setLayoutFunction(self, margin: str, spacing: str) -> None: ...
    def layoutFunction(self) -> typing.Tuple[str, str]: ...
    def setLayoutDefault(self, margin: int, spacing: int) -> None: ...
    def layoutDefault(self) -> typing.Tuple[int, int]: ...
    def setComment(self, comment: str) -> None: ...
    def comment(self) -> str: ...
    def setAuthor(self, author: str) -> None: ...
    def author(self) -> str: ...
    def hasFeature(self, f: typing.Union['QDesignerFormWindowInterface.Feature', 'QDesignerFormWindowInterface.FeatureFlag']) -> bool: ...
    def features(self) -> 'QDesignerFormWindowInterface.Feature': ...
    @typing.overload
    def setContents(self, dev: QtCore.QIODevice, errorMessage: typing.Optional[str] = ...) -> bool: ...
    @typing.overload
    def setContents(self, contents: str) -> bool: ...
    def contents(self) -> str: ...
    def absoluteDir(self) -> QtCore.QDir: ...
    def fileName(self) -> str: ...


class QDesignerFormWindowCursorInterface(sip.simplewrapper):

    class MoveMode(int): ...
    MoveAnchor = ... # type: 'QDesignerFormWindowCursorInterface.MoveMode'
    KeepAnchor = ... # type: 'QDesignerFormWindowCursorInterface.MoveMode'

    class MoveOperation(int): ...
    NoMove = ... # type: 'QDesignerFormWindowCursorInterface.MoveOperation'
    Start = ... # type: 'QDesignerFormWindowCursorInterface.MoveOperation'
    End = ... # type: 'QDesignerFormWindowCursorInterface.MoveOperation'
    Next = ... # type: 'QDesignerFormWindowCursorInterface.MoveOperation'
    Prev = ... # type: 'QDesignerFormWindowCursorInterface.MoveOperation'
    Left = ... # type: 'QDesignerFormWindowCursorInterface.MoveOperation'
    Right = ... # type: 'QDesignerFormWindowCursorInterface.MoveOperation'
    Up = ... # type: 'QDesignerFormWindowCursorInterface.MoveOperation'
    Down = ... # type: 'QDesignerFormWindowCursorInterface.MoveOperation'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDesignerFormWindowCursorInterface') -> None: ...

    def isWidgetSelected(self, widget: QtWidgets.QWidget) -> bool: ...
    def resetWidgetProperty(self, widget: QtWidgets.QWidget, name: str) -> None: ...
    def setWidgetProperty(self, widget: QtWidgets.QWidget, name: str, value: typing.Any) -> None: ...
    def setProperty(self, name: str, value: typing.Any) -> None: ...
    def selectedWidget(self, index: int) -> QtWidgets.QWidget: ...
    def selectedWidgetCount(self) -> int: ...
    def hasSelection(self) -> bool: ...
    def widget(self, index: int) -> QtWidgets.QWidget: ...
    def widgetCount(self) -> int: ...
    def current(self) -> QtWidgets.QWidget: ...
    def setPosition(self, pos: int, mode: 'QDesignerFormWindowCursorInterface.MoveMode' = ...) -> None: ...
    def position(self) -> int: ...
    def movePosition(self, op: 'QDesignerFormWindowCursorInterface.MoveOperation', mode: 'QDesignerFormWindowCursorInterface.MoveMode' = ...) -> bool: ...
    def formWindow(self) -> QDesignerFormWindowInterface: ...


class QDesignerFormWindowManagerInterface(QtCore.QObject):

    class ActionGroup(int): ...
    StyledPreviewActionGroup = ... # type: 'QDesignerFormWindowManagerInterface.ActionGroup'

    class Action(int): ...
    CutAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    CopyAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    PasteAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    DeleteAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    SelectAllAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    LowerAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    RaiseAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    UndoAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    RedoAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    HorizontalLayoutAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    VerticalLayoutAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    SplitHorizontalAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    SplitVerticalAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    GridLayoutAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    FormLayoutAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    BreakLayoutAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    AdjustSizeAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    SimplifyLayoutAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    DefaultPreviewAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'
    FormWindowSettingsDialogAction = ... # type: 'QDesignerFormWindowManagerInterface.Action'

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def showPluginDialog(self) -> None: ...
    def closeAllPreviews(self) -> None: ...
    def showPreview(self) -> None: ...
    def actionGroup(self, actionGroup: 'QDesignerFormWindowManagerInterface.ActionGroup') -> QtWidgets.QActionGroup: ...
    def action(self, action: 'QDesignerFormWindowManagerInterface.Action') -> QtWidgets.QAction: ...
    def setActiveFormWindow(self, formWindow: QDesignerFormWindowInterface) -> None: ...
    def removeFormWindow(self, formWindow: QDesignerFormWindowInterface) -> None: ...
    def addFormWindow(self, formWindow: QDesignerFormWindowInterface) -> None: ...
    def formWindowSettingsChanged(self, fw: QDesignerFormWindowInterface) -> None: ...
    def activeFormWindowChanged(self, formWindow: QDesignerFormWindowInterface) -> None: ...
    def formWindowRemoved(self, formWindow: QDesignerFormWindowInterface) -> None: ...
    def formWindowAdded(self, formWindow: QDesignerFormWindowInterface) -> None: ...
    def core(self) -> QDesignerFormEditorInterface: ...
    def createFormWindow(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> QDesignerFormWindowInterface: ...
    def formWindow(self, index: int) -> QDesignerFormWindowInterface: ...
    def formWindowCount(self) -> int: ...
    def activeFormWindow(self) -> QDesignerFormWindowInterface: ...
    def actionSimplifyLayout(self) -> QtWidgets.QAction: ...
    def actionFormLayout(self) -> QtWidgets.QAction: ...


class QDesignerObjectInspectorInterface(QtWidgets.QWidget):

    def __init__(self, parent: QtWidgets.QWidget, flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...

    def setFormWindow(self, formWindow: QDesignerFormWindowInterface) -> None: ...
    def core(self) -> QDesignerFormEditorInterface: ...


class QDesignerPropertyEditorInterface(QtWidgets.QWidget):

    def __init__(self, parent: QtWidgets.QWidget, flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...

    def setReadOnly(self, readOnly: bool) -> None: ...
    def setPropertyValue(self, name: str, value: typing.Any, changed: bool = ...) -> None: ...
    def setObject(self, object: QtCore.QObject) -> None: ...
    def propertyChanged(self, name: str, value: typing.Any) -> None: ...
    def currentPropertyName(self) -> str: ...
    def object(self) -> QtCore.QObject: ...
    def isReadOnly(self) -> bool: ...
    def core(self) -> QDesignerFormEditorInterface: ...


class QDesignerWidgetBoxInterface(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...

    def save(self) -> bool: ...
    def load(self) -> bool: ...
    def fileName(self) -> str: ...
    def setFileName(self, file_name: str) -> None: ...


class QDesignerContainerExtension(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDesignerContainerExtension') -> None: ...

    def canRemove(self, index: int) -> bool: ...
    def canAddWidget(self) -> bool: ...
    def remove(self, index: int) -> None: ...
    def insertWidget(self, index: int, widget: QtWidgets.QWidget) -> None: ...
    def addWidget(self, widget: QtWidgets.QWidget) -> None: ...
    def setCurrentIndex(self, index: int) -> None: ...
    def currentIndex(self) -> int: ...
    def widget(self, index: int) -> QtWidgets.QWidget: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...


class QDesignerCustomWidgetInterface(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDesignerCustomWidgetInterface') -> None: ...

    def codeTemplate(self) -> str: ...
    def domXml(self) -> str: ...
    def initialize(self, core: QDesignerFormEditorInterface) -> None: ...
    def isInitialized(self) -> bool: ...
    def createWidget(self, parent: QtWidgets.QWidget) -> QtWidgets.QWidget: ...
    def isContainer(self) -> bool: ...
    def icon(self) -> QtGui.QIcon: ...
    def includeFile(self) -> str: ...
    def whatsThis(self) -> str: ...
    def toolTip(self) -> str: ...
    def group(self) -> str: ...
    def name(self) -> str: ...


class QDesignerCustomWidgetCollectionInterface(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDesignerCustomWidgetCollectionInterface') -> None: ...

    def customWidgets(self) -> typing.List[QDesignerCustomWidgetInterface]: ...


class QAbstractExtensionFactory(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QAbstractExtensionFactory') -> None: ...

    def extension(self, object: QtCore.QObject, iid: str) -> QtCore.QObject: ...


class QExtensionFactory(QtCore.QObject, QAbstractExtensionFactory):

    def __init__(self, parent: typing.Optional['QExtensionManager'] = ...) -> None: ...

    def createExtension(self, object: QtCore.QObject, iid: str, parent: QtCore.QObject) -> QtCore.QObject: ...
    def extensionManager(self) -> 'QExtensionManager': ...
    def extension(self, object: QtCore.QObject, iid: str) -> QtCore.QObject: ...


class QAbstractExtensionManager(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QAbstractExtensionManager') -> None: ...

    def extension(self, object: QtCore.QObject, iid: str) -> QtCore.QObject: ...
    def unregisterExtensions(self, factory: QAbstractExtensionFactory, iid: str) -> None: ...
    def registerExtensions(self, factory: QAbstractExtensionFactory, iid: str) -> None: ...


class QFormBuilder(QAbstractFormBuilder):

    def __init__(self) -> None: ...

    def customWidgets(self) -> typing.List[QDesignerCustomWidgetInterface]: ...
    def setPluginPath(self, pluginPaths: typing.Iterable[str]) -> None: ...
    def addPluginPath(self, pluginPath: str) -> None: ...
    def clearPluginPaths(self) -> None: ...
    def pluginPaths(self) -> typing.List[str]: ...


class QDesignerMemberSheetExtension(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDesignerMemberSheetExtension') -> None: ...

    def parameterNames(self, index: int) -> typing.List[QtCore.QByteArray]: ...
    def parameterTypes(self, index: int) -> typing.List[QtCore.QByteArray]: ...
    def signature(self, index: int) -> str: ...
    def declaredInClass(self, index: int) -> str: ...
    def inheritedFromWidget(self, index: int) -> bool: ...
    def isSlot(self, index: int) -> bool: ...
    def isSignal(self, index: int) -> bool: ...
    def setVisible(self, index: int, b: bool) -> None: ...
    def isVisible(self, index: int) -> bool: ...
    def setMemberGroup(self, index: int, group: str) -> None: ...
    def memberGroup(self, index: int) -> str: ...
    def memberName(self, index: int) -> str: ...
    def indexOf(self, name: str) -> int: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...


class QDesignerPropertySheetExtension(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDesignerPropertySheetExtension') -> None: ...

    def isEnabled(self, index: int) -> bool: ...
    def setChanged(self, index: int, changed: bool) -> None: ...
    def isChanged(self, index: int) -> bool: ...
    def setProperty(self, index: int, value: typing.Any) -> None: ...
    def property(self, index: int) -> typing.Any: ...
    def setAttribute(self, index: int, b: bool) -> None: ...
    def isAttribute(self, index: int) -> bool: ...
    def setVisible(self, index: int, b: bool) -> None: ...
    def isVisible(self, index: int) -> bool: ...
    def reset(self, index: int) -> bool: ...
    def hasReset(self, index: int) -> bool: ...
    def setPropertyGroup(self, index: int, group: str) -> None: ...
    def propertyGroup(self, index: int) -> str: ...
    def propertyName(self, index: int) -> str: ...
    def indexOf(self, name: str) -> int: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...


class QExtensionManager(QtCore.QObject, QAbstractExtensionManager):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def extension(self, object: QtCore.QObject, iid: str) -> QtCore.QObject: ...
    def unregisterExtensions(self, factory: QAbstractExtensionFactory, iid: str = ...) -> None: ...
    def registerExtensions(self, factory: QAbstractExtensionFactory, iid: str = ...) -> None: ...


class QDesignerTaskMenuExtension(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDesignerTaskMenuExtension') -> None: ...

    def preferredEditAction(self) -> QtWidgets.QAction: ...
    def taskActions(self) -> typing.List[QtWidgets.QAction]: ...


class QPyDesignerContainerExtension(QtCore.QObject, QDesignerContainerExtension):

    def __init__(self, parent: QtCore.QObject) -> None: ...


class QPyDesignerCustomWidgetCollectionPlugin(QtCore.QObject, QDesignerCustomWidgetCollectionInterface):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...


class QPyDesignerCustomWidgetPlugin(QtCore.QObject, QDesignerCustomWidgetInterface):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...


class QPyDesignerMemberSheetExtension(QtCore.QObject, QDesignerMemberSheetExtension):

    def __init__(self, parent: QtCore.QObject) -> None: ...


class QPyDesignerPropertySheetExtension(QtCore.QObject, QDesignerPropertySheetExtension):

    def __init__(self, parent: QtCore.QObject) -> None: ...


class QPyDesignerTaskMenuExtension(QtCore.QObject, QDesignerTaskMenuExtension):

    def __init__(self, parent: QtCore.QObject) -> None: ...
