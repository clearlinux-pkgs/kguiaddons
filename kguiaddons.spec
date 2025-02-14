#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: e36a856
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kguiaddons
Version  : 6.11.0
Release  : 95
URL      : https://download.kde.org/stable/frameworks/6.11/kguiaddons-6.11.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.11/kguiaddons-6.11.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.11/kguiaddons-6.11.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kguiaddons-bin = %{version}-%{release}
Requires: kguiaddons-data = %{version}-%{release}
Requires: kguiaddons-lib = %{version}-%{release}
Requires: kguiaddons-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-dev
BuildRequires : libXScrnSaver-dev
BuildRequires : libXau-dev
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXdamage-dev
BuildRequires : libXdmcp-dev
BuildRequires : libXext-dev
BuildRequires : libXfixes-dev
BuildRequires : libXft-dev
BuildRequires : libXi-dev
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXv-dev
BuildRequires : libXxf86vm-dev
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(xcb)
BuildRequires : plasma-wayland-protocols-dev
BuildRequires : python3-dev
BuildRequires : qt6base-dev
BuildRequires : qt6wayland-dev
BuildRequires : xcb-util-cursor-dev
BuildRequires : xcb-util-dev
BuildRequires : xcb-util-image-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KDE GUI Addons
Utilities for graphical user interfaces
## Introduction
The &KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input.

%package bin
Summary: bin components for the kguiaddons package.
Group: Binaries
Requires: kguiaddons-data = %{version}-%{release}
Requires: kguiaddons-license = %{version}-%{release}

%description bin
bin components for the kguiaddons package.


%package data
Summary: data components for the kguiaddons package.
Group: Data

%description data
data components for the kguiaddons package.


%package dev
Summary: dev components for the kguiaddons package.
Group: Development
Requires: kguiaddons-lib = %{version}-%{release}
Requires: kguiaddons-bin = %{version}-%{release}
Requires: kguiaddons-data = %{version}-%{release}
Provides: kguiaddons-devel = %{version}-%{release}
Requires: kguiaddons = %{version}-%{release}

%description dev
dev components for the kguiaddons package.


%package lib
Summary: lib components for the kguiaddons package.
Group: Libraries
Requires: kguiaddons-data = %{version}-%{release}
Requires: kguiaddons-license = %{version}-%{release}

%description lib
lib components for the kguiaddons package.


%package license
Summary: license components for the kguiaddons package.
Group: Default

%description license
license components for the kguiaddons package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kguiaddons-6.11.0
cd %{_builddir}/kguiaddons-6.11.0
pushd ..
cp -a kguiaddons-6.11.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739559738
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
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1739559738
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kguiaddons
cp %{_builddir}/kguiaddons-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kguiaddons/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/kguiaddons-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kguiaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kguiaddons-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kguiaddons/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kguiaddons-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kguiaddons/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kguiaddons-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kguiaddons/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kguiaddons-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kguiaddons/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kguiaddons-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kguiaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kguiaddons-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kguiaddons/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kguiaddons-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kguiaddons/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kguiaddons-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kguiaddons/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kguiaddons-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kguiaddons/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kguiaddons-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kguiaddons/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kguiaddons-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kguiaddons/34f19e47876c7baa72ae7cc9acb28d8c2269b098 || :
cp %{_builddir}/kguiaddons-%{version}/src/geo-scheme-handler/google-maps-geo-handler.desktop.license %{buildroot}/usr/share/package-licenses/kguiaddons/8c23ed18e0340f8f0f545b9ccf5ed02e6c1125d2 || :
cp %{_builddir}/kguiaddons-%{version}/src/geo-scheme-handler/openstreetmap-geo-handler.desktop.license %{buildroot}/usr/share/package-licenses/kguiaddons/28ba3ebe1aa04fad742c69eb685e2a5376e9276f || :
cp %{_builddir}/kguiaddons-%{version}/src/geo-scheme-handler/qwant-maps-geo-handler.desktop.license %{buildroot}/usr/share/package-licenses/kguiaddons/8c23ed18e0340f8f0f545b9ccf5ed02e6c1125d2 || :
cp %{_builddir}/kguiaddons-%{version}/src/geo-scheme-handler/wheelmap-geo-handler.desktop.license %{buildroot}/usr/share/package-licenses/kguiaddons/28ba3ebe1aa04fad742c69eb685e2a5376e9276f || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kde-geo-uri-handler
/usr/bin/kde-geo-uri-handler

%files data
%defattr(-,root,root,-)
/usr/share/applications/google-maps-geo-handler.desktop
/usr/share/applications/openstreetmap-geo-handler.desktop
/usr/share/applications/wheelmap-geo-handler.desktop
/usr/share/qlogging-categories6/kguiaddons.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KGuiAddons/KColorCollection
/usr/include/KF6/KGuiAddons/KColorMimeData
/usr/include/KF6/KGuiAddons/KColorSchemeWatcher
/usr/include/KF6/KGuiAddons/KColorUtils
/usr/include/KF6/KGuiAddons/KCountryFlagEmojiIconEngine
/usr/include/KF6/KGuiAddons/KCursorSaver
/usr/include/KF6/KGuiAddons/KDateValidator
/usr/include/KF6/KGuiAddons/KFontUtils
/usr/include/KF6/KGuiAddons/KIconUtils
/usr/include/KF6/KGuiAddons/KImageCache
/usr/include/KF6/KGuiAddons/KJobWindows
/usr/include/KF6/KGuiAddons/KKeySequenceRecorder
/usr/include/KF6/KGuiAddons/KModifierKeyInfo
/usr/include/KF6/KGuiAddons/KSystemClipboard
/usr/include/KF6/KGuiAddons/KWindowInsetsController
/usr/include/KF6/KGuiAddons/KWordWrap
/usr/include/KF6/KGuiAddons/kcolorcollection.h
/usr/include/KF6/KGuiAddons/kcolormimedata.h
/usr/include/KF6/KGuiAddons/kcolorschemewatcher.h
/usr/include/KF6/KGuiAddons/kcolorutils.h
/usr/include/KF6/KGuiAddons/kcountryflagemojiiconengine.h
/usr/include/KF6/KGuiAddons/kcursorsaver.h
/usr/include/KF6/KGuiAddons/kdatevalidator.h
/usr/include/KF6/KGuiAddons/kfontutils.h
/usr/include/KF6/KGuiAddons/kguiaddons_export.h
/usr/include/KF6/KGuiAddons/kguiaddons_version.h
/usr/include/KF6/KGuiAddons/kiconutils.h
/usr/include/KF6/KGuiAddons/kimagecache.h
/usr/include/KF6/KGuiAddons/kjobwindows.h
/usr/include/KF6/KGuiAddons/kkeysequencerecorder.h
/usr/include/KF6/KGuiAddons/klocalimagecacheimpl.h
/usr/include/KF6/KGuiAddons/kmodifierkeyinfo.h
/usr/include/KF6/KGuiAddons/kmodifierkeyinfoprovider_p.h
/usr/include/KF6/KGuiAddons/ksystemclipboard.h
/usr/include/KF6/KGuiAddons/kwindowinsetscontroller.h
/usr/include/KF6/KGuiAddons/kwordwrap.h
/usr/lib64/cmake/KF6GuiAddons/KF6GuiAddonsConfig.cmake
/usr/lib64/cmake/KF6GuiAddons/KF6GuiAddonsConfigVersion.cmake
/usr/lib64/cmake/KF6GuiAddons/KF6GuiAddonsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6GuiAddons/KF6GuiAddonsTargets.cmake
/usr/lib64/libKF6GuiAddons.so
/usr/lib64/pkgconfig/KF6GuiAddons.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6GuiAddons.so.6.11.0
/V3/usr/lib64/qt6/qml/org/kde/guiaddons/libkguiaddonsqml.so
/usr/lib64/libKF6GuiAddons.so.6
/usr/lib64/libKF6GuiAddons.so.6.11.0
/usr/lib64/qt6/qml/org/kde/guiaddons/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/guiaddons/kguiaddonsqml.qmltypes
/usr/lib64/qt6/qml/org/kde/guiaddons/libkguiaddonsqml.so
/usr/lib64/qt6/qml/org/kde/guiaddons/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kguiaddons/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/kguiaddons/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kguiaddons/28ba3ebe1aa04fad742c69eb685e2a5376e9276f
/usr/share/package-licenses/kguiaddons/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kguiaddons/34f19e47876c7baa72ae7cc9acb28d8c2269b098
/usr/share/package-licenses/kguiaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kguiaddons/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kguiaddons/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kguiaddons/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kguiaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kguiaddons/8c23ed18e0340f8f0f545b9ccf5ed02e6c1125d2
/usr/share/package-licenses/kguiaddons/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kguiaddons/e712eadfab0d2357c0f50f599ef35ee0d87534cb
