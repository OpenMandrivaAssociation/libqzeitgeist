%define oname qzeitgeist
%define major 0
%define libname %mklibname %{oname} %{major}
%define develname %mklibname %{oname} -d


Name:		libqzeitgeist
Group:		Development/C++
Summary:	Qt interface for Zeitgeist
Version:	0.8.0
Release:	1
URL:		http://gitorious.org/kde-zeitgeist/libqzeitgeist
License: 	GPLv2
Source0:	http://gitorious.org/kde-zeitgeist/libqzeitgeist/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	zeitgeist

%description
Qt Zeitgeist Library.

#-------------------------------------------------------------------------------
%package -n %{libname}
Group:          System/Libraries
Summary:	Qt Zeitgeist library

%description -n %{libname}
Library for Qt Zeitgeist.

%files -n %{libname}
%{_libdir}/libqzeitgeist.so.%{major}*

#-------------------------------------------------------------------------------
%package -n %{develname}
Group:		Development/C++
Summary:	Qt Zeitgeist developement files
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{name}-devel < %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for Qt Zeitgeist.

%files -n %{develname}
%{_datadir}/qzeitgeist/cmake
%{_includedir}/QtZeitgeist
%{_libdir}/libqzeitgeist.so
%{_libdir}/pkgconfig/QtZeitgeist.pc

#-------------------------------------------------------------------------------
%prep
%setup -q

%build
%cmake_qt4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

