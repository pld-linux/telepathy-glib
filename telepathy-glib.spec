#
# Conditional build:
%bcond_without	apidocs	# gtk-doc documentation
%bcond_without	vala	# Vala API

Summary:	A GLib library to ease writing telepathy clients
Summary(pl.UTF-8):	Biblioteka oparta na GLib dla aplikacji służących do komunikacji
Name:		telepathy-glib
# NOTE: 0.24.x is stable, 0.25.x/0.99.x unstable
Version:	0.24.2
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://telepathy.freedesktop.org/releases/telepathy-glib/%{name}-%{version}.tar.gz
# Source0-md5:	a3a75657e9389381b44fee1680f770a7
URL:		https://telepathy.freedesktop.org/components/telepathy-glib/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-devel >= 0.95
BuildRequires:	dbus-glib-devel >= 0.90
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gobject-introspection-devel >= 1.30.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.17}
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-build >= 4.6
%{?with_vala:BuildRequires:	vala >= 2:0.16.0}
Requires:	dbus-glib >= 0.90
Requires:	dbus-libs >= 0.95
Requires:	glib2 >= 1:2.36.0
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
Requires:	dbus-devel >= 0.95
Requires:	dbus-glib-devel >= 0.90
Requires:	glib2-devel >= 1:2.36.0

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
BuildArch:	noarch

%description apidocs
telepathy-glib API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API telepathy-glib.

%package -n vala-telepathy-glib
Summary:	telepathy-glib API for Vala language
Summary(pl.UTF-8):	API telepathy-glib dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.16.0
BuildArch:	noarch

%description -n vala-telepathy-glib
telepathy-glib API for Vala language.

%description -n vala-telepathy-glib -l pl.UTF-8
API telepathy-glib dla języka Vala.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{__enable_disable apidocs gtk-doc} \
	--enable-introspection \
	%{__enable_disable vala vala-bindings} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtelepathy-glib.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libtelepathy-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-glib.so.0
%{_libdir}/girepository-1.0/TelepathyGLib-0.12.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy-glib.so
%dir %{_includedir}/telepathy-1.0
%dir %{_includedir}/telepathy-1.0/telepathy-glib
%dir %{_includedir}/telepathy-1.0/telepathy-glib/_gen
%{_includedir}/telepathy-1.0/telepathy-glib/*.h
%{_includedir}/telepathy-1.0/telepathy-glib/_gen/*.h
%{_pkgconfigdir}/telepathy-glib.pc
%{_datadir}/gir-1.0/TelepathyGLib-0.12.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libtelepathy-glib.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/telepathy-glib
%endif

%if %{with vala}
%files -n vala-telepathy-glib
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/telepathy-glib.deps
%{_datadir}/vala/vapi/telepathy-glib.vapi
%endif
