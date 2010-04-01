#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	A GLib library to ease writing telepathy clients
Summary(pl.UTF-8):	Biblioteka oparta na GLib dla aplikacji służących do komunikacji
Name:		telepathy-glib
Version:	0.10.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-glib/%{name}-%{version}.tar.gz
# Source0-md5:	588e893f86f8b179d0b48d0946c08c9d
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.20.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.10}
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
telepathy-glib is a D-Bus framework for unifying real time
communication, including instant messaging, voice calls and video
calls. It abstracts differences between protocols to provide a unified
interface for applications.

%description -l pl.UTF-8
telepathy-glib jest szkieletem opartym na D-Bus ujednolicającym
komunikację w czasie rzeczywistym, włączając w to komunikatory oraz
komunikację głosową i za pośrednictwem wideo. Zasłania warstwą
abstrakcji różnice pomiędzy protokołami dostarczając jednolity
interfejs dla aplikacji.

%package devel
Summary:	Header files for telepathy-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki telepathy-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.74
Requires:	glib2-devel >= 1:2.16.0

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

%package apidocs
Summary:	telepathy-glib API documentation
Summary(pl.UTF-8):	Dokumentacja API telepathy-glib
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
telepathy-glib API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API telepathy-glib.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-silent-rules \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libtelepathy-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-glib.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy-glib.so
%{_libdir}/libtelepathy-glib.la
%dir %{_includedir}/telepathy-1.0
%dir %{_includedir}/telepathy-1.0/telepathy-glib
%dir %{_includedir}/telepathy-1.0/telepathy-glib/_gen
%{_includedir}/telepathy-1.0/telepathy-glib/*.h
%{_includedir}/telepathy-1.0/telepathy-glib/_gen/*.h
%{_pkgconfigdir}/telepathy-glib.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtelepathy-glib.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/telepathy-glib
%endif
