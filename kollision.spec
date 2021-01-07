#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kollision
Version  : 20.12.1
Release  : 25
URL      : https://download.kde.org/stable/release-service/20.12.1/src/kollision-20.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.1/src/kollision-20.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.1/src/kollision-20.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kollision-bin = %{version}-%{release}
Requires: kollision-data = %{version}-%{release}
Requires: kollision-license = %{version}-%{release}
Requires: kollision-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the kollision package.
Group: Binaries
Requires: kollision-data = %{version}-%{release}
Requires: kollision-license = %{version}-%{release}

%description bin
bin components for the kollision package.


%package data
Summary: data components for the kollision package.
Group: Data

%description data
data components for the kollision package.


%package doc
Summary: doc components for the kollision package.
Group: Documentation

%description doc
doc components for the kollision package.


%package license
Summary: license components for the kollision package.
Group: Default

%description license
license components for the kollision package.


%package locales
Summary: locales components for the kollision package.
Group: Default

%description locales
locales components for the kollision package.


%prep
%setup -q -n kollision-20.12.1
cd %{_builddir}/kollision-20.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610042421
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1610042421
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kollision
cp %{_builddir}/kollision-20.12.1/COPYING %{buildroot}/usr/share/package-licenses/kollision/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kollision-20.12.1/COPYING.DOC %{buildroot}/usr/share/package-licenses/kollision/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang kollision

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kollision

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kollision.desktop
/usr/share/icons/hicolor/128x128/apps/kollision.png
/usr/share/icons/hicolor/16x16/apps/kollision.png
/usr/share/icons/hicolor/22x22/apps/kollision.png
/usr/share/icons/hicolor/32x32/apps/kollision.png
/usr/share/icons/hicolor/48x48/apps/kollision.png
/usr/share/icons/hicolor/64x64/apps/kollision.png
/usr/share/icons/oxygen/128x128/apps/kollision.png
/usr/share/icons/oxygen/16x16/apps/kollision.png
/usr/share/icons/oxygen/22x22/apps/kollision.png
/usr/share/icons/oxygen/32x32/apps/kollision.png
/usr/share/icons/oxygen/48x48/apps/kollision.png
/usr/share/icons/oxygen/64x64/apps/kollision.png
/usr/share/kollision/pictures/theme.svgz
/usr/share/kollision/sounds/ball_leaving.ogg
/usr/share/kollision/sounds/hit_wall.ogg
/usr/share/kollision/sounds/start.ogg
/usr/share/kollision/sounds/you_lose.ogg
/usr/share/metainfo/org.kde.kollision.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/cs/kollision/index.cache.bz2
/usr/share/doc/HTML/cs/kollision/index.docbook
/usr/share/doc/HTML/de/kollision/index.cache.bz2
/usr/share/doc/HTML/de/kollision/index.docbook
/usr/share/doc/HTML/en/kollision/gameboard.png
/usr/share/doc/HTML/en/kollision/index.cache.bz2
/usr/share/doc/HTML/en/kollision/index.docbook
/usr/share/doc/HTML/es/kollision/index.cache.bz2
/usr/share/doc/HTML/es/kollision/index.docbook
/usr/share/doc/HTML/et/kollision/index.cache.bz2
/usr/share/doc/HTML/et/kollision/index.docbook
/usr/share/doc/HTML/fr/kollision/index.cache.bz2
/usr/share/doc/HTML/fr/kollision/index.docbook
/usr/share/doc/HTML/id/kollision/index.cache.bz2
/usr/share/doc/HTML/id/kollision/index.docbook
/usr/share/doc/HTML/it/kollision/index.cache.bz2
/usr/share/doc/HTML/it/kollision/index.docbook
/usr/share/doc/HTML/ja/kollision/index.cache.bz2
/usr/share/doc/HTML/ja/kollision/index.docbook
/usr/share/doc/HTML/nl/kollision/index.cache.bz2
/usr/share/doc/HTML/nl/kollision/index.docbook
/usr/share/doc/HTML/nn/kollision/index.cache.bz2
/usr/share/doc/HTML/nn/kollision/index.docbook
/usr/share/doc/HTML/pl/kollision/index.cache.bz2
/usr/share/doc/HTML/pl/kollision/index.docbook
/usr/share/doc/HTML/pt/kollision/index.cache.bz2
/usr/share/doc/HTML/pt/kollision/index.docbook
/usr/share/doc/HTML/pt_BR/kollision/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kollision/index.docbook
/usr/share/doc/HTML/sv/kollision/index.cache.bz2
/usr/share/doc/HTML/sv/kollision/index.docbook
/usr/share/doc/HTML/uk/kollision/gameboard.png
/usr/share/doc/HTML/uk/kollision/index.cache.bz2
/usr/share/doc/HTML/uk/kollision/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kollision/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kollision/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kollision.lang
%defattr(-,root,root,-)

