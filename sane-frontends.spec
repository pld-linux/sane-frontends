#
# Conditional build:
%bcond_without	gimp	# don't build GIMP plugin
%bcond_with	gtk1	# use GTK 1.2.x for GUI (for eg. for GIMP 1.2)
#
Summary:	SANE - easy local and networked scanner access
Summary(es):	SANE - acceso a scanners en red y locales
Summary(ko):	스캐너를 다루는 소프트웨어
Summary(pl):	SANE - prosta obs퀅ga skaner�w lokalnych i sieciowych
Summary(pt_BR):	Front-ends para o SANE
Name:		sane-frontends
Version:	1.0.12
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.mostang.com/pub/sane/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6a6166428491b268f5ebe03f16d1bc1f
URL:		http://www.sane-project.org/
BuildRequires:	autoconf
%if %{with gtk1}
BuildRequires:	gtk+-devel >= 1.2.0
%{?with_gimp:BuildRequires:	gimp-devel < 1.3.0}
%{?with_gimp:BuildRequires:	gimp-devel >= 1:1.2.0}
%else
BuildRequires:	gtk+2-devel >= 2.0.0
%{?with_gimp:BuildRequires:	gimp-devel >= 1:1.3.23}
%endif
BuildRequires:	sane-backends-devel >= 1.0.11
%requires_eq	sane-backends
Obsoletes:	xscanimage
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with gimp}
%define		gimpplugindir	%(gimptool --gimpplugindir)
%endif

%description
SANE (Scanner Access Now Easy) is a sane and simple interface to both
local and networked scanners and other image acquisition devices like
digital still and video cameras.

This packages contains frontends for SANE: xscanimage and xcam.

%description -l es
SANE - acceso a scanners en red y locales.

%description -l pl
SANE (Scanner Access Now Easy) jest rozs켨nym i prostym interfejsem do
skaner�w, zar�wno lokalnych jak i sieciowych, oraz innych urz켨ze� do
pozyskiwania obraz�w, jak cyfrowe aparaty i kamery.

Ten pakiet zawiera frontendy dla SANE: xscanimage i xcam.

%description -l pt_BR
SANE (Scanner Access Now Easy) � uma interface para scanners e outros
dispositivos locais e remotos de aquisi豫o de imagens tais como
c�meras digitais. SANE atualmente suporta um grande numero de
scanners, incluindo modelos da Agfa SnapScan, Apple, Artec, Canon,
CoolScan, Epson, HP, Microtek, Mustek, Nikon, Siemens, Tamarack, UMAX,
Connectix QuickCams e outros. Este pacote n�o habilita scanning por
rede por default; se voc� quiser habilitar essa caracter�stica,
verifique o manpage do saned(1).

%prep
%setup -q

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
%attr(755,root,root) %{_bindir}/*
%{?with_gimp:%attr(755,root,root) %{gimpplugindir}/plug-ins/*}
%{_mandir}/man1/*
%{_datadir}/sane
