Summary:	Library to access to Google services
Name:		libkgapi
Version:	2.2.0
Release:	1
License:	GPL v2+
Group:		Development/Libraries
URL:		http://www.progdan.cz/2012/05/libkgoogle-libkgapi
Source0:	http://download.kde.org/stable/libkgapi/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	f3f2e4e68bb8baf849935f2f2eecf781
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
%doc README LICENSE
%attr(755,root,root) %{_libdir}/libkgapi2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkgapi2.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/LibKGAPI2
%{_includedir}/libkgapi2
%attr(755,root,root) %{_libdir}/libkgapi2.so
%{_libdir}/cmake/LibKGAPI2
