import os
import sys

def start_server():
  argList = ''.join(sys.argv[2:])
  # print argList

  if "p" not in argList:
    os.system("set PHP_FCGI_MAX_REQUESTS=1000")
    os.system("start /B php\\php-cgi.exe -b 127.0.0.1:9000 -c php\\php.ini")

  if "m" not in argList:
    os.system("start mysql\\bin\\mysqld")

  if "c" not in argList:
    os.system("start /B memcached\\memcached.exe -m 10 -c 1024")

  if "n" not in argList:
    os.system("start /B nginx\\nginx -p nginx")


def stop_server():
  os.system("nginx\\nginx.exe -p nginx -s quit")
  os.system("taskkill /f /IM php-cgi.exe")
  os.system("taskkill /f /IM mysqld.exe")
  os.system("taskkill /f /IM memcached.exe")


def restart_server():
  os.system("taskkill /f /IM mysqld.exe && start mysql\\bin\\mysqld")
  os.system("taskkill /f /IM php-cgi.exe && start /B php\\php-cgi.exe -b 127.0.0.1:9000 -c php\\php.ini")
  os.system("taskkill /f /IM memcached.exe && start /B memcached\\memcached.exe -m 10 -c 1024")
  os.system("nginx\\nginx.exe -p nginx -s quit && start /B nginx\\nginx -p nginx")


if __name__ == "__main__":
  if "--help" in sys.argv[1:]:
    print """Portable NPM2 Server Help:

      Usage: server.py [serve|stop|restart] OPTIONS

      serve       Starts the server and daemons

      stop        Stops server and all daemons

      restart     Restarts the server. Does not start daemons previously 
                  not run using arguments below.

      Arguments (OPTIONS):

      -p          Do not run PHP (ensure nginx.conf is configured properly)

      -m          Do not run MySQL

      -c          Do not run Memcache daemon

      -n          Do not start Nginx (but why?)

    """
  elif sys.argv[1] == "serve":
    start_server()
  elif sys.argv[1] == "stop":
    stop_server()
  elif sys.argv[1] == "restart":
    restart_server()
  else:
    print "Nothing Done. Did you try the correct command? [serve|stop|restart]"