#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kguiaddons
Version  : 5.91.0
Release  : 50
URL      : https://download.kde.org/stable/frameworks/5.91/kguiaddons-5.91.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.91/kguiaddons-5.91.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.91/kguiaddons-5.91.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kguiaddons-bin = %{version}-%{release}
Requires: kguiaddons-data = %{version}-%{release}
Requires: kguiaddons-lib = %{version}-%{release}
Requires: kguiaddons-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules qtwayland-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : qtx11extras-dev

%description


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
%setup -q -n kguiaddons-5.91.0
cd %{_builddir}/kguiaddons-5.91.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644799565
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1644799565
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kguiaddons
cp %{_builddir}/kguiaddons-5.91.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kguiaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/kguiaddons-5.91.0/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kguiaddons/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kguiaddons-5.91.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kguiaddons/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kguiaddons-5.91.0/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kguiaddons/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/kguiaddons-5.91.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kguiaddons/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kguiaddons-5.91.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kguiaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/kguiaddons-5.91.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kguiaddons/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kguiaddons-5.91.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kguiaddons/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kguiaddons-5.91.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kguiaddons/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kguiaddons-5.91.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kguiaddons/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kguiaddons-5.91.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kguiaddons/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kguiaddons-5.91.0/README.md.license %{buildroot}/usr/share/package-licenses/kguiaddons/34f19e47876c7baa72ae7cc9acb28d8c2269b098
cp %{_builddir}/kguiaddons-5.91.0/src/geo-scheme-handler/openstreetmap-geo-handler.desktop.license %{buildroot}/usr/share/package-licenses/kguiaddons/28ba3ebe1aa04fad742c69eb685e2a5376e9276f
cp %{_builddir}/kguiaddons-5.91.0/src/geo-scheme-handler/wheelmap-geo-handler.desktop.license %{buildroot}/usr/share/package-licenses/kguiaddons/28ba3ebe1aa04fad742c69eb685e2a5376e9276f
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kde-geo-uri-handler

%files data
%defattr(-,root,root,-)
/usr/share/applications/google-maps-geo-handler.desktop
/usr/share/applications/openstreetmap-geo-handler.desktop
/usr/share/applications/qwant-maps-geo-handler.desktop
/usr/share/applications/wheelmap-geo-handler.desktop
/usr/share/qlogging-categories5/kguiaddons.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KGuiAddons/KColorCollection
/usr/include/KF5/KGuiAddons/KColorMimeData
/usr/include/KF5/KGuiAddons/KColorUtils
/usr/include/KF5/KGuiAddons/KCursorSaver
/usr/include/KF5/KGuiAddons/KDateValidator
/usr/include/KF5/KGuiAddons/KFontUtils
/usr/include/KF5/KGuiAddons/KIconUtils
/usr/include/KF5/KGuiAddons/KImageCache
/usr/include/KF5/KGuiAddons/KModifierKeyInfo
/usr/include/KF5/KGuiAddons/KSystemClipboard
/usr/include/KF5/KGuiAddons/KWordWrap
/usr/include/KF5/KGuiAddons/KeySequenceRecorder
/usr/include/KF5/KGuiAddons/kcolorcollection.h
/usr/include/KF5/KGuiAddons/kcolormimedata.h
/usr/include/KF5/KGuiAddons/kcolorutils.h
/usr/include/KF5/KGuiAddons/kcursorsaver.h
/usr/include/KF5/KGuiAddons/kdatevalidator.h
/usr/include/KF5/KGuiAddons/keysequencerecorder.h
/usr/include/KF5/KGuiAddons/kfontutils.h
/usr/include/KF5/KGuiAddons/kguiaddons_export.h
/usr/include/KF5/KGuiAddons/kguiaddons_version.h
/usr/include/KF5/KGuiAddons/kiconutils.h
/usr/include/KF5/KGuiAddons/kimagecache.h
/usr/include/KF5/KGuiAddons/klocalimagecacheimpl.h
/usr/include/KF5/KGuiAddons/kmodifierkeyinfo.h
/usr/include/KF5/KGuiAddons/kmodifierkeyinfoprovider_p.h
/usr/include/KF5/KGuiAddons/ksystemclipboard.h
/usr/include/KF5/KGuiAddons/kwordwrap.h
/usr/lib64/cmake/KF5GuiAddons/KF5GuiAddonsConfig.cmake
/usr/lib64/cmake/KF5GuiAddons/KF5GuiAddonsConfigVersion.cmake
/usr/lib64/cmake/KF5GuiAddons/KF5GuiAddonsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5GuiAddons/KF5GuiAddonsTargets.cmake
/usr/lib64/libKF5GuiAddons.so
/usr/lib64/qt5/mkspecs/modules/qt_KGuiAddons.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5GuiAddons.so.5
/usr/lib64/libKF5GuiAddons.so.5.91.0
/usr/lib64/qt5/plugins/kf5/kguiaddons/kmodifierkey/kmodifierkey_xcb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kguiaddons/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kguiaddons/28ba3ebe1aa04fad742c69eb685e2a5376e9276f
/usr/share/package-licenses/kguiaddons/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kguiaddons/34f19e47876c7baa72ae7cc9acb28d8c2269b098
/usr/share/package-licenses/kguiaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kguiaddons/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kguiaddons/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kguiaddons/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kguiaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kguiaddons/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kguiaddons/e712eadfab0d2357c0f50f599ef35ee0d87534cb
