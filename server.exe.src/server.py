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
    os.system("start /B memcached\memcached.exe -m 10 -c 1024")

  if "n" not in argList:
    os.chdir("nginx")
    os.system("start /B nginx")


def stop_server():
  os.system("taskkill /f /IM nginx.exe")
  os.system("taskkill /f /IM php-cgi.exe")
  os.system("taskkill /f /IM mysqld.exe")
  os.system("taskkill /f /IM memcached.exe")


def restart_server():
  pass


if __name__ == "__main__":
  if "--help" in sys.argv[1:]:
    print """Portable NPM2 Server Help:

      Usage: server.py [serve|stop|restart] OPTIONS

      serve       Starts the server and daemons

      stop        Stops server and all daemons

      restart     Nothing (right now)

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