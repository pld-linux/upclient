# TODO:
# - initscript
%define		_rc	b8
Summary:	Send the uptime of the machine it's running on to a server
Summary(pl.UTF-8):   Wysyłanie czasu działania maszyny na serwer
Name:		upclient
Version:	5.0
Release:	0.%{_rc}.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/upclient/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	5d2ac85193fdb898dd16a694b05ac4d0
URL:		http://upclient.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Upclient is a small program that sends the uptime of the machine it's
running on to a server (ufo.its.kun.nl). This server collects all
uptimes and puts them in a table. To view the table, visit
<http://ufo.its.kun.nl/uptime/>. Upclient causes almost no traffic
(72bytes/minute), and won't give away any other information than the
uptime, load and the operating system it's running on. But to make
sure the program can't do any harm, don't run it as root. All it
needs, is access to /proc/uptime (and /proc/loadavg). Upclient is
totally freeware, so spread it around and make the list grow :)

%description -l pl.UTF-8
Upclient to mały program wysyłający uptime (czas działania) maszyny na
której działa na serwer (ufo.its.kun.nl). Serwer ten zbiera wszystkie
czasy działania i umieszcza w tabeli. Tabelę można obejrzeć pod
adresem <http://ufo.its.kun.nl/uptime/>. Upclient prawie nie powoduje
ruchu (72 bajty na minutę) i nie wysyła żadnych innych informacji niż
czas działania maszyny, obciążenie i system operacyjny na którym
działa. Jednak aby mieć pewność, że program nie zrobi nic złego, nie
należy go uruchamiać jako root. Wszystko, czego potrzebuje, to dostęp
do /proc/uptime (i /proc/loadavg). Upclient jest całkowicie darmowy,
więc można go rozprowadzać i doprowadzać do powiększania listy.

%prep
%setup -q -n %{name}-%{version}%{_rc}

%build
%{__make} -C src linux \
	prefix=%{_prefix} \
	sysconfdir=%{_sysconfdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* AUTHORS FAQ HISTORY HISTORY-BETA INSTALL README TODO TODO-flawfinder
%attr(755,root,root) %{_sbindir}/%{name}
%verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man8/*
