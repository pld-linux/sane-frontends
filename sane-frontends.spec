%define	gimp_ver	1.2
Summary:	SANE - Easy local and networked scanner access
Summary(pl):	SANE - Prosta obs³uga skanerów lokalnych i sieciowych
Summary(pt_BR):	Front-ends para o SANE
Name:		sane-frontends
Version:	1.0.10
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.mostang.com/pub/sane/%{name}-%{version}.tar.gz
URL:		http://www.mostang.com/sane/
BuildRequires:	sane-backends-devel
%{!?_without_gimp:BuildRequires:	gimp-devel}
BuildRequires:	autoconf
Obsoletes:	xscanimage
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if 0%{!?_without_gimp:1}
%define		gimpplugindir	%(gimp-config --gimpplugindir)
%endif

%description
SANE (Scanner Access Now Easy) is a sane and simple interface to both
local and networked scanners and other image acquisition devices like
digital still and video cameras.

This packages contains frontends for SANE: xscanimage and xcam.

%description -l es
SANE - acceso a scanners en red y locales.

%description -l pl
SANE (Scanner Access Now Easy) jest rozs±dnym i prostym interfejsem do
skanerów, zarówno lokalnych jak i sieciowych, oraz innych urz±dzeñ do
pozyskiwania obrazów, jak cyfrowe aparaty i kamery.

Ten pakiet zawiera frontendy dla SANE: xscanimage i xcam.

%description -l pt_BR
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

%build
%{__autoconf}
%configure \
	%{?_without_gimp:--disable-gimp}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%if 0%{!?_without_gimp:1}
install -d $RPM_BUILD_ROOT%{gimpplugindir}/plug-ins
ln -sf %{_bindir}/xscanimage $RPM_BUILD_ROOT%{gimpplugindir}/plug-ins
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS PROBLEMS TODO Changelog
%attr(755,root,root) %{_bindir}/*
%{!?_without_gimp:%attr(755,root,root) %{gimpplugindir}/plug-ins/*}
%{_mandir}/man1/*
%{_datadir}/*
