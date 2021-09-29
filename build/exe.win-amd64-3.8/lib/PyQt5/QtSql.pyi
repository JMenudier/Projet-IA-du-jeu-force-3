# The PEP 484 type hints stub file for the QtSql module.
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


class QSqlDriverCreatorBase(sip.wrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QSqlDriverCreatorBase') -> None: ...

    def createObject(self) -> 'QSqlDriver': ...


class QSqlDatabase(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QSqlDatabase') -> None: ...
    @typing.overload
    def __init__(self, type: str) -> None: ...
    @typing.overload
    def __init__(self, driver: 'QSqlDriver') -> None: ...

    def numericalPrecisionPolicy(self) -> 'QSql.NumericalPrecisionPolicy': ...
    def setNumericalPrecisionPolicy(self, precisionPolicy: 'QSql.NumericalPrecisionPolicy') -> None: ...
    @staticmethod
    def isDriverAvailable(name: str) -> bool: ...
    @staticmethod
    def registerSqlDriver(name: str, creator: QSqlDriverCreatorBase) -> None: ...
    @staticmethod
    def connectionNames() -> typing.List[str]: ...
    @staticmethod
    def drivers() -> typing.List[str]: ...
    @staticmethod
    def contains(connectionName: str = ...) -> bool: ...
    @staticmethod
    def removeDatabase(connectionName: str) -> None: ...
    @staticmethod
    def database(connectionName: str = ..., open: bool = ...) -> 'QSqlDatabase': ...
    @typing.overload
    @staticmethod
    def cloneDatabase(other: 'QSqlDatabase', connectionName: str) -> 'QSqlDatabase': ...
    @typing.overload
    @staticmethod
    def cloneDatabase(other: str, connectionName: str) -> 'QSqlDatabase': ...
    @typing.overload
    @staticmethod
    def addDatabase(type: str, connectionName: str = ...) -> 'QSqlDatabase': ...
    @typing.overload
    @staticmethod
    def addDatabase(driver: 'QSqlDriver', connectionName: str = ...) -> 'QSqlDatabase': ...
    def driver(self) -> 'QSqlDriver': ...
    def connectionName(self) -> str: ...
    def connectOptions(self) -> str: ...
    def port(self) -> int: ...
    def driverName(self) -> str: ...
    def hostName(self) -> str: ...
    def password(self) -> str: ...
    def userName(self) -> str: ...
    def databaseName(self) -> str: ...
    def setConnectOptions(self, options: str = ...) -> None: ...
    def setPort(self, p: int) -> None: ...
    def setHostName(self, host: str) -> None: ...
    def setPassword(self, password: str) -> None: ...
    def setUserName(self, name: str) -> None: ...
    def setDatabaseName(self, name: str) -> None: ...
    def rollback(self) -> bool: ...
    def commit(self) -> bool: ...
    def transaction(self) -> bool: ...
    def isValid(self) -> bool: ...
    def lastError(self) -> 'QSqlError': ...
    def exec(self, query: str = ...) -> 'QSqlQuery': ...
    def exec_(self, query: str = ...) -> 'QSqlQuery': ...
    def record(self, tablename: str) -> 'QSqlRecord': ...
    def primaryIndex(self, tablename: str) -> 'QSqlIndex': ...
    def tables(self, type: 'QSql.TableType' = ...) -> typing.List[str]: ...
    def isOpenError(self) -> bool: ...
    def isOpen(self) -> bool: ...
    def close(self) -> None: ...
    @typing.overload
    def open(self) -> bool: ...
    @typing.overload
    def open(self, user: str, password: str) -> bool: ...


class QSqlDriver(QtCore.QObject):

    class DbmsType(int): ...
    UnknownDbms = ... # type: 'QSqlDriver.DbmsType'
    MSSqlServer = ... # type: 'QSqlDriver.DbmsType'
    MySqlServer = ... # type: 'QSqlDriver.DbmsType'
    PostgreSQL = ... # type: 'QSqlDriver.DbmsType'
    Oracle = ... # type: 'QSqlDriver.DbmsType'
    Sybase = ... # type: 'QSqlDriver.DbmsType'
    SQLite = ... # type: 'QSqlDriver.DbmsType'
    Interbase = ... # type: 'QSqlDriver.DbmsType'
    DB2 = ... # type: 'QSqlDriver.DbmsType'

    class NotificationSource(int): ...
    UnknownSource = ... # type: 'QSqlDriver.NotificationSource'
    SelfSource = ... # type: 'QSqlDriver.NotificationSource'
    OtherSource = ... # type: 'QSqlDriver.NotificationSource'

    class IdentifierType(int): ...
    FieldName = ... # type: 'QSqlDriver.IdentifierType'
    TableName = ... # type: 'QSqlDriver.IdentifierType'

    class StatementType(int): ...
    WhereStatement = ... # type: 'QSqlDriver.StatementType'
    SelectStatement = ... # type: 'QSqlDriver.StatementType'
    UpdateStatement = ... # type: 'QSqlDriver.StatementType'
    InsertStatement = ... # type: 'QSqlDriver.StatementType'
    DeleteStatement = ... # type: 'QSqlDriver.StatementType'

    class DriverFeature(int): ...
    Transactions = ... # type: 'QSqlDriver.DriverFeature'
    QuerySize = ... # type: 'QSqlDriver.DriverFeature'
    BLOB = ... # type: 'QSqlDriver.DriverFeature'
    Unicode = ... # type: 'QSqlDriver.DriverFeature'
    PreparedQueries = ... # type: 'QSqlDriver.DriverFeature'
    NamedPlaceholders = ... # type: 'QSqlDriver.DriverFeature'
    PositionalPlaceholders = ... # type: 'QSqlDriver.DriverFeature'
    LastInsertId = ... # type: 'QSqlDriver.DriverFeature'
    BatchOperations = ... # type: 'QSqlDriver.DriverFeature'
    SimpleLocking = ... # type: 'QSqlDriver.DriverFeature'
    LowPrecisionNumbers = ... # type: 'QSqlDriver.DriverFeature'
    EventNotifications = ... # type: 'QSqlDriver.DriverFeature'
    FinishQuery = ... # type: 'QSqlDriver.DriverFeature'
    MultipleResultSets = ... # type: 'QSqlDriver.DriverFeature'

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def dbmsType(self) -> 'QSqlDriver.DbmsType': ...
    def numericalPrecisionPolicy(self) -> 'QSql.NumericalPrecisionPolicy': ...
    def setNumericalPrecisionPolicy(self, precisionPolicy: 'QSql.NumericalPrecisionPolicy') -> None: ...
    def stripDelimiters(self, identifier: str, type: 'QSqlDriver.IdentifierType') -> str: ...
    def isIdentifierEscaped(self, identifier: str, type: 'QSqlDriver.IdentifierType') -> bool: ...
    @typing.overload
    def notification(self, name: str) -> None: ...
    @typing.overload
    def notification(self, name: str, source: 'QSqlDriver.NotificationSource', payload: typing.Any) -> None: ...
    def subscribedToNotifications(self) -> typing.List[str]: ...
    def unsubscribeFromNotification(self, name: str) -> bool: ...
    def subscribeToNotification(self, name: str) -> bool: ...
    def setLastError(self, e: 'QSqlError') -> None: ...
    def setOpenError(self, e: bool) -> None: ...
    def setOpen(self, o: bool) -> None: ...
    def open(self, db: str, user: str = ..., password: str = ..., host: str = ..., port: int = ..., options: str = ...) -> bool: ...
    def createResult(self) -> 'QSqlResult': ...
    def close(self) -> None: ...
    def hasFeature(self, f: 'QSqlDriver.DriverFeature') -> bool: ...
    def handle(self) -> typing.Any: ...
    def lastError(self) -> 'QSqlError': ...
    def sqlStatement(self, type: 'QSqlDriver.StatementType', tableName: str, rec: 'QSqlRecord', preparedStatement: bool) -> str: ...
    def escapeIdentifier(self, identifier: str, type: 'QSqlDriver.IdentifierType') -> str: ...
    def formatValue(self, field: 'QSqlField', trimStrings: bool = ...) -> str: ...
    def record(self, tableName: str) -> 'QSqlRecord': ...
    def primaryIndex(self, tableName: str) -> 'QSqlIndex': ...
    def tables(self, tableType: 'QSql.TableType') -> typing.List[str]: ...
    def rollbackTransaction(self) -> bool: ...
    def commitTransaction(self) -> bool: ...
    def beginTransaction(self) -> bool: ...
    def isOpenError(self) -> bool: ...
    def isOpen(self) -> bool: ...


class QSqlError(sip.simplewrapper):

    class ErrorType(int): ...
    NoError = ... # type: 'QSqlError.ErrorType'
    ConnectionError = ... # type: 'QSqlError.ErrorType'
    StatementError = ... # type: 'QSqlError.ErrorType'
    TransactionError = ... # type: 'QSqlError.ErrorType'
    UnknownError = ... # type: 'QSqlError.ErrorType'

    @typing.overload
    def __init__(self, driverText: str = ..., databaseText: str = ..., type: 'QSqlError.ErrorType' = ..., errorCode: str = ...) -> None: ...
    @typing.overload
    def __init__(self, driverText: str, databaseText: str, type: 'QSqlError.ErrorType', number: int) -> None: ...
    @typing.overload
    def __init__(self, other: 'QSqlError') -> None: ...

    def swap(self, other: 'QSqlError') -> None: ...
    def nativeErrorCode(self) -> str: ...
    def isValid(self) -> bool: ...
    def text(self) -> str: ...
    def setNumber(self, number: int) -> None: ...
    def number(self) -> int: ...
    def setType(self, type: 'QSqlError.ErrorType') -> None: ...
    def type(self) -> 'QSqlError.ErrorType': ...
    def setDatabaseText(self, databaseText: str) -> None: ...
    def databaseText(self) -> str: ...
    def setDriverText(self, driverText: str) -> None: ...
    def driverText(self) -> str: ...


class QSqlField(sip.simplewrapper):

    class RequiredStatus(int): ...
    Unknown = ... # type: 'QSqlField.RequiredStatus'
    Optional = ... # type: 'QSqlField.RequiredStatus'
    Required = ... # type: 'QSqlField.RequiredStatus'

    @typing.overload
    def __init__(self, fieldName: str = ..., type: QtCore.QVariant.Type = ...) -> None: ...
    @typing.overload
    def __init__(self, fieldName: str, type: QtCore.QVariant.Type, tableName: str) -> None: ...
    @typing.overload
    def __init__(self, other: 'QSqlField') -> None: ...

    def tableName(self) -> str: ...
    def setTableName(self, tableName: str) -> None: ...
    def isValid(self) -> bool: ...
    def isGenerated(self) -> bool: ...
    def typeID(self) -> int: ...
    def defaultValue(self) -> typing.Any: ...
    def precision(self) -> int: ...
    def length(self) -> int: ...
    def requiredStatus(self) -> 'QSqlField.RequiredStatus': ...
    def setAutoValue(self, autoVal: bool) -> None: ...
    def setGenerated(self, gen: bool) -> None: ...
    def setSqlType(self, type: int) -> None: ...
    def setDefaultValue(self, value: typing.Any) -> None: ...
    def setPrecision(self, precision: int) -> None: ...
    def setLength(self, fieldLength: int) -> None: ...
    def setRequired(self, required: bool) -> None: ...
    def setRequiredStatus(self, status: 'QSqlField.RequiredStatus') -> None: ...
    def setType(self, type: QtCore.QVariant.Type) -> None: ...
    def isAutoValue(self) -> bool: ...
    def type(self) -> QtCore.QVariant.Type: ...
    def clear(self) -> None: ...
    def isReadOnly(self) -> bool: ...
    def setReadOnly(self, readOnly: bool) -> None: ...
    def isNull(self) -> bool: ...
    def name(self) -> str: ...
    def setName(self, name: str) -> None: ...
    def value(self) -> typing.Any: ...
    def setValue(self, value: typing.Any) -> None: ...


class QSqlRecord(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QSqlRecord') -> None: ...

    def keyValues(self, keyFields: 'QSqlRecord') -> 'QSqlRecord': ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...
    def clearValues(self) -> None: ...
    def clear(self) -> None: ...
    def contains(self, name: str) -> bool: ...
    def isEmpty(self) -> bool: ...
    def remove(self, pos: int) -> None: ...
    def insert(self, pos: int, field: QSqlField) -> None: ...
    def replace(self, pos: int, field: QSqlField) -> None: ...
    def append(self, field: QSqlField) -> None: ...
    @typing.overload
    def setGenerated(self, name: str, generated: bool) -> None: ...
    @typing.overload
    def setGenerated(self, i: int, generated: bool) -> None: ...
    @typing.overload
    def isGenerated(self, i: int) -> bool: ...
    @typing.overload
    def isGenerated(self, name: str) -> bool: ...
    @typing.overload
    def field(self, i: int) -> QSqlField: ...
    @typing.overload
    def field(self, name: str) -> QSqlField: ...
    def fieldName(self, i: int) -> str: ...
    def indexOf(self, name: str) -> int: ...
    @typing.overload
    def isNull(self, i: int) -> bool: ...
    @typing.overload
    def isNull(self, name: str) -> bool: ...
    @typing.overload
    def setNull(self, i: int) -> None: ...
    @typing.overload
    def setNull(self, name: str) -> None: ...
    @typing.overload
    def setValue(self, i: int, val: typing.Any) -> None: ...
    @typing.overload
    def setValue(self, name: str, val: typing.Any) -> None: ...
    @typing.overload
    def value(self, i: int) -> typing.Any: ...
    @typing.overload
    def value(self, name: str) -> typing.Any: ...


class QSqlIndex(QSqlRecord):

    @typing.overload
    def __init__(self, cursorName: str = ..., name: str = ...) -> None: ...
    @typing.overload
    def __init__(self, other: 'QSqlIndex') -> None: ...

    def setDescending(self, i: int, desc: bool) -> None: ...
    def isDescending(self, i: int) -> bool: ...
    @typing.overload
    def append(self, field: QSqlField) -> None: ...
    @typing.overload
    def append(self, field: QSqlField, desc: bool) -> None: ...
    def name(self) -> str: ...
    def setName(self, name: str) -> None: ...
    def cursorName(self) -> str: ...
    def setCursorName(self, cursorName: str) -> None: ...


class QSqlQuery(sip.simplewrapper):

    class BatchExecutionMode(int): ...
    ValuesAsRows = ... # type: 'QSqlQuery.BatchExecutionMode'
    ValuesAsColumns = ... # type: 'QSqlQuery.BatchExecutionMode'

    @typing.overload
    def __init__(self, r: 'QSqlResult') -> None: ...
    @typing.overload
    def __init__(self, query: str = ..., db: QSqlDatabase = ...) -> None: ...
    @typing.overload
    def __init__(self, db: QSqlDatabase) -> None: ...
    @typing.overload
    def __init__(self, other: 'QSqlQuery') -> None: ...

    def nextResult(self) -> bool: ...
    def finish(self) -> None: ...
    def numericalPrecisionPolicy(self) -> 'QSql.NumericalPrecisionPolicy': ...
    def setNumericalPrecisionPolicy(self, precisionPolicy: 'QSql.NumericalPrecisionPolicy') -> None: ...
    def lastInsertId(self) -> typing.Any: ...
    def executedQuery(self) -> str: ...
    def boundValues(self) -> typing.Dict[str, typing.Any]: ...
    @typing.overload
    def boundValue(self, placeholder: str) -> typing.Any: ...
    @typing.overload
    def boundValue(self, pos: int) -> typing.Any: ...
    def addBindValue(self, val: typing.Any, type: typing.Union['QSql.ParamType', 'QSql.ParamTypeFlag'] = ...) -> None: ...
    @typing.overload
    def bindValue(self, placeholder: str, val: typing.Any, type: typing.Union['QSql.ParamType', 'QSql.ParamTypeFlag'] = ...) -> None: ...
    @typing.overload
    def bindValue(self, pos: int, val: typing.Any, type: typing.Union['QSql.ParamType', 'QSql.ParamTypeFlag'] = ...) -> None: ...
    def prepare(self, query: str) -> bool: ...
    def execBatch(self, mode: 'QSqlQuery.BatchExecutionMode' = ...) -> bool: ...
    def clear(self) -> None: ...
    def last(self) -> bool: ...
    def first(self) -> bool: ...
    def previous(self) -> bool: ...
    def next(self) -> bool: ...
    def seek(self, index: int, relative: bool = ...) -> bool: ...
    @typing.overload
    def value(self, i: int) -> typing.Any: ...
    @typing.overload
    def value(self, name: str) -> typing.Any: ...
    @typing.overload
    def exec(self, query: str) -> bool: ...
    @typing.overload
    def exec(self) -> bool: ...
    @typing.overload
    def exec_(self, query: str) -> bool: ...
    @typing.overload
    def exec_(self) -> bool: ...
    def setForwardOnly(self, forward: bool) -> None: ...
    def record(self) -> QSqlRecord: ...
    def isForwardOnly(self) -> bool: ...
    def result(self) -> 'QSqlResult': ...
    def driver(self) -> QSqlDriver: ...
    def size(self) -> int: ...
    def isSelect(self) -> bool: ...
    def lastError(self) -> QSqlError: ...
    def numRowsAffected(self) -> int: ...
    def lastQuery(self) -> str: ...
    def at(self) -> int: ...
    @typing.overload
    def isNull(self, field: int) -> bool: ...
    @typing.overload
    def isNull(self, name: str) -> bool: ...
    def isActive(self) -> bool: ...
    def isValid(self) -> bool: ...


class QSqlQueryModel(QtCore.QAbstractTableModel):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def roleNames(self) -> typing.Dict[int, QtCore.QByteArray]: ...
    def endRemoveColumns(self) -> None: ...
    def beginRemoveColumns(self, parent: QtCore.QModelIndex, first: int, last: int) -> None: ...
    def endInsertColumns(self) -> None: ...
    def beginInsertColumns(self, parent: QtCore.QModelIndex, first: int, last: int) -> None: ...
    def endRemoveRows(self) -> None: ...
    def beginRemoveRows(self, parent: QtCore.QModelIndex, first: int, last: int) -> None: ...
    def endInsertRows(self) -> None: ...
    def beginInsertRows(self, parent: QtCore.QModelIndex, first: int, last: int) -> None: ...
    def endResetModel(self) -> None: ...
    def beginResetModel(self) -> None: ...
    def setLastError(self, error: QSqlError) -> None: ...
    def indexInQuery(self, item: QtCore.QModelIndex) -> QtCore.QModelIndex: ...
    def queryChange(self) -> None: ...
    def canFetchMore(self, parent: QtCore.QModelIndex = ...) -> bool: ...
    def fetchMore(self, parent: QtCore.QModelIndex = ...) -> None: ...
    def lastError(self) -> QSqlError: ...
    def clear(self) -> None: ...
    def query(self) -> QSqlQuery: ...
    @typing.overload
    def setQuery(self, query: QSqlQuery) -> None: ...
    @typing.overload
    def setQuery(self, query: str, db: QSqlDatabase = ...) -> None: ...
    def removeColumns(self, column: int, count: int, parent: QtCore.QModelIndex = ...) -> bool: ...
    def insertColumns(self, column: int, count: int, parent: QtCore.QModelIndex = ...) -> bool: ...
    def setHeaderData(self, section: int, orientation: QtCore.Qt.Orientation, value: typing.Any, role: int = ...) -> bool: ...
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...) -> typing.Any: ...
    def data(self, item: QtCore.QModelIndex, role: int = ...) -> typing.Any: ...
    @typing.overload
    def record(self, row: int) -> QSqlRecord: ...
    @typing.overload
    def record(self) -> QSqlRecord: ...
    def columnCount(self, parent: QtCore.QModelIndex = ...) -> int: ...
    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int: ...


class QSqlRelationalDelegate(QtWidgets.QItemDelegate):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def setEditorData(self, editor: QtWidgets.QWidget, index: QtCore.QModelIndex) -> None: ...
    def setModelData(self, editor: QtWidgets.QWidget, model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None: ...
    def createEditor(self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex) -> QtWidgets.QWidget: ...


class QSqlRelation(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, aTableName: str, indexCol: str, displayCol: str) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QSqlRelation') -> None: ...

    def swap(self, other: 'QSqlRelation') -> None: ...
    def isValid(self) -> bool: ...
    def displayColumn(self) -> str: ...
    def indexColumn(self) -> str: ...
    def tableName(self) -> str: ...


class QSqlTableModel(QSqlQueryModel):

    class EditStrategy(int): ...
    OnFieldChange = ... # type: 'QSqlTableModel.EditStrategy'
    OnRowChange = ... # type: 'QSqlTableModel.EditStrategy'
    OnManualSubmit = ... # type: 'QSqlTableModel.EditStrategy'

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ..., db: QSqlDatabase = ...) -> None: ...

    def primaryValues(self, row: int) -> QSqlRecord: ...
    @typing.overload
    def record(self) -> QSqlRecord: ...
    @typing.overload
    def record(self, row: int) -> QSqlRecord: ...
    def selectRow(self, row: int) -> bool: ...
    def indexInQuery(self, item: QtCore.QModelIndex) -> QtCore.QModelIndex: ...
    def setQuery(self, query: QSqlQuery) -> None: ...
    def setPrimaryKey(self, key: QSqlIndex) -> None: ...
    def selectStatement(self) -> str: ...
    def orderByClause(self) -> str: ...
    def deleteRowFromTable(self, row: int) -> bool: ...
    def insertRowIntoTable(self, values: QSqlRecord) -> bool: ...
    def updateRowInTable(self, row: int, values: QSqlRecord) -> bool: ...
    def beforeDelete(self, row: int) -> None: ...
    def beforeUpdate(self, row: int, record: QSqlRecord) -> None: ...
    def beforeInsert(self, record: QSqlRecord) -> None: ...
    def primeInsert(self, row: int, record: QSqlRecord) -> None: ...
    def revertAll(self) -> None: ...
    def submitAll(self) -> bool: ...
    def revert(self) -> None: ...
    def submit(self) -> bool: ...
    def revertRow(self, row: int) -> None: ...
    def setRecord(self, row: int, record: QSqlRecord) -> bool: ...
    def insertRecord(self, row: int, record: QSqlRecord) -> bool: ...
    def insertRows(self, row: int, count: int, parent: QtCore.QModelIndex = ...) -> bool: ...
    def removeRows(self, row: int, count: int, parent: QtCore.QModelIndex = ...) -> bool: ...
    def removeColumns(self, column: int, count: int, parent: QtCore.QModelIndex = ...) -> bool: ...
    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int: ...
    def setFilter(self, filter: str) -> None: ...
    def filter(self) -> str: ...
    def setSort(self, column: int, order: QtCore.Qt.SortOrder) -> None: ...
    def sort(self, column: int, order: QtCore.Qt.SortOrder) -> None: ...
    def fieldIndex(self, fieldName: str) -> int: ...
    def database(self) -> QSqlDatabase: ...
    def primaryKey(self) -> QSqlIndex: ...
    def editStrategy(self) -> 'QSqlTableModel.EditStrategy': ...
    def setEditStrategy(self, strategy: 'QSqlTableModel.EditStrategy') -> None: ...
    def clear(self) -> None: ...
    @typing.overload
    def isDirty(self, index: QtCore.QModelIndex) -> bool: ...
    @typing.overload
    def isDirty(self) -> bool: ...
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...) -> typing.Any: ...
    def setData(self, index: QtCore.QModelIndex, value: typing.Any, role: int = ...) -> bool: ...
    def data(self, idx: QtCore.QModelIndex, role: int = ...) -> typing.Any: ...
    def flags(self, index: QtCore.QModelIndex) -> QtCore.Qt.ItemFlags: ...
    def tableName(self) -> str: ...
    def setTable(self, tableName: str) -> None: ...
    def select(self) -> bool: ...


class QSqlRelationalTableModel(QSqlTableModel):

    class JoinMode(int): ...
    InnerJoin = ... # type: 'QSqlRelationalTableModel.JoinMode'
    LeftJoin = ... # type: 'QSqlRelationalTableModel.JoinMode'

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ..., db: QSqlDatabase = ...) -> None: ...

    def setJoinMode(self, joinMode: 'QSqlRelationalTableModel.JoinMode') -> None: ...
    def insertRowIntoTable(self, values: QSqlRecord) -> bool: ...
    def orderByClause(self) -> str: ...
    def updateRowInTable(self, row: int, values: QSqlRecord) -> bool: ...
    def selectStatement(self) -> str: ...
    def removeColumns(self, column: int, count: int, parent: QtCore.QModelIndex = ...) -> bool: ...
    def revertRow(self, row: int) -> None: ...
    def relationModel(self, column: int) -> QSqlTableModel: ...
    def relation(self, column: int) -> QSqlRelation: ...
    def setRelation(self, column: int, relation: QSqlRelation) -> None: ...
    def setTable(self, tableName: str) -> None: ...
    def select(self) -> bool: ...
    def clear(self) -> None: ...
    def setData(self, item: QtCore.QModelIndex, value: typing.Any, role: int = ...) -> bool: ...
    def data(self, item: QtCore.QModelIndex, role: int = ...) -> typing.Any: ...


class QSqlResult(sip.wrapper):

    class BindingSyntax(int): ...
    PositionalBinding = ... # type: 'QSqlResult.BindingSyntax'
    NamedBinding = ... # type: 'QSqlResult.BindingSyntax'

    def __init__(self, db: QSqlDriver) -> None: ...

    def lastInsertId(self) -> typing.Any: ...
    def record(self) -> QSqlRecord: ...
    def numRowsAffected(self) -> int: ...
    def size(self) -> int: ...
    def fetchLast(self) -> bool: ...
    def fetchFirst(self) -> bool: ...
    def fetchPrevious(self) -> bool: ...
    def fetchNext(self) -> bool: ...
    def fetch(self, i: int) -> bool: ...
    def reset(self, sqlquery: str) -> bool: ...
    def isNull(self, i: int) -> bool: ...
    def data(self, i: int) -> typing.Any: ...
    def bindingSyntax(self) -> 'QSqlResult.BindingSyntax': ...
    def hasOutValues(self) -> bool: ...
    def clear(self) -> None: ...
    def boundValueName(self, pos: int) -> str: ...
    def executedQuery(self) -> str: ...
    def boundValues(self) -> typing.List[typing.Any]: ...
    def boundValueCount(self) -> int: ...
    @typing.overload
    def bindValueType(self, placeholder: str) -> 'QSql.ParamType': ...
    @typing.overload
    def bindValueType(self, pos: int) -> 'QSql.ParamType': ...
    @typing.overload
    def boundValue(self, placeholder: str) -> typing.Any: ...
    @typing.overload
    def boundValue(self, pos: int) -> typing.Any: ...
    def addBindValue(self, val: typing.Any, type: typing.Union['QSql.ParamType', 'QSql.ParamTypeFlag']) -> None: ...
    @typing.overload
    def bindValue(self, pos: int, val: typing.Any, type: typing.Union['QSql.ParamType', 'QSql.ParamTypeFlag']) -> None: ...
    @typing.overload
    def bindValue(self, placeholder: str, val: typing.Any, type: typing.Union['QSql.ParamType', 'QSql.ParamTypeFlag']) -> None: ...
    def savePrepare(self, sqlquery: str) -> bool: ...
    def prepare(self, query: str) -> bool: ...
    def exec(self) -> bool: ...
    def exec_(self) -> bool: ...
    def setForwardOnly(self, forward: bool) -> None: ...
    def setSelect(self, s: bool) -> None: ...
    def setQuery(self, query: str) -> None: ...
    def setLastError(self, e: QSqlError) -> None: ...
    def setActive(self, a: bool) -> None: ...
    def setAt(self, at: int) -> None: ...
    def driver(self) -> QSqlDriver: ...
    def isForwardOnly(self) -> bool: ...
    def isSelect(self) -> bool: ...
    def isActive(self) -> bool: ...
    def isValid(self) -> bool: ...
    def lastError(self) -> QSqlError: ...
    def lastQuery(self) -> str: ...
    def at(self) -> int: ...
    def handle(self) -> typing.Any: ...


class QSql(sip.simplewrapper):

    class NumericalPrecisionPolicy(int): ...
    LowPrecisionInt32 = ... # type: 'QSql.NumericalPrecisionPolicy'
    LowPrecisionInt64 = ... # type: 'QSql.NumericalPrecisionPolicy'
    LowPrecisionDouble = ... # type: 'QSql.NumericalPrecisionPolicy'
    HighPrecision = ... # type: 'QSql.NumericalPrecisionPolicy'

    class TableType(int): ...
    Tables = ... # type: 'QSql.TableType'
    SystemTables = ... # type: 'QSql.TableType'
    Views = ... # type: 'QSql.TableType'
    AllTables = ... # type: 'QSql.TableType'

    class ParamTypeFlag(int): ...
    In = ... # type: 'QSql.ParamTypeFlag'
    Out = ... # type: 'QSql.ParamTypeFlag'
    InOut = ... # type: 'QSql.ParamTypeFlag'
    Binary = ... # type: 'QSql.ParamTypeFlag'

    class Location(int): ...
    BeforeFirstRow = ... # type: 'QSql.Location'
    AfterLastRow = ... # type: 'QSql.Location'

    class ParamType(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QSql.ParamType', 'QSql.ParamTypeFlag']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QSql.ParamType') -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QSql.ParamType': ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...
