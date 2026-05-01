# hello-rpm

Welcome to the hello-rpm repository! This project contains an upgraded, GPG-signed hello command-line tool packaged for RPM-based Linux distributions (like Fedora, RHEL, and AlmaLinux).

Features in v2.0:

- Upgraded Executable: Simple, lightweight shell script installed in /usr/bin/hello.

- Configuration File: Includes a customizable configuration file in /etc/hello.conf (flagged as a config file so it won't be overwritten, i.e., noreplace).

- Manual Page: Added a man page (hello.1) to guide users.

- Scriptlets: Includes custom display messages during installation and removal of the package.

To ensure the integrity and authenticity of the packages, each release is digitally signed.

Verify the Package

1. Download and import the public key:

~~~
# If you are on the same machine, import from your build path, or download pubkey.asc
sudo rpmkeys --import pubkey.asc
~~~

2. Verify the RPM package:
~~~
rpm --checksig hello-rpm-2.0-2.el9.noarch.rpm
~~~
🛠️ Installation

If you have the file downloaded locally, use dnf:
~~~
sudo dnf install ./hello-rpm-2.0-2.el9.noarch.rpm
~~~

🌐 Future Plans
Network Repository Hosting
In the near future, this repository will be hosted on a network server. Users will be able to add the repository and install the package using standard dnf commands without needing to download the RPM file manually.

📝 Changelog

v2.0-2

- Updated author information in the man page.

- Fixed local installation directory structure.

- Fixed changelog ordering.

v2.0-1

- Upgraded package with configuration files (/etc/hello.conf) and man page support.
