%define	gimp_ver	1.2
Summary:	SANE - Easy local and networked scanner access
Summary(pl):	SANE - Prosta obs³uga skanerów lokalnych i sieciowych
Name:		sane-frontends
Version:	1.0.6
Release:	1
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Group(pt):	X11/Aplicações/Gráficos
License:	GPL
Source0:	ftp://ftp.mostang.com/pub/sane/sane-%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.mostang.com/sane/
BuildRequires:	sane-backends-devel
BuildRequires:	gimp-devel
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
SANE (Scanner Access Now Easy) is a sane and simple interface to both
local and networked scanners and other image acquisition devices like
digital still and video cameras.

This packages contains frontends for SANE: xscanimage and xcam.

%description -l pl
SANE (Scanner Access Now Easy) jest rozs±dnym i prostym insterfejsem
do skanerów, zarówno lokalnych jak i sieciowych, oraz innych urz±dzeñ
do pozyskiwania obrazów, jak cyfrowe aparaty i kamery.

Ten pakiet zawiera frontendy dla SANE: xscanimage i xcam.

%prep
%setup -q
%patch0 -p1

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gimp/%{gimp_ver}/plug-ins

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_bindir}/xscanimage $RPM_BUILD_ROOT%{_libdir}/gimp/%{gimp_ver}/plug-ins

gzip -9nf AUTHORS NEWS PROBLEMS TODO Changelog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gimp/%{gimp_ver}/plug-ins/*
%{_mandir}/man1/*
%{_datadir}/*
