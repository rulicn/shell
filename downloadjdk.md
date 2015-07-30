Oracle has recently disallowed direct downloads of java from their servers (without going through the browser and agreeing to their terms, which you can look at here: http://www.oracle.com/technetwork/java/javase/terms/license/index.html). So, if you try:
```bash
wget "http://download.oracle.com/otn-pub/java/jdk/7u4-b20/jdk-7u4-linux-x64.tar.gz"
```
you will receive a page with "In order to download products from Oracle Technology Network you must agree to the OTN license terms" error message.

This can be rather troublesome for setting up servers with automated scripts.

Luckily, it seems that a single cookie is all that is needed to bypass this (you still have to agree to the terms to install):
```bash
Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie
```
So, if you want to download jdk7u4 for 64-bit Linux (e.g., Ubuntu) using wget, you can use:
```bash
wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-linux-x64.tar.gz"
```
Just for reference, here are the links to the current (at the time of posting) downloads of JDK and JRE
*UPDATE*: instead of having new post for each JDK/JRE update I'll just keep updating this one

*UPDATE 2*: Seems that you now need the --no-check-certificate flag for wget or you'll get a "cannot verify edelivery.oracle.com's certificate" error.

*UPDATE 3*: Starting with 7u51 they changed the cookie name, it's now "oraclelicense", thank you Yngve for posting in the comments - I updated the commands to include both cookies.

###JDK 8u25

+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-linux-i586.rpm
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-linux-i586.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-linux-x64.rpm
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-linux-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-macosx-x64.dmg
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-solaris-sparcv9.tar.Z
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-solaris-sparcv9.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-solaris-x64.tar.Z
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-solaris-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b18/jdk-8u25-windows-i586.exe
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b18/jdk-8u25-windows-x64.exe

###JDK 7u72

+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-linux-i586.rpm
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-linux-i586.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-linux-x64.rpm
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-linux-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-macosx-x64.dmg
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-solaris-i586.tar.Z
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-solaris-i586.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-solaris-x64.tar.Z
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-solaris-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-solaris-sparc.tar.Z
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-solaris-sparc.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-solaris-sparcv9.tar.Z
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-solaris-sparcv9.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-windows-i586.exe
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-windows-x64.exe

###JRE 8u25

+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jre-8u25-linux-i586.rpm
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jre-8u25-linux-i586.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jre-8u25-linux-x64.rpm
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jre-8u25-linux-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jre-8u25-macosx-x64.dmg
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jre-8u25-macosx-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jre-8u25-solaris-sparcv9.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jre-8u25-solaris-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b18/jre-8u25-windows-i586-iftw.exe
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b18/jre-8u25-windows-i586.exe
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b18/jre-8u25-windows-i586.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b18/jre-8u25-windows-x64.exe
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b18/jre-8u25-windows-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/server-jre-8u25-linux-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/server-jre-8u25-solaris-sparcv9.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b17/server-jre-8u25-solaris-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/8u25-b18/server-jre-8u25-windows-x64.tar.gz

###JRE 7u72

+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-linux-i586.rpm
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-linux-i586.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-linux-x64.rpm
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-linux-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-macosx-x64.dmg
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-macosx-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-solaris-i586.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-solaris-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-solaris-sparc.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-solaris-sparcv9.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-windows-i586-iftw.exe
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-windows-i586.exe
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-windows-i586.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-windows-x64.exe
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-windows-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/server-jre-7u72-linux-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/server-jre-7u72-solaris-i586.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/server-jre-7u72-solaris-sparc.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/server-jre-7u72-solaris-sparcv9.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/server-jre-7u72-solaris-x64.tar.gz
+ http://download.oracle.com/otn-pub/java/jdk/7u72-b14/server-jre-7u72-windows-x64.tar.gz
