#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kollision
Version  : 23.08.4
Release  : 60
URL      : https://download.kde.org/stable/release-service/23.08.4/src/kollision-23.08.4.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.4/src/kollision-23.08.4.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.4/src/kollision-23.08.4.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kollision-bin = %{version}-%{release}
Requires: kollision-data = %{version}-%{release}
Requires: kollision-license = %{version}-%{release}
Requires: kollision-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kollision-23.08.4
cd %{_builddir}/kollision-23.08.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702952116
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702952116
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kollision
cp %{_builddir}/kollision-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kollision/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kollision-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kollision/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kollision-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kollision/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kollision-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kollision/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kollision-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kollision/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kollision
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kollision
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
/usr/share/doc/HTML/ca/kollision/gameboard.png
/usr/share/doc/HTML/ca/kollision/index.cache.bz2
/usr/share/doc/HTML/ca/kollision/index.docbook
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
/usr/share/package-licenses/kollision/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kollision/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kollision/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kollision/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kollision/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f kollision.lang
%defattr(-,root,root,-)

