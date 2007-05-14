Summary:	A GLib library to ease writing telepathy clients
Summary(pl.UTF-8):	Biblioteka oparta na GLib dla aplikacji służących do komunikacji
Name:		telepathy-glib
Version:	0.5.11
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-glib/%{name}-%{version}.tar.gz
# Source0-md5:	5ddba9c6f1620ed27a05e651bebb1800
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	glib2-devel >= 2.4.0
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	libtool
BuildRequires:	libtelepathy-devel
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
telepathy-glib is a D-Bus framework for unifying real time
communication, including instant messaging, voice calls and video
calls. It abstracts differences between protocols to provide a unified
interface for applications.

%description -l pl.UTF-8
telepathy-glib jest szkieletem opartym na D-Bus ujednolicającym
komunikację w czasie rzeczywistym, włączając w to komunikatory
oraz komunikację głosową i za pośrednictwem wideo. Zasłania
warstwą abstrakcji różnice pomiędzy protokołami dostarczając
jednolity interfejs dla aplikacji.

%package devel
Summary:	Header files for telepathy-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki telepathy-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.61
Requires:	glib2-devel >= 2.4.0

%description devel
Header files for telepathy-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki telepathy-glib.

%package static
Summary:	Static telepathy-glib library
Summary(pl.UTF-8):	Statyczna biblioteka telepathy-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static telepathy-glib library.

%description static -l pl.UTF-8
Statyczna biblioteka telepathy-glib.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libtelepathy-glib.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy-glib.so
%dir %{_includedir}/telepathy-1.0
%dir %{_includedir}/telepathy-1.0/telepathy-glib
%{_includedir}/telepathy-1.0/telepathy-glib/*.h
%{_libdir}/libtelepathy-glib.la
%{_pkgconfigdir}/telepathy-glib.pc
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libtelepathy-glib.a
