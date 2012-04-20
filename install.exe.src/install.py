from urllib import urlopen, urlretrieve
import zipfile
import sys
import os
import re

def unzip_install(prog_dir, prog_file_name, prog_base_dir):
  progzip = open(prog_file_name, 'rb')
  prog = zipfile.ZipFile(progzip)
  prog_install_path = prog_file_name[:-4]

  if prog_dir != prog_base_dir:
    prog.extractall()
    os.system("xcopy " + prog_install_path + " " + prog_dir + "/E /C /H /Q")
    os.system("rmdir /S /Q " + prog_install_path)
  else:
    prog.extractall(prog_dir)

  progzip.close()
  os.system("del " + prog_file_name)

def download_nginx():
  nginx_page = urlopen("http://nginx.org/en/download.html").read()
  nginx_base = "http://nginx.org"

  pg_st = nginx_page.find("Stable version")
  pg_end = nginx_page.find("Legacy versions")

  stbl_version = nginx_page[pg_st:pg_end]

  nginx_links = stbl_version.split("\"")
  for itm in nginx_links:
    if itm[-3:] == 'zip':
      nginx_link = nginx_base + itm

  nginx_file_name = nginx_link.split('/')[-1]
  urlretrieve(nginx_link, nginx_file_name)

  unzip_install("nginx", nginx_file_name, "")

def download_php():
  php_page = urlopen("http://windows.php.net/download/").read()
  php_base = 'http://windows.php.net'
  php_page_broken = php_page.split("\"")
  php_links = []
  for itm in php_page_broken:
    if itm[-3:] == 'zip':
      if itm[-7:] == 'src.zip':
        continue
      php_links.append(php_base + itm)

  php_file_name = php_links[0].split("/")[-1]
  urlretrieve(php_links[0], php_file_name)

  unzip_install("php", php_file_name, "php")

def download_mysql():
  mysql_loc = "http://mirror.services.wisc.edu/mysql/Downloads/MySQL-5.5/"
  mysql_page = urlopen(mysql_loc).read()
  mysql_page_files = re.findall(r'href="(.*?)"', mysql_page)
  mysql_links = []
  for itm in mysql_page_files:
    if itm[-9:] == 'win32.zip':
      mysql_links.append(mysql_loc + itm)

  mysql_file_name = mysql_links[-1].split("/")[-1]
  urlretrieve(mysql_links[-1], mysql_file_name)

  unzip_install("mysql", mysql_file_name, "")

def download_memcached():
  memcached_loc = "http://downloads.northscale.com/memcached-1.4.5-x86.zip"
  memcached_name = "memcached-x86.zip"
  urlretrieve(memcached_loc, memcached_name)

  unzip_install("memcached", memcached_name, "")

def usage():
  print """Portable WNMP Server Installer:

  Usage: install OPTIONS

  No OPTIONS installs all components for WNMP

  Arguments (OPTIONS):

  -p          Do not install PHP

  -m          Do not install MySQL

  -c          Do not install Memcached

  -n          Do not install Nginx (again why?)"""


if __name__ == "__main__":
  if not sys.argv[1:]:
    print "You ar installing everything... please be patient..."
    print "Fetching and loading Nginx..."
    download_nginx()
    print "Downloading PHP..."
    download_php()
    print "Downloading and installing MySQL... this may take a while..."
    download_mysql()
    print "Grabbing Memcached..."
    download_memcached()
    sys.exit()

  if "--help" in sys.argv[1:]:
    usage()
    sys.exit()

  argList = ''.join(sys.argv[1:])

  if "p" not in argList:
    print "Downloading PHP..."
    download_php()
  if "n" not in argList:
    print "Fetching and loading Nginx..."
    download_nginx()
  if "m" not in argList:
    print "Downloading and installing MySQL... this may take a while..."
    download_mysql()
  if "c" not in argList:
    print "Grabbing Memcached..."
    download_memcached()
  if "n" in argList:
    print """You didn't install Nginx, are you sure?

Please re-run this with '-pmc' to get Nginx installed."""