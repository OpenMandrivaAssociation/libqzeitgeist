%define oname qzeitgeist
%define major 0
%define libname %mklibname %oname %major
%define develname %mklibname %oname -d


Name:		libqzeitgeist
Group:		Development/C++
Summary:	Qt interface for Zeitgeist
Version:	0.7.0
Release:	1
URL:		http://gitorious.org/kde-zeitgeist/libqzeitgeist
License: 	GPLv2
#  git clone http://gitorious.org/kde-zeitgeist/libqzeitgeist
Source0:	http://gitorious.org/kde-zeitgeist/libqzeitgeist/%{name}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:  kde4-macros

%description
Qt Zeitgeist Library.


#-------------------------------------------------------------------------------
%package -n %libname
Group:          System/Libraries
Summary:	Qt Zeitgeist library

%description -n %libname
Library for Qt Zeitgeist.

%files -n %libname
%defattr(-,root,root)
%{_kde_libdir}/libqzeitgeist.so.%{major}*


#-------------------------------------------------------------------------------
%package -n %develname
Group:		Development/C++
Summary:	Qt Zeitgeist developement files
Requires:	%libname = %version-%release
Obsoletes:	%name-devel < %version-%release
Provides:	%name-devel = %version-%release

%description -n %develname
Development files for Qt Zeitgeist.

%files -n %develname
%defattr(-,root,root)
%_kde_datadir/qzeitgeist/cmake
%_kde_includedir/QtZeitgeist
%_kde_libdir/libqzeitgeist.so
%_kde_libdir/pkgconfig/QtZeitgeist.pc


#-------------------------------------------------------------------------------
%prep
%setup -qn %name

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

