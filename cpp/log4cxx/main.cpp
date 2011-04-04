#include <iostream>
#include <log4cxx/logger.h>
#include <log4cxx/xml/domconfigurator.h>

using namespace std;
using namespace log4cxx;
using namespace log4cxx::xml;
using namespace log4cxx::helpers;

// Define static logger variable

LoggerPtr loggerMyMain(Logger::getLogger( "main"));

LoggerPtr loggerFunctionA(Logger::getLogger( "functionA"));
void functionA()       
{ 
    LOG4CXX_INFO(loggerFunctionA, "Executing functionA.");
}

int main()       
{
    // Load configuration file

    DOMConfigurator::configure("Log4cxxConfig.xml");
    LOG4CXX_TRACE(loggerMyMain, "this is a debug message for detailed code discovery.");
    LOG4CXX_DEBUG(loggerMyMain, "this is a debug message.");
    LOG4CXX_INFO (loggerMyMain, "this is a info message, ignore.");
    LOG4CXX_WARN (loggerMyMain, "this is a warn message, not too bad.");
    LOG4CXX_ERROR(loggerMyMain, "this is a error message, something serious is happening.");
    LOG4CXX_FATAL(loggerMyMain, "this is a fatal message!!!");
    functionA();

    if (loggerMyMain->isInfoEnabled())
        std::cout << "hurra info enabled" << std::endl;


    return 0;
}
