TEMPLATE = app
TARGET =

QMAKE_CXXFLAGS += `pkg-config ecco-xml-1.10 --cflags`
QMAKE_CXXFLAGS += `pkg-config smoke-0.2  --cflags`
QMAKE_CXXFLAGS += "-Wall"

QMAKE_LFLAGS += "`pkg-config ecco-xml-1.10 --libs`"
QMAKE_LFLAGS += "`pkg-config smoke-0.2 --libs`"

CONFIG += release

SOURCES += main.cpp 

