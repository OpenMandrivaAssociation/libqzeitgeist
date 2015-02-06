# Ze: use this untill qt4 macros arent fixed
%define _qt4_datadir %{_prefix}/lib/qt4
%define _qt4_importdir %{_qt4_datadir}/imports

%define oname qzeitgeist
%define major 1
%define libname %mklibname %{oname} %{major}
%define develname %mklibname %{oname} -d


Name:		libqzeitgeist
Group:		Development/C++
Summary:	Qt interface for Zeitgeist
Version:	0.8.0
Release:	2
URL:		http://gitorious.org/kde-zeitgeist/libqzeitgeist
License: 	GPLv2
Source0:	http://gitorious.org/kde-zeitgeist/libqzeitgeist/%{name}-%{version}.tar.bz2
# import fedora patch
# fix linking (use QT_DECLARATIVE_LIBRARIES), consistently use QT_IMPORTS_DIR
Patch0:		libqzeitgeist-0.8.0-declarative.patch
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	pkgconfig(QtDBus) pkgconfig(QtDeclarative) pkgconfig(QtXml)
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
%{_libdir}/libqzeitgeist.so.1
%{_libdir}/libqzeitgeist.so.%{version}

#--------------------------------------------------------------------
%package -n libqzeitgeist-plugin
Group:		System/Libraries
Summary:	Qt Zeitgeist Plugin

%description -n libqzeitgeist-plugin
Qt Zeitgeist plugin.

%files -n libqzeitgeist-plugin
%{_qt4_importdir}/org/gnome/zeitgeist/libQZeitgeistDeclarativePlugin.so
%{_qt4_importdir}/org/gnome/zeitgeist/qmldir

#-------------------------------------------------------------------------------
%package -n %{develname}
Group:		Development/C++
Summary:	Qt Zeitgeist development files
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{name}-devel < %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for Qt Zeitgeist.

%files -n %{develname}
%{_includedir}/QZeitgeist
%{_libdir}/libqzeitgeist.so
%{_libdir}/cmake/QZeitgeist/QZeitgeist*.cmake
%{_libdir}/pkgconfig/QZeitgeist.pc

#-------------------------------------------------------------------------------
%prep
%setup -q
%patch0 -p1 -b .declarative

%build
%cmake -DQT_IMPORTS_DIR=%{_qt4_importdir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build



%changelog
* Wed Dec 21 2011 Zé <ze@mandriva.org> 0.8.0-1
+ Revision: 744052
- use this untill qt4 macros arent fixed
- fix devel file list
- forgot to list plugin files
- fix major and list files in lib package
- automoc4 is needed
- use pkg buildrequires
- declarative patch
- workaround for QT_IMPORTS_DIR (need to investigate why fails in FindQt4.cmake)
- clean defatr and BR
- kde macros are not to be used
- 0.8.0

* Thu Apr 28 2011 Zé <ze@mandriva.org> 0.7.0-1
+ Revision: 659767
- version 0.7.0
- drop patch0 (fixed upstream)
- fix package naming and add renaming
- fix URL

* Mon Mar 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-3
+ Revision: 648684
- Fix install
- Add missing buildrequire
- Install pkgconfig in %%_libdir ( P0 )
- Cosmetics
- Remove changelog, this does not belong to spec file

  + Jani Välimaa <wally@mandriva.org>
    - Created package structure for libzeitgeist.

  + Zé <ze@mandriva.org>
    - first package

