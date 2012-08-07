Summary:	Library to access to Google services
Name:		libkgapi
Version:	0.4.1
Release:	1
License:	GPL v2+
Group:		Development/Libraries
URL:		http://www.progdan.cz/2012/05/libkgoogle-libkgapi
Source0:	ftp://ftp.kde.org/pub/kde/stable/libkgapi/%{version}/src/%{name}-%{version}.tar.bz2
# Source-md5:	b4cefa643e95f5670997b5001547988f
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	kde4-kdepimlibs-devel

%description
Library to access to Google services, this package is needed by
kdepim-runtime to build akonadi-google resources.


%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdepimlibs-devel

%description devel
Libraries and header files for developing applications that use
akonadi-google resources.


%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README CHANGELOG LICENSE
%attr(755,root,root) %{_libdir}/libkgapi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkgapi.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/libkgapi
%{_pkgconfigdir}/libkgapi.pc
%attr(755,root,root) %{_libdir}/libkgapi.so
%{_libdir}/cmake/LibKGAPI
