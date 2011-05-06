#include <QCoreApplication>
#include "QCommandLine.h"

#include "test.h"

int main(int argc, char *argv[])
{
  QCoreApplication app(argc, argv);

#if 0
  QCoreApplication::setOrganizationDomain("titv.se");
  QCoreApplication::setOrganizationName("titv");
  QCoreApplication::setApplicationName("Test");
  QCoreApplication::setApplicationVersion("0.0.1");
#endif
  Test test;

  // return app.exec();
}
