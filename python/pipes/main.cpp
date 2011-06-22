// Copyright (c) 2008, 2011 Thoreb ITvehicle AB

#include <cstring>
#include <fstream>
#include <iostream>
#include <signal.h>

#include <ecco/SerialPort.h>
#include <ecco/Thread.h>

static bool g_Running = true;
static XP_DWORD g_ByteCounter;

static ecco::SerialPort serial;

static void signalhandler(int signum)
{
    // Stop the application
    if (signum == SIGTERM || signum == SIGINT)
    {
        std::cerr << "terminating...\n";
        g_Running = false;
	serial.Close();
    }
}

static void signalhandler2(int signum)
{
    // Stop the application
    if (signum == SIGIO )
    {
      //        std::cerr << "Got SIGIO  ...\n";
    }
}

static void catch_alarm(int sig)
{

        std::cerr << "alarm...\n";
        alarm(1);

}

void OnData(const XP_BYTE*, unsigned int length)
{
    g_ByteCounter += length;
}


int main(int argc, char *argv[])
{
    int returnValue = 0;

    bool fixbug = false;
    if (argc > 1 && (strcmp(argv[1], "kick")==0))
        fixbug = true;

    try
    {
        signal(SIGINT, signalhandler);
        signal(SIGTERM, signalhandler);
	signal(SIGIO, SIG_IGN);
	signal(SIGIO, signalhandler2);
	signal(SIGALRM, catch_alarm);
	//        alarm(2);

        char junk = '0';


        XP_SIGC_CONNECTION connection = serial.SignalOnData.connect(XP_SIGC_PTRFUN(OnData));
	//        serial.Open("/dev/ttyPSC0", 19200,0,0, 0,true);
	//        serial.Open("/dev/ttyPSC9",4800);
        serial.Open("/dev/pts/4",38400);

        if (fixbug) // this will definitely disturb the ongoing ELSY traffic...
        {
            std::cerr << "kicking serial port...\n";
            serial.Write(&junk, 1);
        }

        while (g_Running)
        {
            ecco::Thread::Sleep(500);
            std::cerr << "Bytes received: " << g_ByteCounter << std::endl;
        }
        connection.disconnect();

    }
    catch (const ecco::Exception &e)
    {
        std::cerr << "Exception: " << e.GetMessage() << std::endl;
        returnValue = -1;
    }
    catch (...) // just in case
    {
        std::cerr << "Unknown exception!!!" << std::endl;
        returnValue = -4;
    }

    return returnValue;
}

