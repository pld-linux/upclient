# TODO:
# - initscript
%define		_rc	b8
Summary:	Send the uptime of the machine it's running on to a server
Summary(pl):	Wysy³anie czas dzia³ania maszyny na serwer
Name:		upclient
Version:	5.0
Release:	0.%{_rc}.0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/upclient/%{name}-%{version}%{_rc}.tar.gz
URL:		http://upclient.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Upclient is a small program that sends the uptime of the machine it's
running on to a server (ufo.its.kun.nl). This server collects all
uptimes and puts them in a table. To view the table, visit
http://ufo.its.kun.nl/uptime/ . Upclient causes almost no traffic
(72bytes/minute), and won't give away any other information than the
uptime, load and the operating system it's running on. But to make
sure the program can't do any harm, don't run it as root. All it
needs, is access to /proc/uptime (and /proc/loadavg). Upclient is
totally freeware, so spread it around and make the list grow :)

%description -l pl
Upclient to ma³y program wysy³aj±cy uptime (czas dzia³ania) maszyny na
której dzia³a na serwer (ufo.its.kun.nl). Serwer ten zbiera wszystkie
czasy dzia³ania i umieszcza w tabeli. Tabelê mo¿na obejrzeæ pod
adresem http://ufo.its.kun.nl/uptime/ . Upclient prawie nie powoduje
ruchu (72 bajty na minutê) i nie wysy³a ¿adnych innych informacji ni¿
czas dzia³ania maszyny, obci±¿enie i system operacyjny na którym
dzia³a. Jednak aby mieæ pewno¶æ, ¿e program nie zrobi nic z³ego, nie
nale¿y go uruchamiaæ jako root. Wszystko, czego potrzebuje, to dostêp
do /proc/uptime (i /proc/loadavg). Upclient jest ca³kowicie darmowy,
wiêc mo¿na go rozprowadzaæ i doprowadzaæ do powiêkszania listy.

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
