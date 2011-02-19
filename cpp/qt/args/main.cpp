#include <QCoreApplication>
#include "QCommandLine.h"

#include "test.h"

int main(int argc, char *argv[])
{
  QCoreApplication app(argc, argv);

  QCoreApplication::setOrganizationDomain("titv.se");
  QCoreApplication::setOrganizationName("titv");
  QCoreApplication::setApplicationName("Test");
  QCoreApplication::setApplicationVersion("0.0.1");

  Test test;

  // return app.exec();
}
