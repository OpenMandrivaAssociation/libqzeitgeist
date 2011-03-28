
Name:		libqzeitgeist
Group:		Development/C++
Summary:	Qt interface for Zeitgeist
Version:	0.1
Release:	%mkrel 1
URL:		http://gitorious.org/kde-zeitgeist/libqzeitgeist
License: 	GPL
#  git clone http://gitorious.org/kde-zeitgeist/libqzeitgeist
Source0:	http://gitorious.org/kde-zeitgeist/libqzeitgeist/%{name}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	cmake
BuildRequires:	qt4-devel

%description
Qt Zeitgeist Library.

#-------------------------------------------------------------------------------
%package -n %name-devel
Group:		Development/C++
Summary:	Qt Zeitgeist developement files

%description -n %name-devel
Development files for Qt Zeitgeist.

%files -n %name-devel
%defattr(-,root,root)
%_kde_datadir/qzeitgeist/cmake
%_kde_includedir/QtZeitgeist
%_usr/lib/libqzeitgeist.so
%_usr/lib/pkgconfig/QtZeitgeist.pc

#-------------------------------------------------------------------------------

%prep
%setup -qn %name

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

