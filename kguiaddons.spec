#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kguiaddons
Version  : 5.66.0
Release  : 26
URL      : https://download.kde.org/stable/frameworks/5.66/kguiaddons-5.66.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.66/kguiaddons-5.66.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.66/kguiaddons-5.66.0.tar.xz.sig
Summary  : Addons to QtGui
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kguiaddons-lib = %{version}-%{release}
Requires: kguiaddons-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : qtbase-dev mesa-dev

%description
# KDE GUI Addons
Utilities for graphical user interfaces
## Introduction
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input.

%package dev
Summary: dev components for the kguiaddons package.
Group: Development
Requires: kguiaddons-lib = %{version}-%{release}
Provides: kguiaddons-devel = %{version}-%{release}
Requires: kguiaddons = %{version}-%{release}
Requires: kguiaddons = %{version}-%{release}

%description dev
dev components for the kguiaddons package.


%package lib
Summary: lib components for the kguiaddons package.
Group: Libraries
Requires: kguiaddons-license = %{version}-%{release}

%description lib
lib components for the kguiaddons package.


%package license
Summary: license components for the kguiaddons package.
Group: Default

%description license
license components for the kguiaddons package.


%prep
%setup -q -n kguiaddons-5.66.0
cd %{_builddir}/kguiaddons-5.66.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578934051
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1578934051
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kguiaddons
cp %{_builddir}/kguiaddons-5.66.0/COPYING %{buildroot}/usr/share/package-licenses/kguiaddons/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/kguiaddons-5.66.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/kguiaddons/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KGuiAddons/KColorCollection
/usr/include/KF5/KGuiAddons/KColorMimeData
/usr/include/KF5/KGuiAddons/KColorUtils
/usr/include/KF5/KGuiAddons/KDateValidator
/usr/include/KF5/KGuiAddons/KFontUtils
/usr/include/KF5/KGuiAddons/KIconUtils
/usr/include/KF5/KGuiAddons/KImageCache
/usr/include/KF5/KGuiAddons/KModifierKeyInfo
/usr/include/KF5/KGuiAddons/KWordWrap
/usr/include/KF5/KGuiAddons/kcolorcollection.h
/usr/include/KF5/KGuiAddons/kcolormimedata.h
/usr/include/KF5/KGuiAddons/kcolorutils.h
/usr/include/KF5/KGuiAddons/kdatevalidator.h
/usr/include/KF5/KGuiAddons/kfontutils.h
/usr/include/KF5/KGuiAddons/kguiaddons_export.h
/usr/include/KF5/KGuiAddons/kiconutils.h
/usr/include/KF5/KGuiAddons/kimagecache.h
/usr/include/KF5/KGuiAddons/klocalimagecacheimpl.h
/usr/include/KF5/KGuiAddons/kmodifierkeyinfo.h
/usr/include/KF5/KGuiAddons/kmodifierkeyinfoprovider_p.h
/usr/include/KF5/KGuiAddons/kwordwrap.h
/usr/include/KF5/kguiaddons_version.h
/usr/lib64/cmake/KF5GuiAddons/KF5GuiAddonsConfig.cmake
/usr/lib64/cmake/KF5GuiAddons/KF5GuiAddonsConfigVersion.cmake
/usr/lib64/cmake/KF5GuiAddons/KF5GuiAddonsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5GuiAddons/KF5GuiAddonsTargets.cmake
/usr/lib64/libKF5GuiAddons.so
/usr/lib64/qt5/mkspecs/modules/qt_KGuiAddons.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5GuiAddons.so.5
/usr/lib64/libKF5GuiAddons.so.5.66.0
/usr/lib64/qt5/plugins/kf5/kguiaddons/kmodifierkey/kmodifierkey_xcb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kguiaddons/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/kguiaddons/9a1929f4700d2407c70b507b3b2aaf6226a9543c
