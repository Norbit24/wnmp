# What is this?

Ever wanted a complete, fast, easy-to-use web server that you could put anywhere and run from anything? Welcome to WNMP - the portable Windows/Nginx/MySQL/PHP server. Just download the required packages (selecting which versions you want) and your ready to roll! No installation, no fuss.


# Install Guide:

-   [Install PHP](http://windows.php.net/download/)

    Download the "no-install" zip archive of the PHP version you wish to use and place it in the PHP directory. Make sure to create a "php.ini" file! Recommended: PHP Non-Thread-Safe version, use php-development.ini provided to get started.
-   [Install Memcached](http://blog.elijaa.org/index.php?post/2010/08/25/Memcached-1.4.5-for-Windows)

    Download the windows port of memcached and place it in the "memcached" folder. Version 1.4.5 is the latest memcached version for windows I've found.
-   [Install Nginx](http://nginx.org/)

    Download the Nginx webserver and place it in the "nginx" folder".
-   [Install MySQL](http://dev.mysql.com/downloads/mysql/)

    Download the "no-install" mysql server zip and place it in the "mysql" folder.
-   [OPTIONAL Install phpMyAdmin](http://www.phpmyadmin.net)
    
    phpMyAdmin makes managing MySQL databases easy. Download the phpMyAdmin files and place it in www/phpmyadmin/ (requires PHP to be installed!).

# Running the Server

After each package has been placed in the correct folder then run the serve.exe with the following options:

    Usage: server.exe [serve|stop|restart] OPTIONS

      serve       Starts the server and daemons

      stop        Stops server and all daemons

      restart     Nothing (right now)

      Arguments (OPTIONS):

      -p          Do not run PHP (ensure nginx.conf is configured properly)

      -m          Do not run MySQL

      -c          Do not run Memcache daemon

      -n          Do not start Nginx (but why?)

## Example

#### Start Server without Memcached and MySQL

    server.exe serve -mc

#### Start Server without PHP

    server.exe serve -p
    
#### Stop Server

    server.exe stop

---

# Notes

### Nginx

After downloading nginx you must make sure to enable PHP in the nginx.conf file and you must also make sure to set the correct root so that nginx knows where to find your web files. Please see the example.nginx.conf file included. We recommend that you use the included "www" folder as the web root (rather than the default of nginx/html/) since you might want to update nginx at a later date.

### PHP

Make sure to enabled your required PHP modules by editing the php.ini file. You might also need to set the "extension_dir" param to "ext" to make sure php looks in the right places for the DLL files!

### MySQL

Make sure to create a my.ini file in the mysql folder. It is important that you setup MySQL to handle UTF-8. Please see (or just use) the example.my.ini file for recommended values.

### Memcached

The start_server.bat file loads memcached using only 10MB of RAM by default. If you need more, start memcached separately:

    start /B memcached\memcached.exe -m 10 -c 1024
    server serve -c

Will work on a way to integrate the options for this in the server file, but right now it's not allowed.

---

David Pennington: <http://xeoncross.com> | <http://code2design.com>

Trae Blain: <http://traeblain.com/>