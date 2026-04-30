Name:           hello-rpm
Version:        2.0
Release:        2%{?dist}
Summary:        An upgraded Hello World script with config, docs, and scriptlets

License:        MIT
URL:            https://example.com

Source0:        hello.sh
Source1:        hello.conf
Source2:        hello.1
BuildArch:      noarch

%description
This is the upgraded version of our RPM package. It now includes
a configuration file in /etc, a man page, and a post-installation script.

%prep
# Nothing to prepare here

%build
# Nothing to compile

%install
# Create directories inside the buildroot
install -d -m 755 %{buildroot}/usr/local/bin
install -d -m 755 %{buildroot}/etc
install -d -m 755 %{buildroot}/usr/share/man/man1

# Copy files into place
install -m 755 %{SOURCE0} %{buildroot}/usr/local/bin/hello
install -m 644 %{SOURCE1} %{buildroot}/etc/hello.conf
install -m 644 %{SOURCE2} %{buildroot}/usr/share/man/man1/hello.1

%files
# The %config directive ensures changes to the config file are saved during updates
%config(noreplace) /etc/hello.conf
/usr/local/bin/hello
# Use wildcards to capture compressed man pages created automatically by the build
/usr/share/man/man1/*

%post
echo "--------------------------------------------------------"
echo "Thanks for installing hello-rpm-2.0!"
echo "You can read the manual using: man hello"
echo "--------------------------------------------------------"

%preun
if [ $1 -eq 0 ]; then
    echo "Removing hello-rpm-2.0..."
fi

%changelog
* Thu Apr 30 2026 Your Name <you@example.com> - 2.0-1
- Upgraded to version 2.0
- Added configuration file and manual page

* Fri May 01 2026 Your Name <you@example.com> - 2.0-2
- Updated author information in man page
