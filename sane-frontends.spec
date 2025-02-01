#
# Conditional build:
%bcond_with	gimp	# GIMP plugin
%bcond_with	gtk1	# use GTK+ 1.2.x for GUI (for eg. for GIMP 1.2)
#
Summary:	SANE - easy local and networked scanner access
Summary(es.UTF-8):	SANE - acceso a scanners en red y locales
Summary(ko.UTF-8):	스캐너를 다루는 소프트웨어
Summary(pl.UTF-8):	SANE - prosta obsługa skanerów lokalnych i sieciowych
Summary(pt_BR.UTF-8):	Front-ends para o SANE
Name:		sane-frontends
Version:	1.0.14
Release:	2
License:	GPL v2+
Group:		X11/Applications/Graphics
#Source0Download: https://gitlab.com/sane-project/frontends/tags
Source0:	https://gitlab.com/sane-project/frontends/uploads/14e5c5a9205b10bd3df04501852eab28/%{name}-%{version}.tar.gz
# Source0-md5:	c63bf7b0bb5f530cf3c08715db721cd3
Patch0:		sane-backends-1_20.patch
Patch1:		%{name}-c99.patch
Patch2:		%{name}-configure-c99.patch
URL:		http://sane-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
%if %{with gtk1}
%{?with_gimp:BuildRequires:	gimp-devel < 1.3.0}
%{?with_gimp:BuildRequires:	gimp-devel >= 1:1.2.0}
BuildRequires:	gtk+-devel >= 1.2.0
%else
%{?with_gimp:BuildRequires:	gimp-devel >= 1:1.3.23}
BuildRequires:	gtk+2-devel >= 1:2.0.0
%endif
BuildRequires:	sane-backends-devel >= 1.0.14
Requires:	sane-backends >= 1.0.14
Obsoletes:	xscanimage
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with gimp}
%define		gimpplugindir	%(gimptool --gimpplugindir 2>/dev/null || echo ERROR)
%endif

%description
SANE (Scanner Access Now Easy) is a sane and simple interface to both
local and networked scanners and other image acquisition devices like
digital still and video cameras.

This packages contains frontends for SANE: xscanimage and xcam.

%description -l es.UTF-8
SANE - acceso a scanners en red y locales.

%description -l pl.UTF-8
SANE (Scanner Access Now Easy) jest rozsądnym i prostym interfejsem do
skanerów, zarówno lokalnych jak i sieciowych, oraz innych urządzeń do
pozyskiwania obrazów, jak cyfrowe aparaty i kamery.

Ten pakiet zawiera frontendy dla SANE: xscanimage i xcam.

%description -l pt_BR.UTF-8
SANE (Scanner Access Now Easy) é uma interface para scanners e outros
dispositivos locais e remotos de aquisição de imagens tais como
câmeras digitais. SANE atualmente suporta um grande numero de
scanners, incluindo modelos da Agfa SnapScan, Apple, Artec, Canon,
CoolScan, Epson, HP, Microtek, Mustek, Nikon, Siemens, Tamarack, UMAX,
Connectix QuickCams e outros. Este pacote não habilita scanning por
rede por default; se você quiser habilitar essa característica,
verifique o manpage do saned(1).

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure \
	%{!?with_gimp:--disable-gimp} \
	%{?with_gimp:%{?with_gtk1:--enable-gimp12}} \
	%{?with_gtk1:--disable-gtk2}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with gimp}
install -d $RPM_BUILD_ROOT%{gimpplugindir}/plug-ins
ln -sf %{_bindir}/xscanimage $RPM_BUILD_ROOT%{gimpplugindir}/plug-ins
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog NEWS PROBLEMS README
%attr(755,root,root) %{_bindir}/scanadf
%attr(755,root,root) %{_bindir}/xcam
%attr(755,root,root) %{_bindir}/xscanimage
%{?with_gimp:%attr(755,root,root) %{gimpplugindir}/plug-ins/xscanimage}
%{_mandir}/man1/scanadf.1*
%{_mandir}/man1/xcam.1*
%{_mandir}/man1/xscanimage.1*
%{_datadir}/sane
